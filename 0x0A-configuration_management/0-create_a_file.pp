# Puppet manifest to creat a file in /tmp with specific permissions

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  group   => 'www-data',
  content => 'I love Puppet',
}
