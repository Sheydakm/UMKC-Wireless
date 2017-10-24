import sys
import os
import subprocess
import csv


def main():
	myList = []
	lis=[]
	valid=[]
	d={}
	fhList=[]
	lisf=[]
	finallist=[]
	t=[]
	m=[]
	myList=range(1, 28)
	for k in myList:
		valid.append(str(k))
	with open("fh.csv") as fh:
		for lf in fh:
			fhList.append(lf)
	for n in fhList:
		new_tuplef= tuple(n.split(','))
		lisf.append(new_tuplef)
	for i in lisf:
		new=i[0]
		new_tuple= tuple(new.split(';'))
		lis.append(new_tuple)
	for l in valid:
		for j in lis:
			if j[0]==l:
				tup=(j[0],j[1],j[2]);
				finallist.append(tup)
	m= list(set(finallist))
	with open("latlong.csv","w")  as f2:
		writer=csv.writer(f2, delimiter=",", lineterminator="\r\n") 
		writer.writerows(m)

if __name__ == "__main__":
    sys.exit(main())
