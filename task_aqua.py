#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os
os.system("""(sync; date ; uptime; ps ax ; cat /var/lib/boinc-client/stderrdae.txt; cat /var/lib/boinc-client/stdoutdae.txt; cat /var/lib/boinc-client/time_stats_log)| mail -s "boinc aqua" vasily122@yandex.ru""")
#os.system("""(sync; date ; uptime)| mail -s "Depo" vasily122@yandex.ru""")
