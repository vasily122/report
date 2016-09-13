#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 may 7
# Version: 0.3
#====================================
import os
#os.system("""(date;uptime;lshw;inxi -AbD 2>&1) | mail -s "s5000 task" vasily122@yandex.ru""")
#os.system("""(date;sudo dmidecode 2>&1) | mail -s "s5000 task" vasily122@yandex.ru""")
#os.system("""(date;uptime) | mail -s "s5000 task" vasily122@yandex.ru""")
os.system("""(date;  ls -la /var/lib/boinc-client/) | mail -s "s5000 ls /var/lib/boinc-client/" vasily122@yandex.ru""")
os.system("""(date;cat /var/lib/boinc-client/stderrdae.txt) | mail -s "s5000 stderrdae.txt" vasily122@yandex.ru""")
os.system("""(date; cat /var/lib/boinc-client/stdoutdae.txt) | mail -s "s5000 stdoutdae.txt" vasily122@yandex.ru""")
os.system("""(date;  cat /var/lib/boinc-client/time_stats_log) | mail -s "s5000 time_stats_log" vasily122@yandex.ru""")
