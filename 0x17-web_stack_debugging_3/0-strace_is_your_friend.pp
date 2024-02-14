# A puppet script to replace the extension of a file in the wordpress setting file
$setting_file = '/var/www/html/wp-settings.php'
# replace the class name extension from phpp to php
exec { 'replace_class_name':
 command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${setting_file}",
 path => ['/bin','/usr/bin']
}
