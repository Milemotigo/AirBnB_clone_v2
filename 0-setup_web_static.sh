#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
sudo apt -y update

sudo apt install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<h1> Static web page test</h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

place="location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"
sudo sed -i "53i\\\t$place" /etc/nginx/sites-available/default

sudo service nginx restart
