#!/bin/bash
# sort and move files by TAGS to folder ~/LIBRARY
# 2015 nov 18 v2

point=sort_$(date +%d_%m_%Y)
library=/home/evrosvet/LIBRARY/
#ПРАВИЛА
#howto - полезные инструкции и руководства
#stoks -  относится к акциям, рынку, деньгам вцелом
#book -  книги по всем темам - если надо- вводить подразделы
#search - ссылки и темы для дальнейшего поиска
#info -  информационные документы, справочники
#micro - микропроцессоры, контроллеры, ARDUINO,PINGUINO, PIC etc.
#prog - программирование, языки, ноу-хау
#phys - планетология, физика, другие науки
#girl - наборы картинок
#linux - администрирование всех UNIX\Linux\BSD

# Сначала архивы приравняем к текстам и отправим на сортировку по ТЭГАМ
mv -S.bak -v ~/to_sort/$point/arch/*.* ~/to_sort/$point/txt

#-- MV files to permanent /home/evrosvet/LIBRARY/
#-- suffix .bak, -verbose, -update by newer
for i in {howto,stoks,book,search,info,prog,phys,micro,linux} :
   do mv -S.bak -v ~/to_sort/$point/txt/$i* $library/$i/
done
# остатки от сортировки- некатегорированные архивы- в общую папку
mv -S.bak -v ~/to_sort/$point/txt/*.*  $library/
mv -S.bak -v ~/to_sort/$point/pics/*.* $library/pics

