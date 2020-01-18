#! /usr/bin/python3
import math

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(X):
	col=[0]*len(X)
	for i in range(len(X)+1):
		for j in range(len(X)):
			col[j]=max(len(X[j][0]),len(X[j][1]),len(X[j][2]),len(X[j][3]))
			print((X[j][i]).rjust(col[j]), end=' ')
		print()
                
printTable(tableData)
