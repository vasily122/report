#!/bin/bash
#====================================
#Prog starts in time by crontab and cleans download folder
#look ПРАВИЛА
#after clean.sh crontab lunchs sort.sh
#Author: vasily122@yandex.ru
#Date: 2016 mar 11
#Version: 2.1
#====================================
point=~/to_sort/sort_$(date +%d_%m_%Y)
library=~/LIBRARY
folder=~/Загрузки
#--- make dirs  for daily sort ----
mkdir $point
mkdir $point/{txt,pics,arch}

prename 's/\s+/-/g' $folder/*.*              #--- remove spaces ---
prename 's/\,/-/g' $folder/*.*               #--- change defis to underline --
prename 's/\)/-/g' $folder/*.*               #--- remove brackets ---
prename 's/\(/-/g' $folder/*.*               #---
prename 's/_-_/-/g' $folder/*.*              #--- remove _-_
prename 's/\:/-/g' $folder/*.*               #--- remove :
prename 's/\;/-/g' $folder/*.*               #--- remove ;
prename 's/\~/-/g' $folder/*.*               #--- remove ~
prename 's/--/-/g' $folder/*.*               #--- change pairs of defises
prename 's/__/-/g' $folder/*.*               #--- change pairs of defises

#--- sort files by type in daily sort dir ---
mv $folder/*.{jpg,JPG,jpeg,JPEG,png,PNG,gif,GIF} $point/pics
mv $folder/*.{txt,TXT,pdf,PDF,djvu,odt} $point/txt
mv $folder/*.{rar,RAR,arj,ARJ,zip,ZIP,tar,7z,gz,bz2,tgz,deb} $point/arch

#--- any other not selected ---
mv $folder/*.* $point
#--- report ---
echo -e "cleaned_$(date +%d_%m_%Y)" >> ~/to_sort/log.txt

#--- REMOVE CACHE and THUMBS ---
#rm -R /home/evrosvet/.{thumbnails,cache}
