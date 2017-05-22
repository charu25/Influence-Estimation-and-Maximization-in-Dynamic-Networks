import csv
import string
from DynamicGraph import DynamicGraph
import random
import numpy
from collections import defaultdict
import time

import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Model ::', str(sys.argv[1])
# print 'Number of edges ::', int(sys.argv[2])

dmg = DynamicGraph()
a_set = set()
exclude = string.punctuation
prob = [0.1,0.01,0.001]

dmg.set_beta(32)
edge_set = defaultdict(int)
degreeMap = defaultdict(int)

num_of_edges = int(sys.argv[2])
model = str(sys.argv[1])

j = 0
with open("enron_data_weight.tsv") as tsvfile:
    next(tsvfile)
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    
    for row in tsvreader:
        if j == num_of_edges:
            break
        vertex = row[0].split()
        edge_set[(int(vertex[0]), int(vertex[1]))] += 1
        degreeMap[int(vertex[1])] +=1
        j+=1


i = 0
time0 = time.time()

for edge in edge_set:
    if edge[0] != edge[1] and i < num_of_edges:
        # print edge
        dmg.addVertex(edge[0])
        dmg.addVertex(edge[1])
        # print edge
        a_set.add(edge[0])
        a_set.add(edge[1])
        if model == "TR":
            dmg.addEdge(edge[0],edge[1],random.choice(prob))
        else :
            dmg.addEdge(edge[0],edge[1],1.0/degreeMap[edge[1]])
    i+=1

print model
print num_of_edges
 # "Time taken for {} nodes is {} for {} model".format(num_of_edges,time.time() - time0, model)
time_taken = time.time() - time0
influences = []
for v in a_set:
    val = dmg.infEst(v)
    if val > 0: 
        # print ("Influence of {} is {}".format(v, val))
        influences.append(val)
print influences
print time_taken

# print dmg.infMax(len(a_set))[-5:]
