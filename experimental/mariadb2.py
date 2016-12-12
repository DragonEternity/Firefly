# Auto-installs mariadb with pw.
# This currently works but it's extremely stupid.

from subprocess import call
import os
key = "0xcbcb082a1bb943db"
repo = "deb [arch=amd64,i386] http://ftp.nluug.nl/db/mariadb/repo/10.1/debian jessie main"
pw = "lol"

def preinstall():
     call(["apt-get", "install", "--yes", "--force-yes", "software-properties-common"], stdout=open(os.devnull))
     call(["apt-key", "adv", "--recv-keys", "--keyserver", "keyserver.ubuntu.com", key], stdout=open(os.devnull))
     call(["add-apt-repository", repo], stdout=open(os.devnull))
     call(["apt-get", "--yes", "--force-yes", "update"], stdout=open(os.devnull)) 
     os.environ["DEBIAN_FRONTEND"] = "noninteractive"
     call(["apt-get", "install", "--yes", "--force-yes", "mariadb-server-10.1"], stdout=open(os.devnull)) 

def changepwd():
     call(["mysql", "-u", "root", "-e", "SET PASSWORD FOR root@localhost = PASSWORD("+"'"+pw+"'"+");"])


preinstall()
changepwd()
