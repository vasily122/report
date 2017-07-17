#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2017 july 04
# Version: 0.3.1
#====================================
import os
os.system("""(sync;date;uptime) | mail -s "Pen III hot test" vasily122@yandex.ru""")
