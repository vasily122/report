#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import os
#os.system("""(sync; date ; uptime; ps ax ; cat /var/lib/boinc-client/stderrdae.txt; cat /var/lib/boinc-client/stdoutdae.txt; cat /var/lib/boinc-client/time_stats_log)| mail -s "boinc DepoServ" vasily122@yandex.ru""")
#os.system("""(sync; date ; uptime; ps ax)| mail -s "Depo responce" vasily122@yandex.ru""")
os.system("""(date;ping -c1 192.168.10.91;ping -c1 192.168.10.92)| mail -s "Depo responce" vasily122@yandex.ru""")
