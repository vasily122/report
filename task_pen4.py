#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 may 7
# Version: 0.3
#====================================
import os
#os.system("""(sync;sync;sync;date;ps ax) | mail -s "Pen4 task" vasily122@yandex.ru""")
os.system("""(sync;sync;sync;date;cat /var/log/messages) | mail -s "Pen4 task" vasily122@yandex.ru""")
