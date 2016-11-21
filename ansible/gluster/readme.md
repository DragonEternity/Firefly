Gluster with ansible
#########


A simple, rough ansible script I'm working on for my own intents and purposes. Mostly for learning ansible.

What does it do?
- Two different site.yml's. One is a complete install and the other only pushes config.
- Install GlusterFS-server/client, php5-mysql, php5-fpm and nginx.
- Make a gluster brick and mount it under /var/www/html.
- Push a simple backup script complete with cron entry.


What doesn't it do?
- The backup script requires some manual input as to where files should go.
- Requires a host file with the group [gluster_servers] or just edit the .yml's and define your own group.
