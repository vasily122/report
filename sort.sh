#!/bin/bash
#====================================
#Prog starts by crontab AFTER clean.sh
#sort and move files by TAGS to folder ~/LIBRARY
#Autor: vasily122@yandex.ru
#Date: 2016 jan 26
#Version: 2.4
#====================================
point=sort_$(date +%d_%m_%Y)
library=~/LIBRARY
#ПРАВИЛА
# Сначала архивы приравняем к текстам и отправим на сортировку по ТЭГАМ
#-- suffix .bak, -verbose, -update by newer
mv -S.bak -v ~/to_sort/$point/arch/*.* ~/to_sort/$point/txt
# -- {..} taken from skel.sh
for i in {arch,book,draw,howto,info,linux,micro,phys,prog,search,stoks,radio,hack} :
   do mv -S.bak -v ~/to_sort/$point/txt/$i* $library/$i/
done
# остатки от сортировки- в общую папку
mv -S.bak -v ~/to_sort/$point/txt/*.*  $library/
mv -S.bak -v ~/to_sort/$point/pics/*.* $library/pics
#некатегорированные архивы- в общую папку
mv -S.bak -v ~/to_sort/$point/*.* $library/
#--- report ---
echo -e "sorted_$(date +%d_%m_%Y) \n" >> ~/to_sort/log.txt
