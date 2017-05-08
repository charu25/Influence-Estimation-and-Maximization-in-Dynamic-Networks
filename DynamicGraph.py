import random as rng

class Hedge(object):
    def __init__(self):
        self.H = set([])
        self.par = []
        self.x = []
        self.z = -1

class DynamicGraph(object):
    Vertices = {}
    VtoIndices = {}
    W = 0
    IndegMap = {}
    ps = {}
    rs = {}
    TOT = -1
    hs = []
    ws = []


    def _get_R():
        n, m = len(self.Vertices), len(self.ps)
        return (self.beta * (n + m) * np.log2(n))

    def _next_target(at):
        n = len(self.vertexList)

        cnt = 0
        while True:
            rng.seed(n)
            z = random.choice(self.vertexList)

            if (z in self.Vertices):
                return z

            cnt += 1

    def __init__(self):
        self.name = ""

    #u is the source ,v vertex and p is prob
    def addEdge(u,v,p):
        print "yafg"

    def addVertex(u):
        print "yafg"


    def delVertex(u):
        print"ToDO"

    def delEdge(u,v):
        if (u,v) not in self.ps:
            print 'Warning: Edge (%d, %d) does not exist.' % (u,v)
            return
        else:
            _change(u, v, 0)

            for node in VtoIndices[v]:
                _weight(node, -1)

            self.ps.remove((u,v))
            self.ps.remove((v,u))
            self.IndegMap[v] -= 1
            _adjust()

    def changeEdge(u,v,p):
        print "To DO"

    def _adjust():
        R = _get_R()

        rem = 0
        add = 0

        while self.TOT < R:
            z = _next_target(len(self.hs))

            h = Hedge()
            h.z = z
            self.hs.append(h)
            self.ws.append(0)
            expand(len(hs) - 1, h.z)

            add += 1

        for at in range(len(self.hs)-1, 0, -1):

            if (self.TOT - self.ws[at]) < R:
                break

            _clear(at)
            self.hs.pop()
            self.ws.pop()

            rem += 1



    def _shrink(att):
        print ""


    def _expand(at, z):
        print "To do"

    def infEst(vSet):
        hit = 0

        for i in range(len(hs)):
            for v in vSet:
                if (v in hs[i].H):
                    hit += 1
                    break

        return (1.0 * hit * len(Vertices))/(len(hs))

    def _clear(at):

        for v in self.hs[at].H:
            self.VtoIndices[v].remove(at)

        _weight(at, -selft.ws[at])
        self.hs[at].H = []
        self.hs[at].x = []
        self.hs[at].par = []

    def infMax():
        print "To do"

    def _weight(at, dw):
        self.ws[at] += dw
        self.TOT += dw
