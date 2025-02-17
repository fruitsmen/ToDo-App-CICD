#!/bin/sh

echo "Install package..."
sudo apt update && install -y python3 python3-pip postgresql postgresql-contrib nginx
pip install -r requirements.txt

echo "Setup DB..."
sudo -u postgres psql -c "CREATE DATABASE todolist;"
sudo -u postgres psql -c "CREATE USER todouser WITH PASSWORD 'password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE todolist TO todouser;"

echo "Setup Nginx..."
sudo cp ./config/nginx/todoapp /etc/nginx/sites-enabled/
sudo systemctl restart nginx
