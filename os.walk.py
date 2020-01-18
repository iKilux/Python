#! /usr/bin/python3
import os
for folderName, subfolders, filenames in os.walk('/home/kaba/Desktop/python'):
	print('the current folder is '+ folderName)
	
	for subfolder in subfolders:
		print('Subfolder of'+ folderName + ': '+subfolder)
	
	for filename in filenames:
		print('file inside '+ folderName + ': '+ filename)

	print('')