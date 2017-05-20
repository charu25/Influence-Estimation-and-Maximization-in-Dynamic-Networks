import csv
import string
from DynamicGraph import DynamicGraph
import random
import numpy
from collections import defaultdict
dmg = DynamicGraph()
a_set = set()
exclude = string.punctuation
prob = [0.1,0.01,0.001]

edge_set = defaultdict(int)
with open("out.enron") as tsvfile:
    next(tsvfile)
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for row in tsvreader:
        vertex = row[0].split()
        edge_set[(int(vertex[0]), int(vertex[1]))] += 1

for edge in edge_set:
    if edge[0] not in a_set:
        dmg.addVertex(edge[0])
        a_set.add(edge[0])
    if edge[1] not in a_set:
        dmg.addVertex(edge[1])
        a_set.add(edge[1])

    dmg.addEdge(edge[0],edge[1],0.1)#random.choice(prob))


#with open("out.enron") as tsvfile:
#    next(tsvfile)
#    tsvreader = csv.reader(tsvfile, delimiter="\t")
#    for row in tsvreader:
#        #print row
#        vertex = row[0].split()
#        #print vertex
#        sour = int(vertex[0])
#        dest = int(vertex[1])
#        print sour, dest
#        if sour not in a_set:
#            dmg.addVertex(sour)
#            a_set.add(sour)
#        if dest not in a_set: 
#            dmg.addVertex(dest)
#            a_set.add(dest)
#        dmg.addEdge(sour,dest,0.1)#random.choice(prob))
#print a_set

for v in a_set:
    if dmg.infEst(v) > 0:
        print ("Influence of {} is {}".format(v, dmg.infEst(v)))

print ("Most influential vertex is {}".format(dmg.infMax(4)[-1]))
