#!/bin/bash
amazon-linux-extras install epel -y
yum install -y nginx
service nginx restart
systemctl enable nginx
echo "<html><H1>this is my website!!. this server ip is `curl ident.me --silent`</h1></html>" > /usr/share/nginx/html/index.html