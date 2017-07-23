import networkx as nx
import sys
from pprint import pprint
from copy import copy


def main():
    cols = int(sys.argv[1])
    rows = int(sys.argv[2])
    edgesFilename = sys.argv[3]
    G=nx.Graph()

    lines = []
    with open(edgesFilename) as fHandle:
        lines = fHandle.readlines()
    for line in lines:
        line = line.strip()
        if line is None or line == '':
            continue
        n1,n2 = line.split(',')
        G.add_edge(n1,n2)

    triangles = set()
    for n in G.nodes():
        triangles |= trianglesFromNode(G,n)
    print(len(triangles))
    #render(G,'triangles.gv')
    txtGrid = []
    blankRow = [' ' for i in range((2*cols)-1)] # we don't need right-most empty cells
    for r in range(rows):
        row = []
        for c in range(cols):
            #row.append("n"+str(r)+str(c))
            row.append('o')
            if c != (cols-1):
                row.append(' ')
        txtGrid.append(row)
        if r != (rows-1):
            txtGrid.append(blankRow.copy())
    for triangle in triangles:
        renderTriangle(txtGrid,triangle)
        return


def isTriangleLegal(n1,n2,n3):
    '''
    detect if three edges lie in a straight line
    take two pairs of nodes, get slope, and if equal then it's a straight line
    '''
    #r1,c1 = __coordsFromNode(n1,1)
    #r2,c2 = __coordsFromNode(n2,1)
    #r3,c3 = __coordsFromNode(n3,1)
    #m1 = 0 if (c2-c1)==0 else (r2-r1)/(c2-c1)
    #m2 = 0 if (c3-c2)==0 else (r3-r2)/(c3-c2)
    #return m1 != m2
    rise1,run1 = __slope(n1,n2)
    rise2,run2 = __slope(n2,n3)
    if run1==0 and run2==0:
        return False
    if run1==0 or run2==0:
        return True
    if (rise1/run1) == (rise2/run2):
        return False
    return True


def trianglesFromNode(graph,node):
    '''
    returns a set of triangles that can be formed from edges starting at node 'node'
    the triangles in the set returned are represented as frozensets of 3 nodes
    '''
    triangles = set()
    for e1 in graph.edges(node):
        assert node in e1
        assert not ((e1[0] == node) and (e1[1] == node))
        n1 = e1[1] if e1[0] == node else e[0]
        for e2 in graph.edges(n1):
            assert n1 in e2
            assert not ((e2[0] == n1) and (e2[1] == n1))
            n2 = e2[1] if e2[0] == n1 else e2[0]
            if n2 == node:
                continue
            for e3 in graph.edges(n2):
                assert n2 in e3
                assert not ((e3[0] == n2) and (e3[1] == n2))
                n3 = e3[1] if e3[0] == n2 else e3[0]
                if n3 != node or n3 == n1 or n3 == n2:
                    continue
                if isTriangleLegal(n1,n2,n3):
                    triangles.add(frozenset(sorted([node,n1,n2])))
    return triangles


def renderTriangle(txtGrid,triangle):
    triangle = list(triangle)
    print(triangle)
    nodePairs = [(0,1),(0,2),(1,2)]
    for i,j in nodePairs:
        n1,n2 = triangle[i],triangle[j]
        print("%s,%s" % (n1,n2))
        r1,c1 = __coordsFromNode(n1,2)
        r2,c2 = __coordsFromNode(n2,2)
        txtGrid[r1][c1] = '*'
        txtGrid[r2][c2] = '*'
        if False and (r1!=r2) and (c1!=c2):
            # it's a diagonal
            print('diagonal')
            mnR = min(r1,r2)
            mxR = max(r1,r2)
            mxC = max(c1,c2)
            mnC = min(c1,c2)
            while mnR <= mxR:
                print('setting [%s][%s]' % (mnR,mnC))
                txtGrid[mnR][mnC] = '*'
                mnC += 1
                mnR += 1
        if True or (r1==r2):
            # it's a horizontal
            print('horizontal')
            rise,run = __slope(n1,n2)
            print('rise %s, run %s' % (rise,run))
            _r1 = r1
            _c1 = c1
            while (_r1!=r2) or (_c1!=c2):
                print('setting [%s][%s]' % (_r1,_c1))
                txtGrid[_r1][_c1] = '*'
                _r1 += rise
                _c1 += run
#            mnC = min(c1,c2)
#            mxC = max(c1,c2)
#            while mnC <= mxC:
#                print('setting [%s][%s]' % (r1,mnC))
#                txtGrid[r1][mnC] = '*'
#                mnC += 1
        if False and (c1==c2):
            # it's a vertical
            print('vertical')
            mnR = min(r1,r2)
            mxR = max(r1,r2)
            while mnR <= mxR:
                print("setting [%s][%s]" % (mnR,c1))
                txtGrid[mnR][c1] = '*'
                mnR += 1
    pprint(txtGrid)


def render(G,filename):
    boilerplateBegin = '''
digraph G {
	graph [center=1 rankdir=LR bgcolor="#808080"]
	edge [dir=none splines=false]
	node [width=0.3 height=0.3]
	{ node [shape=circle]
		n00 n10 n20 n30 n40
	}
	{ node [shape=diamond]
		n01 n11 n21 n31 n41
	}
	{ node [shape=square]
		n02 n12 n22 n32 n42
	}
	{ node [shape=triangle]
		n03 n13 n23 n33 n43
	}
	{ node [shape=ellipse]
		n04 n14 n24 n34 n44
	}
	{ edge [color="#ffffff"]
'''
    boilerplateEnd = '''
	}
}
'''
    with open(filename,'w') as fHandle:
        fHandle.write(boilerplateBegin)
        for n in G.nodes():
            for edge in G.edges(n):
                fHandle.write('		%s -> %s\n' % edge)
        fHandle.write(boilerplateEnd)
        fHandle.close()


def __slope(n1,n2):
    '''
    returns the slope of the line connecting two points n1,n2
    we don't want to deal with infinity so we return a tuple of
    the rise,run
    '''
    r1,c1 = __coordsFromNode(n1,1)
    r2,c2 = __coordsFromNode(n2,1)
    rise = r2-r1
    run  = c2-c1
#    if rise < 0 and run < 0:
#        return -rise,-run
    same = rise == run
    if rise == 0 or same:
        if run > 1:
            run = 1
        if run < 1:
            run = -1
    if run == 0 or same:
        if rise > 1:
            rise = 1
        if rise < -1:
            rise = -1
    
    return rise,run


def __coordsFromNode(node,scale):
    '''
    node is a str in form of n01 or n22
    generally it's nRC where R==row and C==col
    returns r,c tuple
    scale is an int multiplier where 1 is par, 2 is 2x
    i.e. scale=2 with n21 would return 4,2
    '''
    return (int(node[1])*scale,int(node[2])*scale)


if __name__ == '__main__':
    main()
