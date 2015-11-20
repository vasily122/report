#!/bin/bash
#====================================
#Prog starts in time by crontab and cleans DOWNLOAD folder
# смотри файл ПРАВИЛА
# after cleaning crontab lunch script sort.sh
#Author: vasily122@yandex.ru
#Date: #2015 nov 18
#Version: 1.1
#====================================

point=sort_$(date +%d_%m_%Y)
library=/home/evrosvet/LIBRARY/
#echo $point

#--- make dirs  for daily sort ----
mkdir ~/to_sort/$point
mkdir ~/to_sort/$point/{txt,pics,arch}

#--- sort files by type in daily sort dir ---
mv ~/Загрузки/*.{jpg,JPG,jpeg,JPEG,png,PNG,gif,GIF} ~/to_sort/$point/pics
mv ~/Загрузки/*.{txt,TXT,pdf,PDF,djvu,odt} ~/to_sort/$point/txt
mv ~/Загрузки/*.{rar,RAR,arj,ARJ,zip,ZIP,tar} ~/to_sort/$point/arch
# gz,bz2,deb ?

#--- any other not selected ---
mv ~/Загрузки/*.* ~/to_sort/$point

#--- REMOVE CACHE and THUMBS ---
rm -R /home/evrosvet/.{thumbnails,cache}

#--- report ---
touch ~/Рабочий\ стол/cleaned$(date +%d_%m_%Y).txt
