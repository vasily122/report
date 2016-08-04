#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 july 28
# Version: 0.4
#====================================
import os
os.system("""sync; date >> ~/DO/log.txt """)
os.system("""(date; ifconfig; df) | mail -s "samsung r530 task" vasily122@yandex.ru""")
