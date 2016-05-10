#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 may 7
# Version: 0.3
#====================================
import os
os.system("""(date;uptime;inxi -Abo) | mail -s "s5000 task" vasily122@yandex.ru""")
