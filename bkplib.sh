#!/bin/bash
#====================================
# Prog starts by crontab
# incremental backup of library: files, added last month
# Autor: vasily122@yandex.ru
# Date: 2016 mar 2
# Version: 0.1
#====================================
filename=LIBRARY_$(date +%d_%m_%Y)
prefix=~
tar cvf - `find ~/LIBRARY -ctime +30 -print` > $prefix/$filename.tar
#full bachup
#cd /mnt/backup
#sudo tar cvpzf $prefix/backup_`date +%Y.%m.%d_%H_%M`.tgz --exclude=/media --exclude=/proc --exclude=/lost+found --exclude=/mnt  --exclude=/home --exclude=/sys / >> /dev/null 2>&1

#--- REMOVE CACHE and THUMBS ---
#rm -R $prefix/.thumbnails
#rm -R $prefix/.cache
#--- report ---
touch ~/Рабочий\ стол/saved_$(date +%d_%m_%Y).txt
# todo: probable, we need some kind of log-file?
