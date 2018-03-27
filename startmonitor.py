import subprocess#import
import os
import time
from time import sleep
import csv


import sys
import platform
from subprocess import Popen



path='/home/vmuser/Desktop/DATA/'
path=path+'monitor'

def main():

	subprocess.getoutput('sudo airmon-ng check kill')
	output=subprocess.getoutput('sudo airmon-ng')
	output=output.split()
	putout=[]
	boo=False
	
	for x in range (len(output)):
		
		if output[x]=='mon0':
			boo=True
			num=x
		
		else:
			putout.append([str(x),output[x]],)

	if boo==True:
		output=subprocess.getoutput('sudo airmon-ng start mon0')
		
	else:
		print('Please select wireless device')
		print('')
	
		for x in range (len(putout)):
			print(putout[x][0],putout[x][1])
		
		print('')
		number=int(input())
		print('')
		device=output[number]
		print('')
		print('Device is ',device)
		print('')
		sleep(3)
		
		if device!='mon0':
			output=subprocess.getoutput('sudo airmon-ng start '+device)
			print('monitor started')
	
	subprocess.call('sudo airodump-ng mon0 --write '+path+' --output-format csv --manufacturer', shell=True)
	

main()