import sys
import os
import subprocess
import csv


def main():
	myList = []
	lisf = []
	lastlist = []
	diction={}
	dictlist = []
	floorlist = []
	APlist = []
	dislist = []
	APnames = []
	APnameslist = []
	pointlist=[]
	finallist=[]
	llist=[]
	with open("distance.csv") as fh:
		for lf in fh:
			myList.append(lf)
	for n in myList:
		new_tuplef= tuple(n.split(';'))
		lisf.append(new_tuplef)
	#print lisf
	for m in lisf:
		APnameslist.append(m[5])
	#print APnameslist,"**********"
	Apnames=list(set(APnameslist))
	#print Apnames
	for k in range(len(Apnames)):
		#print k
		#print Apnames[k]
		for j in lisf:
			if j[5]==Apnames[k]:
					#print Apnames[k]
					#print j[0]
					#print j[3]
					#print j[5]
					#dictionary = {j[5]:[j[3],float(j[0])]}
					t=[j[3],j[5],j[0]]
					finallist.append(t)
		#print finallist
		a=(finallist)
		finallist=[]
		#print finallist
		print a
		for h in a:
			print h[2]
			floorlist.append(h[2])
		print floorlist
		idx=floorlist.index(min(floorlist))
		print idx
		llist.append(a[idx])
		floorlist=[]
	print llist
	with open("min.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(llist)
	#print dictionary
	#print min(dictionary, key=lambda d: d[j[5]][1])
	#				
	#print finallist
	#for f in finallist:
	#	print f
	#		#print pointlist
	#		#print APlist
	#		#print dislist
			
if __name__ == "__main__":
    sys.exit(main())
