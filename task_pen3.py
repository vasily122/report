#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2018 mar 21
# Version: 0.3.2
#====================================
import os
os.system("""(sync;date;uptime;ps ax ) | mail -s "Pen III alive test 1" vasily122@yandex.ru""")
#os.system("""(sync;date;uptime;cat /sys/class/thermal/thermal_zone*/temp) | mail -s "Pen III thermal test" vasily122@yandex.ru""")
#os.system("""(date;ls /sys/class/) | mail -s "=== III  vasily122@yandex.ru""")
#os.system("""(sync;date;uptime;ls -R /sys/class/;uptime;ls -R -la /sys/class/ ) | mail -s "Pen III thermal test1" vasily122@yandex.ru""")
