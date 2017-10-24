import sys
import os
import subprocess
import csv
from collections import defaultdict


def main():
	count=0
	myList = []
	lisf = []
	lastlist = []
	diction1={}
	diction2={}
	diction3={}
	dictlist = []
	floorlist = []
	APlist = []
	BWlist = []
	APnames = []
	APnameslist = []
	list1=[]
	list2=[]
	list3=[]
	listlist=[]
	with open("data.csv") as fh:
		for lf in fh:
			myList.append(lf)
	for n in myList:
		new_tuplef= tuple(n.split(','))
		lisf.append(new_tuplef)
	for j in lisf:
		#print j[3]
		if j[3]=='http://www.networkrouting.net/misc/IMG_1838.jpg':
			list1.append(j)
		if j[3]=='http://d.web.umkc.edu/dmedhi/misc/IMG_1838.jpg':
			list2.append(j)
		if j[3]=='http://d.web.umkc.edu/dmedhi/misc/cc76-nov2016-DSC_0658.jpg.zip':
			list3.append(j)
	listlist=[list1,list2,list3]
	for m in lisf:
		APnameslist.append(m[0])
	Apnames=list(set(APnameslist))
	#print Apnames
	for f in range(len(listlist)):
		for k in range(len(Apnames)):
			for j in listlist[f]:
				if j[0]==Apnames[k]:
						#print j[0]
						#print j[8]
						#floorlist.append(j[0])
						BWlist.append(float(j[13]))
			#print BWlist
			ave=sum(BWlist) / len(BWlist)
			print "*********",ave,"********"
			BWlist[:] = []
			if listlist[f]==list1:
				diction1[Apnames[k]]=ave
			if listlist[f]==list2:
				diction2[Apnames[k]]=ave
			else:
				diction3[Apnames[k]]=ave
	print diction1,"******************************************"
	print diction2,"***********"
	print diction3,"***********"
	c = dict([(l,(diction1[l],diction2[l],diction3[l])) for l in diction1])
	print c
	#with open('last.csv', 'wb') as csv_file:
	#	writer = csv.writer(csv_file)
    	#	for key, value in c.items():
       	#		writer.writerow([key, value])
	with open("last.csv", "wb") as f:
		csv.writer(f).writerows((l,) + v for l, v in c.iteritems())


if __name__ == "__main__":
    sys.exit(main())
