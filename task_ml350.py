#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2018 mar 31
# Version: 0.3.12
#====================================
import os
os.system("""(date;history) | mail -s "HP_ml350 history" vasily122@yandex.ru""")

#os.system("""(sync;date;uptime;cat /sys/class/thermal/thermal_zone*/temp ) | mail -s "HP 350 thermal test2" vasily122@yandex.ru""")
#os.system("""(sync;date;uptime; ps ax) | mail -s "HP_ml350 alive test 1" vasily122@yandex.ru""")
#os.system("""(date;uptime;lshw;inxi -AbD 2>&1) | mail -s "HP_ml350 task" vasily122@yandex.ru""")
#os.system("""(date;sudo dmidecode 2>&1) | mail -s "HP_ml350 task" vasily122@yandex.ru""")
#os.system("""(date ; cat /var/lib/boinc-client/stderrdae.txt; cat /var/lib/boinc-client/stdoutdae.txt; cat /var/lib/boinc-client/time_stats_log)| mail -s "boinc HP_ml350" vasily122@yandex.ru""")
