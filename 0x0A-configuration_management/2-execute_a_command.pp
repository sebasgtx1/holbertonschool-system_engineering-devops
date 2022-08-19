# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'Kill_process':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  }

