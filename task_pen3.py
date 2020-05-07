#!/usr/bin/python
# -*- coding: utf-8 -*- 
# 2020may07

import os

#os.system("""(sync; date ; uptime; ps ax ;cat /etc/issue; cat /var/lib/boinc-client/stderrdae.txt; cat /var/lib/boinc-client/stdoutdae.txt; cat /var/lib/boinc-client/time_stats_log)| mail -s "Pen3 seti errors 2" vasily122@yandex.ru""")
os.system("""(sync; date; cat /var/lib/boinc-client/stdoutdae.txt)| mail -s "Pen3 seti errors 4" vasily122@yandex.ru""")
#os.system("""(date; cat .bash_history)| mail -s "Pen3 history" vasily122@yandex.ru""")

##os.system("""rm index.html""")
##os.system("""lynx --dump opennet.ru""")
##os.system("""mail -s "Pen3 test 0.16 linx" vasily122@yandex.ru < index.html""")

#os.system("""rm index.html""")
#os.system("""wget opennet.ru""")
#os.system("""(cat index.html)|mail -s "Pen3 test 0.16 wget" vasily122@yandex.ru""")

#os.system("""(date;ls) | mail -s "Pen3 test 0.13" vasily122@yandex.ru""")
#os.system("""(cat index.html) | mail -s "Pentium3 news digest" vasily122@yandex.ru""")
#os.system("""rm index.html""")
#os.system("""(sync; date; uptime; ps ax) | mail -s "PentiumIII" vasily122@yandex.ru""")
#os.system("""(sync; date; uptime; ps ax; crontab -l; cat ~/DO/monitor.py; cat ~/task_pen3.py) | mail -s "Pen3 " vasily122@yandex.ru""")
#os.system("""(date;crontab -l;cat ~/DO/monitor.py)| mail -s "pen3" vasily122@yandex.ru""")
#os.system("""wget https://raw.githubusercontent.com/vasily122/report/master/monitor.py""")
#os.system("""ls -la|mail -s "pen3 get monitor" vasily122@yandex.ru""")
#os.system("""(date;python3 --version;uptime)|mail -s "pen3 python versions" vasily122@yandex.ru""")
