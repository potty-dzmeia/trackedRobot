#!/bin/bash

target=$1

count=$( ping -c 1 $target | grep icmp* | wc -l )

if [ $count -eq 0 ]
then
    #echo "Host is not Alive! Try again later.."
    echo "Server is down!" | mail -s owncloud_is_down  ch.levkov@gmail.com
else
    echo "Yes! Host is Alive!"
    #echo "Server is up and runnning" | mail -s owncloud_is_OK  ch.levkov@gmail.com
fi