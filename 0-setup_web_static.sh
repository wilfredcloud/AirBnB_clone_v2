#!/usr/bin/env bash

#Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

echo "Hello world" > /data/web_static/releases/test/index.html

# Delete the existing symbolic link if it exists
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi

# Create the new symbolic link
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Define the configuration file path
nginx_config="/etc/nginx/sites-available/default"

# Create a backup of the Nginx configuration file
sudo cp "$nginx_config" "$nginx_config.backup"

# Define the sed command to update the configuration
sed_command='s@location / {@location / {\n        location /hbnb_static/ {\n            alias /data/web_static/current/;\n        }\n@g'

# Use sed to update the configuration file
sudo sed -i "$sed_command" "$nginx_config"

# Restart Nginx to apply the changes
sudo systemctl restart nginx


