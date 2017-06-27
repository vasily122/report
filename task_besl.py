#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2017 june 27
# Version: 0.5
#====================================
import os
#os.system("""sync; date >> ~/DO/log.txt """)
#os.system("""(date; df; cat ~/DO/log.txt ) | mail -s " Samsung r530 boot" vasily122@yandex.ru""")
os.system("""(date; df) | mail -s " Samsung r530 boot" vasily122@yandex.ru""")
