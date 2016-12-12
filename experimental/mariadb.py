# Requires python3-apt to be installed through the debian package manager.
# This currently doesn't work.

from subprocess import call
import apt
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
     call(["debconf-set-selections", "<<<", "'""mariadb-server-10.1", "mysql-server/root_password", "password", pw,"'"], shell=True)
     call(["debconf-set-selections", "<<<", "'","mariadb-server-10.1 mysql-server/root_password_again", "password", pw,"'"], shell=True)
     
def install():
     call(["apt-get", "install", "--yes", "--force-yes", "mariadb-server-10.1"])

preinstall()
feedpw()
install()
