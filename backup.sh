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
tar -czf  /home/evrosvet/$filename.tgz  /home/evrosvet/Mail  /home/evrosvet/.sylpheed-2.0  /home/evrosvet/.purple /home/evrosvet/.Skype

#cd /mnt/backup
#sudo tar cvpzf /home/evrosvet/backup_`date +%Y.%m.%d_%H_%M`.tgz --exclude=/media --exclude=/proc --exclude=/lost+found --exclude=/mnt  --exclude=/home --exclude=/sys / >> /dev/null 2>&1

#--- REMOVE CACHE and THUMBS ---
rm -R /home/evrosvet/.thumbnails
rm -R /home/evrosvet/.cache

#--- report ---
touch ~/Рабочий\ стол/saved_$(date +%d_%m_%Y).txt
# todo: probable, we need some kind of log-file?
