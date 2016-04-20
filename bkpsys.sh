#!/bin/bash
#====================================
# Prog starts by crontab
# backup system arter rsync by cron
# Autor: vasily122@yandex.ru
# Date: 2016 apr 20
# Version: 0.7
#====================================
filename=system_backup_$(date +%d_%m_%Y)
prefix=/home/.backup
tar -cvzpf ~/$filename.tgz  --exclude=$prefix/media --exclude=$prefix/proc --exclude=$prefix/lost+found --exclude=$prefix/mnt  --exclude=$prefix/home --exclude=$prefix/sys  $prefix >> /dev/null 2>&1
#report to logfile and mail
echo -e "BACKUP_SYSTEM_$(date +%d_%m_%Y)" >> ~/log.txt
history | mail -s "Backup_SYS_$(date +%d_%m_%Y)" vasily122@yandex.ru
