from collections import defaultdict
import random
import math
import matplotlib.pyplot as plt
import numpy




def readData(file):
	PyEdgeInf = defaultdict(lambda: defaultdict(list))
	PyTimeInf = defaultdict(lambda: defaultdict(list))
	Pylab =defaultdict(lambda: defaultdict(list))
	PynoEdge = set([])
	with open(file) as f:
		content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content] 
	i=0
	while i < len(content):
		Pylab = content[i]
		edges = int(content[i+1])
		PynoEdge.add(edges)
		a = content[i+2].replace("[", "").replace("]", "").replace(",","").split()
		results = map(float, a)
		time = content[i+3]
		PyEdgeInf[Pylab][edges] += results
		PyTimeInf[Pylab][edges].append(time)
		i=i+4
	return (PyEdgeInf,PyTimeInf,Pylab,PynoEdge)
	




def plot_hist(name,x,y ,title, lab1, lab2):
	bins = numpy.linspace(-10, 10, 100)
	plt.plot(range(len(x)), x, 'r', label=lab1)
   	plt.plot(range(len(y)), y, 'g', label=lab2)
#	plt.hist(x, bins, alpha=0.5, label=lab1)
#	plt.hist(y, bins, alpha=0.5, label=lab2)
	plt.legend(loc='upper right')
	plt.savefig(name)
   	plt.close()

def plot_graph(name, edges1, edges2, error1,error2 , error3, error4, title, lab1, lab2, lab3, lab4,xlabel,ylabel):
	plt.plot(edges1, error1, 'r', label=lab1)
   	plt.plot(edges1, error2, 'g', label=lab2)
   	plt.plot(edges2, error3, 'b', label=lab3)
   	plt.plot(edges2, error4, 'c', label=lab4)
   	plt.title(title)
    	plt.xlabel(xlabel)
    	plt.ylabel(ylabel)
    	plt.xscale('log')
    	plt.legend(loc='upper right')
    	plt.savefig(name)
    	plt.close()

PyEdgeInf,PyTimeInf,Pylab,PynoEdge = readData('pyth.txt')
CEdgeInf,CTimeInf,Clab,CnoEdge = readData('cpp.txt')
a = sorted(sum(PyTimeInf['TR'].values(), []))
b = sorted(sum(PyTimeInf['WC'].values(), []) )
c = sorted(sum(CTimeInf['TR'].values(), []) )
d = sorted(sum(CTimeInf['WC'].values(), []) )

plot_graph('Time Plot', list(PynoEdge),list(CnoEdge),a,b,c,d,'CPP Python RunTime Comparisons','Python TR',' Python WC','CPP TR',' CPP WC','Edges','Time' )
plot_hist('Influence Histogram', sorted(PyEdgeInf['TR'][500] , reverse = True) , sorted(CEdgeInf['TR'][500] , reverse = True) , 'Influence Histogram' , 'Python' , 'CPP')



