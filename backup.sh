#!/bin/bash
#====================================
# Prog starts by crontab 
# backup home direcrory (only mail, chats) by shedule and remove caches
# Autor: vasily122@yandex.ru
# Date: 2016 apr 11
# Version: 1.0
#====================================
filename=backup_$(date +%d_%m_%Y)
prefix=~
tar -czf $prefix/$filename.tgz $prefix/Mail $prefix/.sylpheed-2.0 $prefix/.purple $prefix/.Skype
#--- report ---
echo -e "backup_$(date +%d_%m_%Y)" >> ~/log.txt
