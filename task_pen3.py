#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import os
#os.system("""(sync;date;uptime;ps ax) | mail -s "Pen3 responce " vasily122@yandex.ru""")
os.system("""(date;ping -c1 192.168.10.91;ping -c1 192.168.10.92)| mail -s "pen3 probe" vasily122@yandex.ru""")
