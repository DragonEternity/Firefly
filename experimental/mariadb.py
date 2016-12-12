# Auto-installs mariadb with pw.
# This currently works but it's extremely stupid.

from subprocess import call
import os
key = "0xcbcb082a1bb943db"
repo = "deb [arch=amd64,i386] http://ftp.nluug.nl/db/mariadb/repo/10.1/debian jessie main"
pw = "lol"

def preinstall():
     call(["apt-get", "install", "--yes", "--force-yes", "software-properties-common"])
     call(["apt-key", "adv", "--recv-keys", "--keyserver", "keyserver.ubuntu.com", key])
     call(["add-apt-repository", repo])
     call(["apt-get", "--yes", "--force-yes", "update"])

def feedpw():
     os.environ["DEBIAN_FRONTEND"] = "noninteractive"

def install():
     call(["apt-get", "install", "--yes", "--force-yes", "mariadb-server-10.1"])
     call(["mysql", "-u", "root", "-e", "SET PASSWORD FOR root@localhost = PASSWORD("+"'"+pw+"'"+");"])



preinstall()
feedpw()
install()
