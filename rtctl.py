#!/usr/bin/env python

#==================================================================================
#Created by Ramon Castillo - rcjr@uic.edu
#Univerisity of Illinois at Chicago
#Academic Computing and Communications Center
#Enterprise Architecture and Development


#This script assumes you are using postfix. It blocks spammers for all instances
#hosted on your server by rejecting mail at /etc/postfix/access. 
#==================================================================================

import os
import subprocess
import argparse
import time
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--block-sender",
                    help="block email address or domain of user")

args = parser.parse_args()

#Check of user is root
if not os.geteuid() == 0:
    sys.exit("You must be root")


if args.block_sender:

    #Ensure UIC.edu and Gmail domain is not in blocked. You can block specific users from that domain, but you can't block the entire domain.
    if args.block_sender == '@uic.edu' or args.block_sender == '*@uic.edu' or args.block_sender == '%@uic.edu' or args.block_sender == 'uic.edu' or args.block_sender == 'gmail.com':
        sys.exit("You can not block the entire uic.edu domain")

    #Define sender access file
    access = "/etc/postfix/access"
    block_content = str(args.block_sender)+"	REJECT\n"
    #Reject email Address
    print("Adding "+args.block_sender+" to block list...")
    time.sleep(1)
    access_file = open(access,"a")
    access_file.write(block_content)
    access_file.close()

    print("Restarting postfix")
    os.system("service postfix restart")
    print("\n"+args.block_sender+" has been added to /etc/postfix/access")

