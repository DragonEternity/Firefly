wget -O - http://download.gluster.org/pub/gluster/glusterfs/LATEST/rsa.pub | apt-key add -
echo deb http://download.gluster.org/pub/gluster/glusterfs/LATEST/Debian/jessie/apt jessie main > /etc/apt/sources.list.d/gluster.list
apt-get update
apt-get --yes --force-yes install glusterfs-server glusterfs-client
