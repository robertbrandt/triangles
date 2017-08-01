import networkx as nx
import sys
from copy import copy


def main():
    maxCol = maxRow = 0
    edgesFilename = sys.argv[1]
    G = nx.Graph()

    lines = []
    with open(edgesFilename) as fHandle:
        lines = fHandle.readlines()
    for line in lines:
        line = line.strip()
        if line is None or line == '':
            continue
        n1,n2 = line.split(',')
        G.add_edge(n1,n2)
        for n in [n1,n2]:
            r,c = __coordsFromNode(n,1)
            if r > maxRow: maxRow = r
            if c > maxCol: maxCol = c

    triangles = set()
    for n in G.nodes():
        triangles |= trianglesFromNode(G,n)
    print(len(triangles))
    # print rendering of each triangle
    # we'll do it node-by-node so there's some organization of it
    displayedTriangles = set()
    for node in sorted(G.nodes()):
        for triangle in triangles:
            if node in triangle and triangle not in displayedTriangles:
                txtGrid = __makeGrid(maxCol+1,maxRow+1)
                renderTriangle(txtGrid,triangle)
                displayedTriangles.add(triangle)


def isTriangleLegal(n1,n2,n3):
    '''
    detect if three edges lie in a straight line
    take two pairs of nodes, get slope, and if equal then it's a straight line
    '''
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


def gridPrint(txtGrid):
    for line in txtGrid:
        print(''.join(line))


def renderTriangle(txtGrid,triangle):
    triangle = list(triangle)
    print(triangle)
    nodePairs = [(0,1),(0,2),(1,2)]
    for i,j in nodePairs:
        n1,n2 = triangle[i],triangle[j]
        r1,c1 = __coordsFromNode(n1,2)
        r2,c2 = __coordsFromNode(n2,2)
        #print('writing %s,%s' % (r1,c1))
        #print('writing %s,%s' % (r2,c2))
        txtGrid[r1][c1] = '*'
        txtGrid[r2][c2] = '*'
        rise,run = __slope(n1,n2)
        _r1 = r1
        _c1 = c1
        while (_r1!=r2) or (_c1!=c2):
            #print('writing %s,%s with rise %s and run %s' % (_r1,_c1,rise,run))
            txtGrid[_r1][_c1] = '*'
            _r1 += rise
            _c1 += run
    gridPrint(txtGrid)


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
    same = abs(rise) == abs(run)
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


def __makeGrid(cols,rows):
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
    return txtGrid


if __name__ == '__main__':
    main()
