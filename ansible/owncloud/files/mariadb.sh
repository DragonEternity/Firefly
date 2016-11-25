#!/bin/bash
apt-get --yes --force-yes install software-properties-common
#apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
add-apt-repository 'deb [arch=amd64,i386] http://ftp.nluug.nl/db/mariadb/repo/10.1/debian jessie main'
apt-get update
export DEBIAN_FRONTEND=noninteractive
debconf-set-selections <<< 'mariadb-server-10.1 mysql-server/root_password password KOjgkn39g8sdv'
debconf-set-selections <<< 'mariadb-server-10.1 mysql-server/root_password_again password KOjgkn39g8sdv'
apt-get install -y mariadb-server-10.1
apt-get --yes --force-yes install mariadb-server
