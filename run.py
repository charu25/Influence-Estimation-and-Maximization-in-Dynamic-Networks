#!/usr/bin/python
import os
edges = [10,50,100,150,500,1000,10000]
models = ["TR","WC"]
for edge in edges:
	for model in models:
		print "Edges :: {}, Model :: {}".format(edge,model)
		os.system("python enron.py " +  str(model) + " " + str(edge) + " >> op.txt" )  
