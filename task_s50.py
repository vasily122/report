
#!/usr/bin/python
# -*- coding: utf-8 -*- 
#====================================
# Prog: external uploaded command module 
# Author: vasily122@yandex.ru
# Date: 2016 june 27
# Version: 0.5
#====================================
import os
os.system(""" (sync;date) | mail -s "toshiba s50 task" vasily122@yandex.ru """)
os.system("""(echo "task done"; date)>>monitor.log""")
