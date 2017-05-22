from DynamicGraph import DynamicGraph
dmg = DynamicGraph()
# dmg.init() # Call at the beginning

dmg.addVertex(0) # Insert vertex 0
dmg.addVertex(1) # Insert vertex 1
dmg.addEdge(0, 1, 0.4) # Insert edge (0,1) with probability 0.5
dmg.set_beta(32) # Set beta=32

dmg.addVertex(2) # Insert vertex 2
dmg.addVertex(3) # Insert vertex 3
dmg.addEdge(1, 2, 0.5) # Insert edge (1,2) with probability 0.6
dmg.addEdge(2, 0, 0.6) # Insert edge (2,0) with probability 0.7
dmg.addEdge(2, 3, 0.7) # Insert edge (2,3) with probability 0.8

for v in range(0,4):
    print "Influence of {} is {}".format(v, dmg.infEst(v))

print "Most influential vertex is {}".format(dmg.infMax(1)[0])

dmg.addEdge(3, 1, 0.8) # Insert edge (3,1) with probability 0.8
dmg.delEdge(2, 3) # Delete edge (2,3)

for v in range(0,4):
    print "Influence of {} is {}".format(v, dmg.infEst(v))

print "Most influential vertex is {}".format(dmg.infMax(1)[0])

dmg.delVertex(2) #Delete vertex 2
dmg.changeEdge(0, 1, 0.9) # Change probability of edge (0,1) to 0.9

for v in range(0,4):
    print "Influence of {} is {}".format(v, dmg.infEst(v))

<<<<<<< HEAD
print "Most influential vertex is {}".format(dmg.infMax(4)[-1])
=======
print "Most influential vertex is {}".format(dmg.infMax(1)[0])

>>>>>>> aa8afeefb79f78d3de1c4eee9c16d966a8f6bf0f
