Syncs ezmlm-mailing list subscriptions with a web resource.

The web resource must be a text file listing all the wanted subscriptions for
the mailing list. When new emails are added to the text file, they are
automatically subscribed to the mailing list managed by ezmlm. Also when emails
are removed from the text file, they are also unsubscribed from the list.

To use the script you need to add *app/settings.py* with all the imported data. The file
might look something like

    web_resource_url = "http://path/to/csv/file.txt"
    gmail_username = "my_gmail@gmail.com"
    gmail_password = "my_password"
    ezmlm_listname = "list_name"
    ezmlm_domain = "domain-where-ezmlm-is-running.com"
    error_email = "address-for-error-emails@gmail.com"

TL;DR: Learning git.