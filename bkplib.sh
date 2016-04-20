#!/bin/bash
#====================================
# Prog starts by crontab
# incremental backup of library: files, added last month
# Autor: vasily122@yandex.ru
# Date: 2016 apr 20
# Version: 1.2
#====================================
filename=LIBRARY_$(date +%d_%m_%Y)
prefix=~
tar cvzf - `find ~/LIBRARY -ctime +11 -print` > $prefix/$filename.tgz
#touch ~/Рабочий\ стол/saved_$(date +%d_%m_%Y).txt
#report to logfile and mail
echo -e "BACKUP_LIBRARY_$(date +%d_%m_%Y)" >> ~/log.txt
echo -e "Backup_LIBRARY_$(date +%d_%m_%Y)" | mail -s "Backup LIB report" vasily122@yandex.ru
