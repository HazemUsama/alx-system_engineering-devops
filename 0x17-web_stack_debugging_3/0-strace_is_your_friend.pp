# Strace is your friend
include stdlib

file_line {'Fix the typo':
  ensure  => present,
  path    => '/var/www/html/wp-settings.php',
  line    => 'equire_once( ABSPATH . WPINC . "/class-wp-locale.php" );',
  replace => true,

}
