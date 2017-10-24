import sys
import os
import subprocess
import csv

def main():
	myList = []
	myList1 = []
	lisf = []
	lisf1 = []
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
	with open("work.csv") as fh:
		for lf in fh:
			myList.append(lf)
	for n in myList:
		new_tuplef= tuple(n.split(','))
		lisf.append(new_tuplef)
	print lisf
	with open("latlong.csv") as fh1:
		for lf1 in fh1:
			myList1.append(lf1)
	for m in myList1:
		new_tuplef1= tuple(m.split(','))
		lisf1.append(new_tuplef1)
	print lisf1
	for j in lisf:
		for i in lisf1:
			r1=i[3].split("\n")[0]
			r2=j[3].split("\n")[0]
			if r1[0]==" ":
				r1 = r1.split()[0]
			if r1==r2:
				t = (j[0],j[1],j[2],r1,i[1],i[2])
				finallist.append(t)
	print finallist
	with open("pointAP.csv","w")  as f2:
		writer=csv.writer(f2, delimiter=",", lineterminator="\r\n") 
		writer.writerows(finallist)
if __name__ == "__main__":
    sys.exit(main())
