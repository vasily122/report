#!/bin/bash
#====================================
#Prog starts in time by crontab and cleans download folder
#look ПРАВИЛА
#THIS version moves files directly to library
#Author: vasily122@yandex.ru
#Date: 2016 mar 17
#Version: 2.4
#====================================
library=~/LIBRARY
folder=~/Загрузки
#-- TODO: put in cycle for i in {..} 
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
#--- move all files with tags ---
#-- TODO: if folder doesn`t exist- create it
for i in {arch,book,draw,howto,info_,linux,micro,phys,prog,search,stoks,radio,hack} :
   do mv -S.bak -v $folder/$i* $library/$i/
done
#--- move other files by type
mv -S.bak -v $folder/*.{jpg,JPG,jpeg,JPEG,png,PNG,gif,GIF} $library/pics
mv -S.bak -v $folder/*.{txt,TXT,pdf,PDF,djvu,odt} $library/txt
mv -S.bak -v $folder/*.{rar,RAR,arj,ARJ,zip,ZIP,tar,7z,gz,bz2,tgz,deb} $library/arch
#--- any other type, if not selected ---
mv -S.bak -v $folder/*.*  $library/
#--- report ---
echo -e "cleaned_$(date +%d_%m_%Y)" >> ~/log.txt
