#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 may 7
# Version: 0.3
#====================================
import os
os.system("""(sync;uptime;date;ps ax) | mail -s "deposerv task" vasily122@yandex.ru""")

#os.system("""(date;uptime;lshw;inxi -AbD 2>&1) | mail -s "s5000 task" vasily122@yandex.ru""")
#os.system("""(date;sudo dmidecode 2>&1) | mail -s "s5000 task" vasily122@yandex.ru""")
#os.system("""(sync;date ;ps ax; cat /var/lib/boinc-client/stderrdae.txt; cat /var/lib/boinc-client/stdoutdae.txt; cat /var/lib/boinc-client/time_stats_log)| mail -s "boinc deposerv" vasily122@yandex.ru""")
#os.system("""(sync date ; ps ax ; cat /var/lib/boinc-client/stdoutdae.txt)| mail -s "boinc deposerv" vasily122@yandex.ru""")

