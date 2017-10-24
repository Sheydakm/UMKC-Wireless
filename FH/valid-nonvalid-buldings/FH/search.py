import sys
import os
import subprocess
import csv


def main():
	myList = []
	lis=[]
	valid=[]
	with open("output1.csv") as f:
		for line in f:
			myList.append(line)
			#myList=[x for x in line.split('\r') if x]
	print "----------------------------------------------------"
	print myList
	for i in myList:
		new_tuple= tuple(i.split(';'))
		#print new_tuple[:-1]
		lis.append(new_tuple[:-1])
	#print lis
	with open("finalvalid.log") as f1:
		for line1 in f1:
			valid.append(line1.split()[0])
	print "----------------------------------------------------"
	print valid
	for j in lis:
		count=0
		for k in valid:
			#print j
			#print lis.index(j)
			if j[0]!='v':
				#print j[13], "?" ,k
				if j[13]==k:
					indx=lis.index(j)
					l=list(j)
					l[0]='v'
					j=tuple(l)
					lis[indx]=j
	print "----------------------------------------------------"
	print lis
	#directory = os.path.dirname('result')
	with open('result.csv',"w")  as f2:
		writer=csv.writer(f2, delimiter=";", lineterminator="\r\n") 
		writer.writerows(lis)
	os.remove('output.csv')
	os.remove('output1.csv')
	#os.remove('unique.log')


if __name__ == "__main__":
    sys.exit(main())

















