#!/bin/bash
#====================================
#Prog starts in time by crontab and cleans download folder "~/Загрузки"
#look ПРАВИЛА
#after clean.sh crontab lunchs sort.sh
#Author: vasily122@yandex.ru
#Date: 2016 mar 3
#Version: 2.0
#====================================
point=sort_$(date +%d_%m_%Y)
library=~/LIBRARY
#--- make dirs  for daily sort ----
mkdir ~/to_sort/$point
mkdir ~/to_sort/$point/{txt,pics,arch}

prename 's/\s+/-/g' ~/Загрузки/*.*              #--- remove spaces ---
prename 's/\,/-/g' ~/Загрузки/*.*               #--- change defis to underline --
prename 's/\)/-/g' ~/Загрузки/*.*               #--- remove brackets ---
prename 's/\(/-/g' ~/Загрузки/*.*               #---
prename 's/_-_/-/g' ~/Загрузки/*.*              #--- remove _-_
prename 's/\:/-/g' ~/Загрузки/*.*               #--- remove :
prename 's/\;/-/g' ~/Загрузки/*.*               #--- remove ;
prename 's/\~/-/g' ~/Загрузки/*.*               #--- remove ~
prename 's/--/-/g' ~/Загрузки/*.*               #--- change pairs of defises
prename 's/__/-/g' ~/Загрузки/*.*               #--- change pairs of defises

#--- sort files by type in daily sort dir ---
mv ~/Загрузки/*.{jpg,JPG,jpeg,JPEG,png,PNG,gif,GIF} ~/to_sort/$point/pics
mv ~/Загрузки/*.{txt,TXT,pdf,PDF,djvu,odt} ~/to_sort/$point/txt
mv ~/Загрузки/*.{rar,RAR,arj,ARJ,zip,ZIP,tar,7z,gz,bz2,tgz} ~/to_sort/$point/arch
# deb
#--- any other not selected ---
mv ~/Загрузки/*.* ~/to_sort/$point
#--- report ---
echo -e "cleaned_$(date +%d_%m_%Y)" >> ~/to_sort/log.txt

#--- REMOVE CACHE and THUMBS ---
#rm -R /home/evrosvet/.{thumbnails,cache}
