#The code will create a file name  school inside the /tmp di
file{`/tmp/school` ;
ensure => file, 
content => `I love Puppet`,
mode  => `0744`,
owner => `www-dat`,
group =>  www.data`,
} 

