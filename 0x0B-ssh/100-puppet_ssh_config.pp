#Creates an ssh config file for our server


file { '/etc/ssh/ssh_config':
  ensure  => present,
content => "
    # SSH client configuration
    Host ubuntu-online
      HostName 54.209.112.112
      User ubuntu
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
