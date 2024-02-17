#Fix typo

exec { 'command':
  command  => '
  sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php
  service apache2 restrat',
  provider => shell,
  }
