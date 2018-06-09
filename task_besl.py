#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2018 june 09
# Version: 0.5.3
#====================================
import os
os.system("""(date; df; tail ~/monitor.log) | mail -s "Samsung_R530 is online" vasily122@yandex.ru""")
