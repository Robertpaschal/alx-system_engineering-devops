# Puppet mainfest to install Flask version 2.1.0 using pip3

package { 'python3-pip':
  ensure   => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',

}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}