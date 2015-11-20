#!/bin/bash
# prototipe only, carefull!
cd /mnt/backup
sudo tar cvpzf /home/evrosvet/backup_`date +%Y.%m.%d_%H_%M`.tgz --exclude=/media --exclude=/proc --exclude=/lost+found --exclude=/mnt  --exclude=/home --exclude=/sys / >> /dev/null 2>&1
