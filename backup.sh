#!/bin/bash
filename=backup_$(date +%d_%m_%Y)
tar -czf  /home/evrosvet/$filename.tgz  /home/evrosvet/Mail  /home/evrosvet/.sylpheed-2.0  /home/evrosvet/.purple /home/evrosvet/.Skype

#--- REMOVE CACHE and THUMBS ---
rm -R /home/evrosvet/.thumbnails
rm -R /home/evrosvet/.cache

touch ~/Рабочий\ стол/mail_saved$(date +%d_%m_%Y).txt
