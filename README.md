# report
Main purpose of this project is to research and develop
monitoring scripts for some servers, that run BOINC or
for maintain old notebook of my parents

They use Xubuntu 16.04 LTS + 4G-modem for Skype.
(Also tested on servers with Ubuntu 18.04, Debian 8,9)

3G/4G usually has dynamic IP address during connecting
and communications have single direction via e-mail only.
NOTE: some mail servers use protection from spam
and mails from new sources drop to trash folder. 
Check your emails, moved to spam folder 

PREPARATIONS:
sudo apt-get install exim4 mailutils
sudo dpkg-reconfigure exim4-config   # config to email from internet site
mkdir ~/DO
cp /...your folder.../{report,monitor}.py ~/DO/
chmod u+x ~/DO/*.py

crontab -e
ADD (mobile network):
      @reboot  python3 /home/...username..../DO/report.py
OR (automatic network):
      @reboot  python3 /home/...username..../DO/monitor.py
      
MONITORING:
1.report.py - start script for mobile or manual network connection
installed in /home/..full..path.../ -your scripts folder
It starts on @reboot in crontab, needs no change (may depend on ping version)

If network exists - call next additional file monitor.py  
if not- do sleep cycle until network appears. 
That is why because mobile 3G/4G connection starts in 2-3-5 min or manually
if network is automatic, we dont need file report.py

USAGE:
    crontab -e
    ADD:
      @reboot  python3 /home/..full..path.../report.py
 
2.monitor.py - main monitoring script to download command file, specific to host,
make it executable and start from report.py, by crontab or manually
if network is automatic, we dont need file report.py

USAGE:
    crontab -e
    ADD:
     (once on reboot)
     @reboot  python /home/...path.../monitor.py
     or
     0 * * * * python /home/...path.../monitor.py
     (hourly)

In file monitor.py string 'filename' sets according to the hostname:
task_{host}.py
which will download and execute
  
3.task_{host}.py-command file specific to host
If necessary I put additional commands to file task_{host}.py in repository "report"
to get additional reports by mail (different commans for different hosts)
or left it empty
