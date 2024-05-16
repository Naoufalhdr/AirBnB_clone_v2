# Puppet Manifest to set up web servers for the deployment of web_static.

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories if they don't exist
file { ['/data/web_static/releases/test/', '/data/web_static/shared/']:
  ensure => directory,
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
}

# Create or recreate the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  force  => true,
}

# Set ownership recursively to the ubuntu user and group
file { '/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
	listen 80;
	listen [::]:80;

	server_name _;

	location /hbnb_static/ {
		alias /data/web_static/current/;
		index index.html;
	}
}
",
  notify  => Service['nginx'],
}

# Restart nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
}
