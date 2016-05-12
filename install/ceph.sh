wget -q -O- 'https://download.ceph.com/keys/release.asc' | apt-key add -
echo deb http://download.ceph.com/debian-{ceph-stable-release}/ $(lsb_release -sc) main | tee /etc/apt/sources.list.d/ceph.list
apt-get update
apt-get install --yes --force-yes ceph-deploy