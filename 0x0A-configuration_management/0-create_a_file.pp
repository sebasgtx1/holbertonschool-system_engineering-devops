# Using Puppet, create a file in /tmp.
file { 'school':
  path    => '/tmp/school',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
  }
