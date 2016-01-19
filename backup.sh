#!/bin/bash
#====================================
# ---> It`s a prototype! Don`t work!
# Prog starts by crontab 
# backup home direcrory (only mail, chats) by shedule
# Autor: vasily122@yandex.ru
# Date: 2015 dec 7
# Version: 0.2
#====================================
filename=backup_$(date +%d_%m_%Y)
prefix=~/
tar -czf  $prefix/$filename.tgz  $prefix/Mail  $prefix/.sylpheed-2.0  $prefix/.purple $prefix/.Skype

#cd /mnt/backup
#sudo tar cvpzf $prefix/backup_`date +%Y.%m.%d_%H_%M`.tgz --exclude=/media --exclude=/proc --exclude=/lost+found --exclude=/mnt  --exclude=/home --exclude=/sys / >> /dev/null 2>&1

#--- REMOVE CACHE and THUMBS ---
rm -R $prefix/.thumbnails
rm -R $prefix/.cache

#--- report ---
touch ~/Рабочий\ стол/saved_$(date +%d_%m_%Y).txt
# todo: probable, we need some kind of log-file?
