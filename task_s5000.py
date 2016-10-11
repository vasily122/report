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
os.system("""(sync;date;uptime) | mail -s "s5000 task" vasily122@yandex.ru""")

#os.system("""(date;  ls -la /var/lib/boinc-client/) | mail -s "s5000 ls /var/lib/boinc-client/" vasily122@yandex.ru""")
#os.system("""tar -cvf b2.tar /var/lib/boinc-client/ ;  (date; uptime) | mutt -s " S5000 boinc dir" vasily122@yandex.ru -a b2.tar""")
#os.system(""" rm b2.tar""")

#os.system("""(date;  ls -la /var/lib/boinc-client/projects) | mail -s "s5000 ls /var/lib/boinc-client/projects" vasily122@yandex.ru""")
#os.system("""(date;  ls -la /var/lib/boinc-client/slots) | mail -s "s5000 ls /var/lib/boinc-client/slots" vasily122@yandex.ru""")

#os.system("""(date;  cat /var/lib/boinc-client/statistics_boinc.bakerlab.org_rosetta.xml) | mail -s "s5000 statis" vasily122@yandex.ru""")

#os.system("""(date;  mutt -v) | mail -s "s5000 mutt" vasily122@yandex.ru""")

#os.system("""(date;cat /var/lib/boinc-client/stderrdae.txt) | mail -s "s5000 stderrdae.txt" vasily122@yandex.ru""")
#os.system("""(date; cat /var/lib/boinc-client/stdoutdae.txt) | mail -s "s5000 stdoutdae.txt" vasily122@yandex.ru""")
#os.system("""(date;  cat /var/lib/boinc-client/time_stats_log) | mail -s "s5000 time_stats_log" vasily122@yandex.ru""")
