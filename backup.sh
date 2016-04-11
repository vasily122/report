#!/bin/bash
#====================================
# Prog starts by crontab 
# backup home direcrory (only mail, chats) by shedule and remove caches
# Autor: vasily122@yandex.ru
# Date: 2016 apr 11
# Version: 0.4
#====================================
filename=backup_$(date +%d_%m_%Y)
prefix=~
#receive all messages before backup
#sylpheed --configdir /home/evrosvet/.sylpheed_-2.0 --receive-all
tar -czf $prefix/$filename.tgz $prefix/Mail $prefix/.sylpheed-2.0 $prefix/.purple $prefix/.Skype

#TODO: full backup of home folder -IN WORK!
#cd /mnt/backup
#sudo tar cvpzf $prefix/backup_`date +%Y.%m.%d_%H_%M`.tgz --exclude=/media --exclude=/proc --exclude=/lost+found --exclude=/mnt  --exclude=/home --exclude=/sys / >> /dev/null 2>&1
#TODO --- REMOVE CACHE and THUMBS ---
#rm -R $prefix/.thumbnails
#rm -R $prefix/.cache
#--- report ---
touch ~/Рабочий\ стол/saved_$(date +%d_%m_%Y).txt
echo -e "backup_$(date +%d_%m_%Y)" >> ~/log.txt
