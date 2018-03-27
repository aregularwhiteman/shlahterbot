import subprocess#import
import os
import time
from time import sleep
import csv
import sys
import platform
from subprocess import Popen


path2='dump'

def main():

	with open('temp.csv', 'r') as csv_file:
		reader = csv.reader(csv_file)
		thenet = dict(reader)

	bssid=thenet['BSSID']
	channel=thenet['channel']
	essid=thenet['ESSID']
	print(essid,bssid,channel)
	sleep(1)
	bash='sudo airodump-ng --channel '+str(channel)+' --bssid '+str(bssid)+' mon0 --write '+path2
	print(bash)
	sleep(1)
	subprocess.call(bash, shell=True)
	
main()