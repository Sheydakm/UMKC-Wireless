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
	#--------------------------------------------------get the tuples of APname and point number from FH_Names.csv-------------------------------------------
	with open("result2.csv") as fh:
		for lf in fh:
			fhList.append(lf)
	for n in fhList:
		new_tuplef= tuple(n.split(';'))
		lisf.append(new_tuplef)
	#print lisf
	#--------------------------------------------------get the list of all lines in result1.csv (we need to addAP names infront of each line)----------------
	with open("AP IP & BaseRadio MAC for FH-HH-RH.csv") as f:
		for line in f:
			myList.append(line)
	for i in myList:
		new_tuple= tuple(i.split(','))
		lis.append(new_tuple)
	#print lis
	#------------------------------compare each tuple list result1.csv with each tuple of FH_Names.csv if the points are equal put APname from FH_Names.csv to APname of FH_Names.csv ----------------
	for j in lisf:
		for k in lis:
			print j[16],"==", k[1].upper()
			#.split("\n")[0]
			#if j[2].split()[0]==k[1].split("\n")[0]:
			if j[16]==k[1].upper():
				#print j[2].split()[0],k[1].split("\n")[0]
				l=list(j)
				l[0]=k[0]
				l[1]=k[3][:-2]
				#print l[0]
				finallist.append(tuple(l))
				print l
				#j[0].append(k[0])
	print finallist
	with open("result3.csv","w")  as f2:
		writer=csv.writer(f2, delimiter=";", lineterminator="\r\n") 
		writer.writerows(finallist)
	#os.remove('result2.csv')

if __name__ == "__main__":
    sys.exit(main())
