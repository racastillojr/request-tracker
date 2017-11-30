#!/usr/bin/env python

#==================================================================================
#Created by Ramon Castillo - rcjr@uic.edu
#Univerisity of Illinois at Chicago
#Academic Computing and Communications Center
#Enterprise Architecture and Development
#==================================================================================


import os
import sys
import subprocess
import filecmp
import time

#rtInstance = raw_input("Instance?:e.g., accc ")

#Check if the directory exist
#if os.path.isdir(rtInstance):
#    print(rtInstance+"exists. Checking aliases")
#else:
#    sys.exit("Can't find "+rtInstance+". Check instance.")

#This gets all the aliases associated with rt on the server
getalises = os.system("cat /usr/local/rt/aliases |awk '{print $1}' |grep -Ev '#' |sed 's/://g' |awk '!/^$/' > /usr/local/rt/production/accc_core_mods/global/rt-aliases.main")


currentAliases = "/usr/local/rt/production/accc_core_mods/global/rt-aliases.current"
allAliases = "/usr/local/rt/production/accc_core_mods/global/rt-aliases.main"
regexFile = "/usr/local/rt/production/accc_core_mods/global/email-regex.pm"


#compare the main and current rt-aliases
compareAliases = filecmp.cmp(currentAliases,allAliases)

if compareAliases == False:
    print("Need to update current alias list...Updating")
    time.sleep(3)
    #update current alias list
    os.system("cat "+allAliases+" > "+currentAliases)
    time.sleep(2)
    #Compare main and current rt-aliases file again
    compareAliases = filecmp.cmp(currentAliases,allAliases)

    if compareAliases == False:
        sys.exit("Could not update file...Please check")
    else:
        print("List sync'd...updating email-regex.pm file")

        readallAliases = open(allAliases, 'r')
        openregexFile = open(regexFile, 'w')
        with readallAliases as fo:
                data=fo.read().replace('\n', '|').replace (',', '')
                with openregexFile as f:
                    f.write("Set($RTAddressRegexp, '^(")
                    f.write(data)
                    f.write(")?\@(helpdesk.uic.edu|uic.edu)|(\@helpdesk[^.]*\.uic\.edu)|(\@LISTSERV\.UIC\.EDU)|(\@helpdesk\.uillinois\.edu)|(eclerk\@helpdesk\.admin\.uillinois\.edu)|(AITSESAscanNotice\@uillinois\.edu)$');")

                    print(" ")
                    print("Done...")
                    print(" ")
                    print("Update complete...Closing files")
                    #Close files
                    openregexFile.close()
                    readallAliases.close()

