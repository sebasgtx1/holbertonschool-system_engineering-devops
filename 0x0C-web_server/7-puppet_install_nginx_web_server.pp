# Install Nginx web server (w/ Puppet)
exec { 'Nginx_install':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello wolrd" > /var/www/html/index.html ; sudo sed -i "s/server_name _; sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4\&ab_channel=NyanCat permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
  provider => 'shell',
}

