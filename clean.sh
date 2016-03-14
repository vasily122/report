#!/bin/bash
#====================================
#Prog starts in time by crontab and cleans download folder
#look ПРАВИЛА
#after clean.sh crontab lunchs sort.sh
#Author: vasily122@yandex.ru
#Date: 2016 mar 14
#Version: 2.2
#THIS version moves files directly to library
#====================================
point=~/to_sort/sort_$(date +%d_%m_%Y)
library=~/LIBRARY
folder=~/Загрузки

#--- make dirs  for daily sort ===DO NOT NEED, comment after testing ----
mkdir $point
mkdir $point/{txt,pics,arch}

#-- TO DO: put in cycle for i in {..} 
#{"s/\s+/-/g","s/\,/-/g", "s/\)/-/g", "s/\(/-/g", "s/_-_/-/g","s/\:/-/g", "s/\;/-/g", "s/\~/-/g", "s/--/-/g", "s/__/-/g"}

#for i in  s/\s+/-/g  s/\ /-/g  s/\)/-/g  s/\(/-/g  s/_-_/-/g  s/\:/-/g  s/\;/-/g  s/\~/-/g  s/--/-/g  s/__/-/g  :
#   do echo $i
#done
#--- пока не получается---

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

# -- {..} taken from skel.sh
# --- the new concept- all the files with tags are sorting by first step 
for i in {arch,book,draw,howto,info_,linux,micro,phys,prog,search,stoks,radio,hack} :
   do mv -S.bak -v $folder/$i* $library/$i/
done

#--- sort files by type in daily sort dir ---
#mv $folder/*.{jpg,JPG,jpeg,JPEG,png,PNG,gif,GIF} $point/pics
#mv $folder/*.{txt,TXT,pdf,PDF,djvu,odt} $point/txt
#mv $folder/*.{rar,RAR,arj,ARJ,zip,ZIP,tar,7z,gz,bz2,tgz,deb} $point/arch
#--- move files with tags ---
mv -S.bak -v $folder/*.{jpg,JPG,jpeg,JPEG,png,PNG,gif,GIF} $library/pics
mv -S.bak -v $folder/*.{txt,TXT,pdf,PDF,djvu,odt} $library/txt
mv -S.bak -v $folder/*.{rar,RAR,arj,ARJ,zip,ZIP,tar,7z,gz,bz2,tgz,deb} $library/arch

#--- any other not selected ---
#mv $folder/*.* $point
mv -S.bak -v $folder/*.*  $library/

#--- report ---
#echo -e "cleaned_$(date +%d_%m_%Y)" >> ~/to_sort/log.txt
echo -e "cleaned_$(date +%d_%m_%Y)" >> ~/log.txt

#--- REMOVE CACHE and THUMBS ---
#rm -R /home/evrosvet/.{thumbnails,cache}
