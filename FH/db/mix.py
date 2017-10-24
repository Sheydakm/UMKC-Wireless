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
	fhList1=[]
	lisf=[]
	lisf1=[]
	finallist=[]
	my_tuple = ()
	with open("last.csv") as fh1:
		for lf1 in fh1:
			fhList1.append(lf1)
	for n1 in fhList1:
		new_tuplef1= tuple(n1.split(','))
		lisf1.append(new_tuplef1)
	#print lisf1
	#print len(lisf1)
	with open("mindb.csv") as fh:
		for lf in fh:
			fhList.append(lf)
	for n in fhList:
		new_tuplef= tuple(n.split(','))
		lisf.append(new_tuplef)
	#print lisf
	#print len(lisf)
	for j in lisf1:
		for k in lisf:
			if j[0]==k[1].split()[0]:
				print "YES"
				print j[0]
				print k[1].split()[0]
				m=k[1].split("\r\n")
				print "***************",m[0],"*****************"
				n=j[3].split("\r\n")
				print "***************",n[0],"*****************"
				o=k[2].split("\r\n")
				print "***************",o[0],"*****************"
				my_tuple = (j[0],k[0],o[0],j[1],j[2],n[0])
				#print my_tuple
				myList.append(my_tuple)
				#myList.append(j[1])
				#myList.append(k[1])
			#print myList
	with open("db.csv","w")  as f2:
		writer=csv.writer(f2, delimiter=",", lineterminator="\r\n") 
		writer.writerows(myList)
if __name__ == "__main__":
    sys.exit(main())
