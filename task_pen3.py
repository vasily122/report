#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2017 july 04
# Version: 0.3.1
#====================================
import os
os.system("""(sync;date;uptime;ls /sys/class/thermal/) | mail -s "Pen III thermal test" vasily122@yandex.ru""")
