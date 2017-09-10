#!/usr/bin/expect -f
set ip [lindex $argv 0];
set port [lindex $argv 1];
set password [lindex $argv 2];
spawn ssh  -o StrictHostKeyChecking=no -R 19999:localhost:$port $ip
expect "*?assword:*"
send "$password\r"
expect "*#"
send "touch /tmp/done\r"
interact