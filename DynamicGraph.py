from bisect import bisect_left
import Queue
from collections import deque
import random
import numpy as np
from collections import defaultdict

class Hedge(object):
    def __init__(self):
        self.H = set()
        self.par = []
        self.x = []
        self.z = -1

class Xorshift:
    def helper(self, s, i):
        return 1812433253 * (s ^ (s >> 30)) + i + 1

    def __init__(self, seed):
        self.x = self.helper(seed, 0)
        self.y = self.helper(self.x, 1)
        self.z = self.helper(self.y, 2)
        self.w = self.helper(self.z, 3)

    def __init__(self):
        self.x = self.helper(0, 0)
        self.y = self.helper(self.x, 1)
        self.z = self.helper(self.y, 2)
        self.w = self.helper(self.z, 3)

    def gen_int(self):
        t = self.x ^ (self.x << 11)
        self.x = self.y
        self.y = self.z
        self.z = self.w
        self.w = self.w ^ (self.w >> 19) ^ t ^ (t >> 8)
        return self.w

    def gen_int2(self, n):
        return int(n * self.gen_double())

    def gen_double(self):
        a, b = abs(self.gen_int()) >> 5, abs(self.gen_int()) >> 6
        return (a * 67108864.0 + b) * (1.0 / (1 << 53))


class DynamicGraph(object):
    Vertices = set([])
    VtoIndices = defaultdict(list)
    W = 0
    IndegMap = {}
    ps = {}
    rs = {}
    TOT = -1
    hs = []
    ws = []
    VertexList = []
    beta = 0.0

    rng = Xorshift()

    def __init__(self):
        self.name = ""

    def _next_target(self, at):
        n = len(self.VertexList)
        while True:
            x = self.rng.gen_int2(n)
            print x
            z = self.VertexList[x]
            if (z in self.Vertices):
                return z

    def _weight(self, at, dw):
        self.ws[at] += dw
        self.TOT += dw

    def _get_R(self):
        n, m = len(self.Vertices), len(self.ps)
        return (self.beta * (n + m) * np.log2(n))


    def set_beta(self, beta_val):
        self.beta = beta_val

    #u is the source ,v vertex and p is prob
    def addEdge(self,u,v,p):
        if u==v or u not in self.Vertices or v not in self.Vertices:
            print "Invalid Edge"

        elif (u,v) in self.ps: #PS is dict with key (u,v)
            print "Edge exists"

        else:
            self.ps[(u, v)] = 0
            self.rs[(v, u)] = 0
            self.IndegMap[v]+=1
        for at in self.VtoIndices[v]: #Adding 1 to weights of all subgraph containing v
            self._weight(at, +1)

        self.changeEdge(u, v, p)
        self._adjust()

    def addVertex(self, u):
        if u in self.Vertices:
            return
        else:
            self.IndegMap[u] = 0
            self.Vertices.add(u)
            self.VertexList.append(u)

            for at in range(0, len(self.hs)):
                prob = 1.0/len(self.Vertices)
                temp = random.uniform(0, 1)
                if (temp < prob):
                    self._clear(at)
                    self.hs[at].z = u
                    self._expand(at, u)
        self._adjust()

    def delEdge(self,u,v):
        if (u,v) not in self.ps:
            print 'Warning: Edge (%d, %d) does not exist.' % (u,v)
            return
        else:
            self.changeEdge(u, v, 0)

            for node in self.VtoIndices[v]:
                self._weight(node, -1)

            self.ps.pop((u,v))
            self.rs.pop((v,u))
            self.IndegMap[v] -= 1
            self._adjust()

    def _adjust(self):
        R = self._get_R()
        rem = 0
        add = 0

        while self.TOT < R:
            z = self._next_target(len(self.hs))

            h = Hedge()
            h.z = z
            self.hs.append(h)
            self.ws.append(0)
            self._expand(len(self.hs) - 1, h.z)

            add += 1

        for at in range(len(self.hs)-1, 0, -1):

            if (self.TOT - self.ws[at]) < R:
                break

            self._clear(at)
            self.hs.pop()
            self.ws.pop()

            rem += 1

    def changeEdge(self,u,v,p):
        self.ps[(u, v)] = p
        self.rs[(v, u)] = p
        for at in self.VtoIndices[v]:
            jt = bisect_left(self.hs[at].x, (v, u), lo=0, hi=len(self.hs[at].x))
            uv1 = jt != len(self.hs[at].x) and self.hs[at].x[jt] == (v,u)
            uv2 = rng.uniform(0,1) < p
            # Case 1: dead -> live
            if not uv1 and uv2 :
                self.hs[at].x.insert(jt, (v, u))
                if u not in self.hs[at].H:
                    kt = bisect_left(self.hs[at].par, (v, u), lo=0, hi=len(self.hs[at].par))
                    self.hs[at].par.insert(kt, (v, u))
                    self._expand(at, u)


            # Case 2:live -> dead
            if uv1 and not uv2 :
                del self.hs[at].x[jt]
                self._shrink(at)

    def delVertex(self,v):
        if v in self.Vertices :
            "vertex {} was not found.".format(v)
            return
        else :
            ine = [] 
            out = []

            # OUT-edges `from' v
            for it in range(bisect_left(self.ps, (v, 0), lo=0, hi=len(self.ps)), len(self.ps)) :
                if it[0] != v:
                    break
                out.append(it[1])

            # IN-edges `to' v
            for it in range(bisect_left(self.rs, (v, 0), lo=0, hi=len(self.rs)), len(self.rs)) :
                if it[0] != v:
                    break
                ine.append(it[1])

            # Remove OUT-edges from each sketch
            for w in out :
                for at in self.VtoIndices[w]:
                    e = (w, v)
                    jt = bisect_left(self.hs[at].x, e, lo = 0, hi=len(self.hs[at].x))
                    if (jt != len(self.hs[at].x) and jt == e) :
                        self.hs[at].x.remove(jt)
                    self._weight(at, -1) # Removal of (v, w)

            # So that _next_target MUST not return v
            self.Vertices.remove(v)
            for w in out :
                # Remove (v, w)
                self.ps.remove((v, w))
                self.rs.remove((w, v))
                self.IndegMap[w]-=1

            # Scan sketches that have v
            for at in self.VtoIndices[v] :
                if (self.hs[at].z == v) : # If target = v
                    # Reconstruction
                    self._clear(at)
                    self.hs[at].z = self._next_target(at)
                    self._expand(at, self.hs[at].z)
                else : #{ // Otherwise
                    # Remove vertices that can no longer reach to z
                    self._shrink(at)

            # Remove IN-edges to v
            for u in ine :
                self.ps.remove((u, v))
                self.rs.remove((v, u))
                self.IndegMap[v]-=1
            self.IndegMap.remove(v)
            self._adjust()

    def _shrink(self,att):
        #clear -> TO DO
        self._clear(att) 
        queue = deque()
        queue.append(self.hs[att].z)
        X = set()
        X.add(self.hs[att].z)
        while (len(queue) > 0):
            currentVert = queue.pop()
            for i in self.hs[att].x[:bisect_left(self.hs[att].x,(currentVert,0))]:
                if i[1] not in X:
                    X.add(i[1])
                    queue.append(i[1])
                    X.add(i[1])
                    self.hs[att].par.append((currentVert,i[1]))
        sorted(self.hs[att].par)
        Y = self.hs[att].H - X
        self.hs[att].x = [(u,v) for u, v in self.hs[att].x if u in Y]
        ## Adjust weights -> To DO
        self.hs[att].H =  self.hs[att].H.difference(Y)
        for v in Y:
            self.VtoIndices[v].remove(att)

            self._weight(att,-self.IndegMap[v])
            self._weight(att,-1)

    def _expand(self, at, z):
        if z not in self.hs[at].H:
            revbfs = []
            revbfs.append(z)
            self.hs[at].H.add(z)
            self._weight(at, +1 + self.IndegMap[z])

            while(len(revbfs)!=0):
                v = revbfs.pop(0)

                self.VtoIndices[v].append(at)
                for key, value in self.rs.iteritems():
                    if key[0]==v:
                        u=key[1]
                        p=value
                        x = rng.uniform(0,1)
                        if p > x: #Edge is live
                            self.hs[at].x.append((v,u))
                            if u not in self.hs[at].H:
                                revbfs.append(u)
                                self.hs[at].H.add(u)
                                self._weight(at,+1+self.IndegMap[u])
                                self.hs[at].par.append((v,u))


            self.hs[at].x = sorted(self.hs[at].x, key=lambda tup: (tup[0],tup[1]))
            self.hs[at].par = sorted(self.hs[at].par, key=lambda tup: (tup[0],tup[1]))

    def infEst(self, vSet):
        hit = 0
        for i in range(len(self.hs)):
            for v in vSet:
                if (v in self.hs[i].H):
                    hit += 1
                    break

        return (1.0 * hit * len(self.Vertices))/(len(self.hs))

    def _clear(self, at):

        for v in self.hs[at].H:
            self.VtoIndices[v].remove(at)

        self._weight(at, -self.ws[at])
        self.hs[at].H = set()
        self.hs[at].x = []
        self.hs[at].par = []


    def infMax(self, k):
        n = len(self.Vertices)
        # vector<ULL> degs(n)
        I = [False]*len(self.hs)

        degs = [0]*n

        Q = Queue.PriorityQueue()

        # priority_queue<tuple<LL, int, int> > Q
        # <deg, v, tick>

        for v in self.Vertices :
            degs[v] = len(self.VtoIndices[v])
            Q.put((degs[v], v, 0))

        S = []
        iter = 0
        while iter < k :
            e = Q.get()
            v = e[1] 
            tick = e[2]
            if tick == iter :
                S.append(v)
                for at in self.VtoIndices[v] :
                    if not I[at] :
                        I[at] = True
                        for v in self.hs[at].H :
                            degs[v] -= 1
                iter+=1
            else :
                Q.push((degs[v], v, iter))

        return S
