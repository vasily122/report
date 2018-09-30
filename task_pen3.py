#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import os
#os.system("""(sync;date;uptime;ps ax) | mail -s "Pen3 responce " vasily122@yandex.ru""")
os.system("""(date;crontab -l;cat ~/DO/monitor.py)| mail -s "pen3" vasily122@yandex.ru""")
