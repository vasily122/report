#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
#os.system("""(sync; date ; uptime; ps ax ; cat /var/lib/boinc-client/stderrdae.txt; cat /var/lib/boinc-client/stdoutdae.txt; cat /var/lib/boinc-client/time_stats_log)| mail -s "boinc DepoServ" vasily122@yandex.ru""")
#os.system("""(sync; date; uptime; ps ax; crontab -l; cat ~/DO/monitor.py; cat ~/task_depo.py)| mail -s "Depo" vasily122@yandex.ru""")
os.system("""(date;ping -c3 192.168.10.90;ping -c3 192.168.10.94)| mail -s "Depo responce" vasily122@yandex.ru""")
#os.system("""wget https://raw.githubusercontent.com/vasily122/report/master/monitor.py""")
#os.system("""ls -la|mail -s "depo get monitor" vasily122@yandex.ru""")
