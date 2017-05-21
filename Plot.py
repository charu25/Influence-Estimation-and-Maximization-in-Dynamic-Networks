from collections import defaultdict
import random
import math
import matplotlib.pyplot as plt
with open('out.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
print len(content)
EdgeInf = defaultdict(lambda: defaultdict(list))
TimeInf = defaultdict(lambda: defaultdict(list))
lab =defaultdict(lambda: defaultdict(list))
noEdge = set([])
i=0
while i < len(content):
	lab = content[i]
	edges = int(content[i+1])
	noEdge.add(edges)
	a = content[i+2].replace("[", "").replace("]", "").replace(",","").split()
	results = map(float, a)
	time = content[i+3]
	EdgeInf[lab][edges] += results
	TimeInf[lab][edges].append(time)
	i=i+4
print EdgeInf['WC'][10]
print TimeInf['TR'][10]





def plot_graph(error1,error2 ,title, lab1, lab2,xlabel,ylabel):
    plt.plot(range(len(error1)), error1, 'r', label=lab1)
   	plt.plot(range(len(error2)), error2, 'g', label=lab2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='upper right')
    plt.savefig('graph1')
    plt.close()
plot_graph(EdgeInf['TR'][10],EdgeInf['WC'][10],"TR WC Inf plots for edges = 10",'TR','WC','Edges','Influences' )
print 'abc'
