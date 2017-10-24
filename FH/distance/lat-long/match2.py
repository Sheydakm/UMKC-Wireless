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
	lisf1=[]
	finallist=[]
	t=[]
	m=[]
	with open("result3.csv") as fh:
		for lf in fh:
			fhList.append(lf)
	for n in fhList:
		new_tuplef= tuple(n.split(';'))
		lisf.append(new_tuplef)
	print lisf
	print "----------------------------------------------------"
	with open("latlong.csv") as f1:
		for line1 in f1:
			valid.append(line1)
	print valid
	for l in valid:
		new_tuplef1= tuple(l.split(','))
		lisf1.append(new_tuplef1)
	print lisf1
	for i in lisf:
		for j in lisf1:
			if i[2].split()[0]==j[3].split()[0]:
				k=list(i)
				k[0]=j[1]
				k[1]=j[2]
				finallist.append(tuple(k))
	print finallist
	with open("extra.csv","w")  as f2:
		writer=csv.writer(f2, delimiter=";", lineterminator="\r\n") 
		writer.writerows(finallist)


if __name__ == "__main__":
    sys.exit(main())

