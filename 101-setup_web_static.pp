# Setup the web servers for the deployment of web_static
exec { '/usr/bin/env apt -y update' : }
-> package { 'nginx':
  ensure => installed,
}
-> file { '/data':
  ensure  => 'directory'
}
-> file { '/data/web_static':
  ensure => 'directory'
}
-> file { '/data/web_static/releases':
  ensure => 'directory'
}
-> file { '/data/web_static/releases/test':
  ensure => 'directory'
}
-> file { '/data/web_static/shared':
