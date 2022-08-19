exec { 'Kill_process':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  }

