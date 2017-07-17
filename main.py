import networkx as nx
import sys


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
    render(G,'triangles.gv')


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
                triangles.add(frozenset(sorted([node,n1,n2])))
    return triangles


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


if __name__ == '__main__':
    main()
