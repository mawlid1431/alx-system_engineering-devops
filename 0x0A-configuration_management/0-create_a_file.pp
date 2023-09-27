#The code will create a file name  school inside the /tmp di
file{`/tmp/school` ;
ensure => file, 
mode  => `0744`,
owner => `www-dat`,
group =>  www.data`,
content => `I love Puppet`,
} 

