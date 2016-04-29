apt-get install lsb-release
cd /tmp && wget http://archive.zfsonlinux.org/debian/pool/main/z/zfsonlinux/zfsonlinux_6_all.deb
dpkg -i zfsonlinux_6_all.deb
apt-get update
apt-get --yes --force-yes install debian-zfs