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
	dblist = []
	APnames = []
	APnameslist = []
	finallist=[]
	llist=[]
	with open("result3.csv") as fh:
		for lf in fh:
			myList.append(lf)
	for n in myList:
		new_tuplef= tuple(n.split(';'))
		lisf.append(new_tuplef)
	for m in lisf:
		APnameslist.append(m[2])
	print APnameslist,"**********"
	Apnames=list(set(APnameslist))
	print Apnames
	for k in range(len(Apnames)):
		#print k
		#print Apnames[k]
		for j in lisf:
			if j[2]==Apnames[k]:
					#print Apnames[k]
					#print j[0]
					#print j[2]
					#print j[20]
					#APlist.append(j[0])
					#dblist.append(j[20])
					t=[j[0],j[2],j[20]]
					finallist.append(t)
		a=(finallist)
		finallist=[]
		#print APlist
		#print dblist
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
	with open("mindb.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(llist)


	#with open("floordb.csv","w")  as f2:
	#	writer=csv.writer(f2, delimiter=";", lineterminator="\r\n") 
	#	writer.writerows(lastlist)
	#print lastlist

if __name__ == "__main__":
    sys.exit(main())
