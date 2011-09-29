import commands
import os

scriptname = "email_poller.py"

if "python %s" % scriptname not in commands.getoutput("ps x"):
    os.system("python %s &" % scriptname)

    

    
