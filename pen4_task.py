#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 may 7
# Version: 0.3
#====================================
import os
#os.system("""(date ; cat /var/lib/boinc-client/stderrdae.txt cat /var/lib/boinc-client/stdoutdae.txt; cat /var/lib/boinc-client/time_stats_log)| mail -s "Activity report" vasily122@yandex.ru""")
#os.system("""(date ; tail /var/lib/boinc-client/stderrdae.txt; tail /var/lib/boinc-client/stdoutdae.txt; tail /var/lib/boinc-client/time_stats_log)| mail -s "Activity report" vasily122@yandex.ru""")
#os.system("""(date ; tail /var/lib/boinc-client/stderrdae.txt; report-hw)| mail -s "system data" vasily122@yandex.ru""")
#os.system("""(date; uptime)>>log.txt""")
os.system("""date;uptime;df" | mail -s "Pen4 task" vasily122@yandex.ru""")
