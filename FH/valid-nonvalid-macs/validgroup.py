import sys
import os

def main():
	f2 = open("Valid.log", "w")
	f3 = open("nonValid.log", "w")
	myList = []
	myList1 = []
	new_list = []
	lis = []
	l=[]
	l1=[]
	with open("macsACC.log") as f:
		for line in f:
			item=line.upper().split('\n')[0]
			l.append(item)
	myList=set(l)
	print myList
	print len(myList)
	with open("APmac.log") as f1:
		for line1 in f1:
			item1=line1.split()[0]
			l1.append(item1)
	myList1=set(l1)
	print myList1
	for i in myList:
		for j in myList1:
			if i==j:
				#print i,"VALID"
				lis.append(i)
				f2.write("%s\n" % i)
	print lis
	print len(lis)
	for k in myList:
		if k not in lis:
			new_list.append(k)
	print new_list
	for item2 in new_list:
		f3.write("%s\n" % item2)
	#here find the whole mac

if __name__ == "__main__":
    sys.exit(main())

