# Automating adding headers using puppet

package { 'nginx':
  ensure  => installed,
}

file_line { 'add header':
  ensure  => 'present',
  after   => 'server_name _;'
  line    => '      add_header X-Served-By $HOSTNAME;',
  path    => '/etc/nginx/sites-available/default',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
