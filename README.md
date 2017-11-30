# request-tracker

This script will add RT queue emails in the email-regex.pm config so RT instances do not email or accept email from other RT instance.
Without configuring email-regex, you run the risk of emails being in a loop becasue of auto-reply.

This script can be ran manually or set as a cron job to update the email-regex.pm config.

If you manage several instance, it may be best to manage one file and create a symbolic link in the RT_SiteConfig.d directory of your 
instance pointing to the actual file.

