#!/bin/bash
point=sort_$(date +%d_%m_%Y)
library=/home/evrosvet/LIBRARY/
#echo $point

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

# архивы приравняем к текстам и отправим на сортировку
mv -S.bak -v ~/to_sort/$point/arch/*.* ~/to_sort/$point/txt
#
#-- MV files to permanent /home/evrosvet/LIBRARY/
#-- suffix .bak, -verbose, -update by newer

mv -S.bak -v ~/to_sort/$point/txt/howto*.*  $library/howto
mv -S.bak -v ~/to_sort/$point/txt/stoks*.*  $library/stoks
mv -S.bak -v ~/to_sort/$point/txt/book*.*  $library/txt
mv -S.bak -v ~/to_sort/$point/txt/search*.*  $library/search
mv -S.bak -v ~/to_sort/$point/txt/info*.*  $library/
mv -S.bak -v ~/to_sort/$point/txt/prog*.*  $library/prog
mv -S.bak -v ~/to_sort/$point/txt/phys*.*  $library/phys
mv -S.bak -v ~/to_sort/$point/txt/micro*.*  $library/micro
mv -S.bak -v ~/to_sort/$point/txt/linux*.*  $library/linux

# остатки от сортировки- некатегорированные архивы- в общую папку
mv -S.bak -v ~/to_sort/$point/txt/*.*  $library/

mv -S.bak -v ~/to_sort/$point/pics/*.* $library/pics
mv -S.bak -v ~/to_sort/$point/txt/girl*.*  $library/pics
#mv -S.bak -v ~/to_sort/$point/arch/*.* $library/arch
