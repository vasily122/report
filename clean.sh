#!/bin/bash
#2015 oct 28 v 1.0
point=sort_$(date +%d_%m_%Y)
library=/home/evrosvet/LIBRARY/
#echo $point

#--- make dirs  for daily sort ----
mkdir ~/to_sort/$point
mkdir ~/to_sort/$point/txt
mkdir ~/to_sort/$point/pics
mkdir ~/to_sort/$point/arch

#--- sort files by type in daily sort dir ---
mv ~/Загрузки/*.jpg ~/to_sort/$point/pics
mv ~/Загрузки/*.jpeg ~/to_sort/$point/pics
mv ~/Загрузки/*.png ~/to_sort/$point/pics
mv ~/Загрузки/*.gif ~/to_sort/$point/pics

mv ~/Загрузки/*.txt ~/to_sort/$point/txt
mv ~/Загрузки/*.pdf ~/to_sort/$point/txt
mv ~/Загрузки/*.PDF ~/to_sort/$point/txt
mv ~/Загрузки/*.djvu ~/to_sort/$point/txt
mv ~/Загрузки/*.odt ~/to_sort/$point/txt

mv ~/Загрузки/*.rar ~/to_sort/$point/arch
mv ~/Загрузки/*.7z ~/to_sort/$point/arch
mv ~/Загрузки/*.arj ~/to_sort/$point/arch
mv ~/Загрузки/*.zip ~/to_sort/$point/arch
mv ~/Загрузки/*.tar ~/to_sort/$point/arch
#mv ~/Загрузки/*.gz ~/to_sort/$point/arch
#mv ~/Загрузки/*.bz2 ~/to_sort/$point/arch
#mv ~/Загрузки/*.deb ~/to_sort/$point/arch

#--- any other not selected ---
mv ~/Загрузки/*.* ~/to_sort/$point

#--- REMOVE CACHE and THUMBS ---
rm -R /home/evrosvet/.thumbnails
rm -R /home/evrosvet/.cache

#--- report ---
touch ~/Рабочий\ стол/cleaned$(date +%d_%m_%Y).txt
