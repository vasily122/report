#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2018 mar 21
# Version: 0.3.1
#====================================
import os
os.system("""(sync;date;uptime;ps ax) | mail -s "Pen4 alive test 1 " vasily122@yandex.ru""")
