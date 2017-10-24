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
	with open("FH_Names.csv") as fh:
		for lf in fh:
			fhList.append(lf)
	for n in fhList:
		new_tuplef= tuple(n.split(','))
		lisf.append(new_tuplef)
	#print lisf
	#--------------------------------------------------get the list of all lines in result1.csv (we need to addAP names infront of each line)----------------
	with open("result1.csv") as f:
		for line in f:
			myList.append(line)
	for i in myList:
		new_tuple= tuple(i.split(';'))
		lis.append(new_tuple)
	print lis
	#------------------------------compare each tuple list result1.csv with each tuple of FH_Names.csv if the points are equal put APname from FH_Names.csv to APname of FH_Names.csv ----------------
	for j in lis:
		for k in lisf:
			#print j[2].split()[0],k[1].split("\n")[0]
			if j[2].split()[0]==k[1].split("\n")[0]:
				#print j[2].split()[0],k[1].split("\n")[0]
				l=list(j)
				l[0]=k[0]
				#print l[0]
				finallist.append(tuple(l))
				#j[0].append(k[0])
	print finallist
	with open("result2.csv","w")  as f2:
		writer=csv.writer(f2, delimiter=";", lineterminator="\r\n") 
		writer.writerows(finallist)
	#os.remove('result.csv')
	#os.remove('result1.csv')
	#print lis
	#for j in lis:
	#	for k in valid:
	#		if j[14]==k.upper():
	#			#print j[2]
	#			d[j[14]] = j[2].split()[0]
	#			print j[0]
	#print d
	#print lisf
	#for key in d:
	#	for t in lisf:
	#		if d[key]==t[1].split('\n')[0]:
	#			print t[0]

if __name__ == "__main__":
    sys.exit(main())
