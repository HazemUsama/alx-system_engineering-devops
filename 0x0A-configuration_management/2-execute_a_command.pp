# kill process killmenow

exec { 'pkill':
    command  => 'pkill killmenw',
    provider => 'shell',
  }
