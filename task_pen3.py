#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2017 july 04
# Version: 0.3.1
#====================================
import os
#os.system("""(sync;date;uptime;cat /sys/class/thermal/thermal_zone*/temp) | mail -s "Pen III thermal test" vasily122@yandex.ru""")
#os.system("""(date;ls /sys/class/) | mail -s "=== III  vasily122@yandex.ru""")
os.system("""(sync;date;uptime;ls /sys) | mail -s "Pen III thermal test" vasily122@yandex.ru""")
