# set up the client SSH configuration file to connect to a server

file { '/etc/ssh/ssh_config':
  ensure => 'present',
}

#exec { 'IdentityFile'
#    command => '/usr/bin/echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
#    provider => 'shell',
#}

exec { 'PasswordAutentication'
    command => '/usr/bin/echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config'
    provider => 'shell',
}
