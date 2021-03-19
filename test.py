#!/bin/python
import os
import sys
import json

top = []
def CompareAdd(share, inp):
	inserted = 0
	#print ("before insert")
	#for i in range(len(top)):
	#	print ("%d Material: %s    Planet: %s" % (i, str(top[i]["share"]), top[i]["planet"]["name"]))
	for i in range(len(top)):
		x = top[i]
		if x["share"] < share:
			top.insert(i, {"share": share, "planet": inp})
			inserted = 1
			break
	
	if inserted == 0 and len (top) < 10:
		top.insert(len (top), {"share": share, "planet": inp})
	if inserted == 1 and len (top) > 10:
		del top[10]

	#print ("after insert")
	#for i in range(len(top)):
	#	print ("%d Material: %s    Planet: %s" % (i, str(top[i]["share"]), top[i]["planet"]["name"]))
	#print ("leave comapre \n\n\n")
	

#if (x["share"] < share)
			
if len(sys.argv) < 3:
	print ("Usage: ./%s <filename> <material_name" % sys.argv[0])

with open (sys.argv[1], 'r') as f:
	index = 0
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		if len(line) < 5:
			continue;

		x = json.loads(line)
		#print(json.dumps(x, indent=4))
		for i in x["materials"]:
			if i["material_name"] == sys.argv[2] and i["share"] != None:
				#print("Material: %s    Planet: %s\n" % (i["share"], x["name"]))
				CompareAdd(float(i["share"]), x)
		if index % 1000000 == 0:
			print (index / 1000000)
			print ("Million")
			print ("TOP 10 %s" % sys.argv[2])
			for i in range(len(top)):
				print ("%d Material: %s    Planet: %s" % (i, str(top[i]["share"]), top[i]["planet"]["name"]))
			print ("\n\n\n\n")
		index += 1

	print ("TOP 10 %s" % sys.argv[2])
	for i in range(len(top)):
		print ("%d Material: %s    Planet: %s" % (i, str(top[i]["share"]), top[i]["planet"]["name"]))

