#creating a custom HTTP header response

exec { 'command':
  command  => 'sudo apt-get -y update;
  sudo apt-get -y install nginx;
  sudo sed -i "/gzip on;/a\ add_header X-Served-By $hostname;" /etc/nginx/nginx.conf;
  sudo service nginx start'
  provider => shell,
  }
