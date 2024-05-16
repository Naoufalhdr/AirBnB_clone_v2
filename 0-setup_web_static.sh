#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
	apt-get update
	apt-get -y install nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate the symbolic link
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership recursively to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content="
server {
	listen 80;
	listen [::]:80;

	server_name _;

	location /hbnb_static/ {
		alias /data/web_static/current/;
		index index.html;
	}
}
"
echo "$config_content" | tee /etc/nginx/sites-available/default > /dev/null

# Restart nginx
service nginx restart

exit 0
