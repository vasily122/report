#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 jan 19
# Version: 0.3
#====================================
import os
os.system("""(date ; cat /var/lib/boinc-client/stderrdae.txt cat /var/lib/boinc-client/stdoutdae.txt; cat /var/lib/boinc-client/time_stats_log)| mail -s "Activity report" vasily122@yandex.ru""")
