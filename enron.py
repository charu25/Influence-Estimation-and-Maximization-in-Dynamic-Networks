import csv
import time
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
start_time = time.time()



dmg.set_beta(32)
edge_set = defaultdict(int)
degreeMap = defaultdict(int)

num_of_edges = int(sys.argv[2])
is_naive = int(sys.argv[3])
model = str(sys.argv[1])

j = 0
with open("enron_data_weight.tsv") as tsvfile:
    next(tsvfile)
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    
    for row in tsvreader:
        if j == num_of_edges + 100:
            break
        vertex = row[0].split()
        edge_set[(int(vertex[0]), int(vertex[1]))] += 1
        degreeMap[int(vertex[1])] +=1
        j+=1


i = 0
time0 = time.time()

i=0
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

# print model
print num_of_edges
 # "Time taken for {} nodes is {} for {} model".format(num_of_edges,time.time() - time0, model)

time1 = time.time()
time_taken1 = time1 - time0
# print time_taken1
influences = []

print is_naive
if is_naive == 0:
    dmg.naive_operation = False

for edge in edge_set:
    if edge[0] != edge[1] and edge[0] not in a_set:
        dmg.addVertex(edge[0])
        break
    elif edge[0] != edge[1] and edge[1] not in a_set:
        dmg.addVertex(edge[1])
        break


time_taken2 = time.time() - time1
print time_taken2

# for v in a_set:
#     val = dmg.infEst(v)
#     if val > 0: 
#         # print ("Influence of {} is {}".format(v, val))
#         influences.append(val)
# print influences
# print time_taken1
# 
# print ("Most influential vertex is {}".format(dmg.infMax(1)[0]))


# print("--- %s seconds ---" % (time.time() - start_time))
