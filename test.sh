#!/bin/bash
point=sort_$(date +%d_%m_%Y)
echo $point
#touch ~/Рабочий\ стол/cleaned$(date +%d_%m_%Y).txt
#DISPLAY=:0 gdialog --msgbox "SDELAY PERERYV \!" 25 20 > /dev/null
#rm -R /home/evrosvet/.thumbnails
#rm /home/evrosvet/Рабочий\ стол/cleaned*.txt
# ./test.sh >> ~/Рабочий\ стол/1.txt
#mkdir ~/to_sort/$point
#mv ~/Загрузки/*.* ~/to_sort/sort_$(date +%d_%m_%Y)

#!/bin/bash
for i in {howto,stoks,book,search,info,prog,phys,micro,linux} 
do  mkdir $i ;
done
