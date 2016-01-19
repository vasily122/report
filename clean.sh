#!/bin/bash
#====================================
#Prog starts in time by crontab and cleans download folder "~/Загрузки"
#look ПРАВИЛА
#after cleaning crontab lunch script sort.sh
#Author: vasily122@yandex.ru
#Date: 2016 jan 19
#Version: 1.5
#====================================
point=sort_$(date +%d_%m_%Y)
library=~/LIBRARY
#--- make dirs  for daily sort ----
mkdir ~/to_sort/$point
mkdir ~/to_sort/$point/{txt,pics,arch}
#--- sort files by type in daily sort dir ---
mv ~/Загрузки/*.{jpg,JPG,jpeg,JPEG,png,PNG,gif,GIF} ~/to_sort/$point/pics
mv ~/Загрузки/*.{txt,TXT,pdf,PDF,djvu,odt} ~/to_sort/$point/txt
mv ~/Загрузки/*.{rar,RAR,arj,ARJ,zip,ZIP,tar,7z} ~/to_sort/$point/arch
# gz,bz2,deb,tgz
#--- any other not selected ---
mv ~/Загрузки/*.* ~/to_sort/$point
#--- report ---
echo -e "cleaned_$(date +%d_%m_%Y)" >> ~/to_sort/log.txt
#--- REMOVE CACHE and THUMBS ---
#rm -R /home/evrosvet/.{thumbnails,cache}
