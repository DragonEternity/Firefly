mysql -u root -pKOjgkn39g8sdv -e "CREATE DATABASE owncloud;"
mysql -u root -pKOjgkn39g8sdv -e "GRANT ALL ON owncloud.* to 'owncloud'@'localhost' IDENTIFIED BY '1234'"
mysql -u root -pKOjgkn39g8sdv -e "RENAME USER 'root' TO 'boat'@'localhost'"
