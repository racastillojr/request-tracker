# request-tracker

<b>update-rt-regex.py:</b>
This script will add RT queue emails in the email-regex.pm config so RT instances do not email or accept email from other RT instance.
Without configuring email-regex, you run the risk of emails being in a loop becasue of auto-reply.

This script can be ran manually or set as a cron job to update the email-regex.pm config.

If you manage several instance, it may be best to manage one file and create a symbolic link in the RT_SiteConfig.d directory of your 
instance pointing to the actual file.

<b>rtctl.py:</b>
This script assumes you are using postfix. It blocks spammers for all instances hosted on your server by rejecting mail at /etc/postfix/access. This script will eventually have several argument to perform other tasks.
Also, make sure you have the following defined in /etc/postfix/main.cf

smtpd_sender_restrictions = hash:/etc/postfix/access

