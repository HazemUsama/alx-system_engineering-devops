#creating a custom HTTP header response
exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i '/gzip on;/a\
  add_header X-Served-By $hostname;
  ' /etc/nginx/nginx.conf;
  service nginx start'
  provider => shell,
  }
