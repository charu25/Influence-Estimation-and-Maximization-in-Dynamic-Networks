import csv
import string
from DynamicGraph import DynamicGraph
import random
import numpy
from collections import defaultdict
import time
dmg = DynamicGraph()
a_set = set()
exclude = string.punctuation
prob = [0.1,0.01,0.001]

dmg.set_beta(32)
edge_set = defaultdict(int)
j = 0
with open("enron/out.enron") as tsvfile:
    next(tsvfile)
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    
    for row in tsvreader:
        if j == 100:
            break
        vertex = row[0].split()
        edge_set[(int(vertex[0]), int(vertex[1]))] += 1
        j+=1
i = 0
time0 = time.time()
for edge in edge_set:
    if edge[0] != edge[1] and i < 100:
        # print edge
        dmg.addVertex(edge[0])
        dmg.addVertex(edge[1])
        print edge
        a_set.add(edge[0])
        a_set.add(edge[1])
        dmg.addEdge(edge[0],edge[1],random.choice(prob))
    i+=1
        # if edge[0] not in a_set:
        #     dmg.addVertex(edge[0])
        #     a_set.add(edge[0])
        # if edge[1] not in a_set:
        #     dmg.addVertex(edge[1])
        #     a_set.add(edge[1])

        #random.choice(prob))


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

# print len(a_set)
for v in a_set:
    val = dmg.infEst(v)
    if val > 0: 
        print ("Influence of {} is {}".format(v, val))
print dmg.infMax(len(a_set))[-5:]
