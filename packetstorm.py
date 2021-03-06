#!/usr/bin/env python
import requests
import os
import sys
import datetime
import argparse
import tarfile
import progressbar
from termcolor import colored, cprint

#TODO needs a prgressbar for each download
#TODO needs more color to tell the user whats going on
#TODO needs to loop through years from 1999 to find yearly exploits
#TODO need to loop through months to download montly archives

def get_yearly_exploits(header):
    try:
       #Grab current time and date
       now = datetime.datetime.now()
       #url to get yearly exploits from
       url = r'http://dl.packetstormsecurity.net/' + now.strftime("%y") + '12-exploits/' + now.strftime("%Y") + '-exploits.tgz'
       print url
       #build the request, with the proper user-agent in the custom header
       r = requests.get(url, headers=header, timeout=30)
       totalsize=r.headers['content-length']
       if int(totalsize) <= 500:
          cprint("Fail Whale", "red")
    except requests.exceptions.RequestException, e:
       cprint("An Error has occured: %s" %str(e), 'red', attrs=["bold"])

def get_monthly_exploits(headers):
    date = datetime.datetime.now()
    months = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
    for month in months:
        print month
        

#def search_exploits(search):
    

def main():
   parser = argparse.ArgumentParser(description="Dowloads and searchs packetsorm exploits archives")
   parser.add_argument('-s', '--search', type=str, help="Please provide a search string. E.G. cisco")
   parser.add_argument('-v', '--version', type=str, help="Provides version information about script")
   args = parser.parse_args()
   dir='/usr/share/exploits/packetstorm'

   if os.getuid() != 0:
      cprint("This script requires root privledges!", 'red', attrs=['bold'])
      sys.exit(1)
   else:
      pass

   if not os.path.exists(dir):
      cprint("%s does not exists. Creating..." %str(dir), 'blue', attrs=['bold'])
      os.makedirs(dir)
      cprint("%s directory created, all downloads will be dumped here." %str(dir), 'blue', attrs['bold'])
      cprint("all downloads will be placed in %s." %str(dir), 'blue', attrs=['bold'])

   #set the user-agent to the one specified for kernel.com
   header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0',}
   
   get_yearly_exploits(header)
  

if __name__ == '__main__':
     main()  
