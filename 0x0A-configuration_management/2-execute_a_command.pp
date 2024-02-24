# Puppet manifest to kill a process named "killmenow" using pkill

exec { 'kill_process':
  command     => '/usr/bin/pkill killmenow',
  path        =>['/usr/bin/bash'],
  refreshonly => true,
  subscribe   => Exec['check_process'],
}

exec { 'check_process':
  command     => '/usr/bin/pgrep killmenow',
  returns     => [0, 1],
  refreshonly => true,
}