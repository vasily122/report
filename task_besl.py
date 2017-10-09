#!/usr/bin/python3
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2017 sep 09
# Version: 0.5.1
#====================================
import os
#os.system("""sync; date >> ~/DO/log.txt """)
#os.system("""(date; df; cat ~/DO/log.txt ) | mail -s " Samsung r530 boot" vasily122@yandex.ru""")
#os.system("""(date; df) | mail -s " Samsung r530 task" vasily122@yandex.ru""")
os.system("""(date; crontab -l; ls -la; cat ~/DO/monitor.py; cat ~/DO/report.py) | mail -s "Samsung R530 is online" vasily122@yandex.ru""")
