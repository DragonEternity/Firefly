wget -q -O- "http://debian.saltstack.com/debian-salt-team-joehealy.gpg.key" | apt-key add -
deb http://debian.saltstack.com/debian jessie-saltstack main > /etc/apt/sources.list.d/saltstack.list
apt-get update
apt-get --yes --force-yes install salt-minion