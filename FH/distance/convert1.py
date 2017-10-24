import sys
import os
import subprocess
import csv
import math

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
	R = 3959 # Radius of the earth in km
	with open("output.csv") as fh:
		for lf in fh:
			fhList.append(lf)
	for n in fhList:
		new_tuplef= tuple(n.split(';'))
		lisf.append(new_tuplef)
	#print lisf
	print "----------------------------------------------------"
	for i in lisf:
		print i
		print i[0]
		lat1=float(i[1])
		lon1=float(i[2])
		lat2=float(i[8])
		lon2=float(i[9])
		print lat1,lon1,lat2,lon2
		dLat = deg2rad(lat2-lat1) # deg2rad below
		dLon = deg2rad(lon2-lon1)
		a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2) 
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
		d = R * c # Distance in mile
		k=list(i)
		k[0]=d
		print d
		finallist.append(tuple(k))
	#print finallist
	with open("distance.csv","w")  as f2:
		writer=csv.writer(f2, delimiter=";", lineterminator="\r\n") 
		writer.writerows(finallist)


def deg2rad(deg):
    return deg * (math.pi/180)

if __name__ == "__main__":
    sys.exit(main())
#deg2rad
