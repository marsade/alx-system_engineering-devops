#!/usr/bin/puppet

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}

# Ensure Flask is installed with version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# Ensure Werkzeug is installed with version 2.1.1
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
