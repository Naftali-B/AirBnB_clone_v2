#!/bin/bash

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
	    apt-get update
	        apt-get -y install nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
    </head>
      <body>
          Test HTML file
	    </body>
	    </html>" > /data/web_static/releases/test/index.html

	    # Create or recreate symbolic link
	    rm -rf /data/web_static/current
	    ln -sf /data/web_static/releases/test/ /data/web_static/current

	    # Set ownership of /data/ directory to ubuntu user and group
	    chown -R ubuntu:ubuntu /data/

	    # Update Nginx configuration
	    config_file="/etc/nginx/sites-available/default"
	    sed -i '/^\s*location \/hbnb_static\/ {/a \        alias /data/web_static/current/;' $config_file

	    # Restart Nginx
	    service nginx restart

	    exit 0

