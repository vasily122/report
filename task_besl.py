#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2017 may 20
# Version: 0.4
#====================================
import os
os.system("""sync; date >> ~/DO/log.txt """)
os.system("""(date; df) | mail -s " Mama samsung r530 task" vasily122@yandex.ru""")
