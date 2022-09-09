# Install Nginx web server (w/ Puppet)
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_redirect'],
}

exec { 'add_redirect':
  provider    => shell,
  command     => 'sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4\&ab_channel=NyanCat permanent;/" /etc/nginx/sites-available/default',
  before      => Exec['restart Nginx'],
}

exec { 'add_index':
  provider    => shell,
  command     => 'echo "Hello World" > /var/www/html/index.html',
  before      => Exec['add_redirect'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
