apt-get --yes --force-yes install software-properties-common
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
add-apt-repository 'deb [arch=amd64,i386] http://ftp.nluug.nl/db/mariadb/repo/10.1/debian jessie main'
apt-get update
apt-get --yes --force-yes install mariadb-server