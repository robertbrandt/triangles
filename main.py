import networkx as nx


def ChaseDorset():
    G=nx.Graph()
    for c in range(5):
        for r in range(5):
            G.add_node('n'+str(r)+str(c))

    G.add_edge('n00','n01')
    G.add_edge('n00','n02')
    G.add_edge('n00','n03')
    G.add_edge('n00','n04')
    G.add_edge('n00','n10')
    G.add_edge('n00','n20')
    G.add_edge('n00','n30')
    G.add_edge('n00','n40')
    G.add_edge('n00','n11')
    G.add_edge('n00','n22')
    G.add_edge('n00','n33')
    G.add_edge('n00','n44')
    
    G.add_edge('n01','n00')
    G.add_edge('n01','n02')
    G.add_edge('n01','n03')
    G.add_edge('n01','n04')
    G.add_edge('n01','n11')
    G.add_edge('n01','n21')
    G.add_edge('n01','n31')
    G.add_edge('n01','n41')
    
    G.add_edge('n02','n01')
    G.add_edge('n02','n00')
    G.add_edge('n02','n03')
    G.add_edge('n02','n04')
    G.add_edge('n02','n11')
    G.add_edge('n02','n20')
    G.add_edge('n02','n13')
    G.add_edge('n02','n24')
    G.add_edge('n02','n12')
    G.add_edge('n02','n22')
    G.add_edge('n02','n32')
    G.add_edge('n02','n42')
    
    G.add_edge('n03','n02')
    G.add_edge('n03','n01')
    G.add_edge('n03','n00')
    G.add_edge('n03','n04')
    G.add_edge('n03','n13')
    G.add_edge('n03','n23')
    G.add_edge('n03','n33')
    G.add_edge('n03','n43')
    
    G.add_edge('n04','n03')
    G.add_edge('n04','n02')
    G.add_edge('n04','n01')
    G.add_edge('n04','n00')
    G.add_edge('n04','n14')
    G.add_edge('n04','n24')
    G.add_edge('n04','n34')
    G.add_edge('n04','n44')
    G.add_edge('n04','n13')
    G.add_edge('n04','n22')
    G.add_edge('n04','n31')
    G.add_edge('n04','n40')

    G.add_edge('n10','n11')
    G.add_edge('n10','n12')
    G.add_edge('n10','n13')
    G.add_edge('n10','n14')
    G.add_edge('n10','n20')
    G.add_edge('n10','n30')
    G.add_edge('n10','n40')
    G.add_edge('n10','n00')

    G.add_edge('n11','n10')
    G.add_edge('n11','n12')
    G.add_edge('n11','n13')
    G.add_edge('n11','n14')
    G.add_edge('n11','n00')
    G.add_edge('n11','n20')
    G.add_edge('n11','n21')
    G.add_edge('n11','n31')
    G.add_edge('n11','n41')
    G.add_edge('n11','n22')
    G.add_edge('n11','n33')
    G.add_edge('n11','n44')
    G.add_edge('n11','n01')
    G.add_edge('n11','n02')

    G.add_edge('n12','n11')
    G.add_edge('n12','n10')
    G.add_edge('n12','n13')
    G.add_edge('n12','n14')
    G.add_edge('n12','n02')
    G.add_edge('n12','n22')
    G.add_edge('n12','n32')
    G.add_edge('n12','n42')
    
    G.add_edge('n13','n12')
    G.add_edge('n13','n11')
    G.add_edge('n13','n10')
    G.add_edge('n13','n14')
    G.add_edge('n13','n03')
    G.add_edge('n13','n23')
    G.add_edge('n13','n33')
    G.add_edge('n13','n43')
    G.add_edge('n13','n04')
    G.add_edge('n13','n22')
    G.add_edge('n13','n31')
    G.add_edge('n13','n40')
    G.add_edge('n13','n02')
    G.add_edge('n13','n24')
    
    G.add_edge('n14','n13')
    G.add_edge('n14','n12')
    G.add_edge('n14','n11')
    G.add_edge('n14','n10')
    G.add_edge('n14','n04')
    G.add_edge('n14','n24')
    G.add_edge('n14','n34')
    G.add_edge('n14','n44')

    G.add_edge('n20','n21')
    G.add_edge('n20','n22')
    G.add_edge('n20','n23')
    G.add_edge('n20','n24')
    G.add_edge('n20','n10')
    G.add_edge('n20','n00')
    G.add_edge('n20','n30')
    G.add_edge('n20','n40')
    G.add_edge('n20','n11')
    G.add_edge('n20','n02')
    G.add_edge('n20','n31')
    G.add_edge('n20','n42')

    G.add_edge('n21','n20')
    G.add_edge('n21','n22')
    G.add_edge('n21','n23')
    G.add_edge('n21','n24')
    G.add_edge('n21','n11')
    G.add_edge('n21','n01')
    G.add_edge('n21','n31')
    G.add_edge('n21','n41')
    
    G.add_edge('n22','n21')
    G.add_edge('n22','n20')
    G.add_edge('n22','n23')
    G.add_edge('n22','n24')
    G.add_edge('n22','n12')
    G.add_edge('n22','n02')
    G.add_edge('n22','n32')
    G.add_edge('n22','n42')
    G.add_edge('n22','n11')
    G.add_edge('n22','n00')
    G.add_edge('n22','n33')
    G.add_edge('n22','n44')
    G.add_edge('n22','n13')
    G.add_edge('n22','n04')
    G.add_edge('n22','n31')
    G.add_edge('n22','n40')
   
    G.add_edge('n23','n22')
    G.add_edge('n23','n21')
    G.add_edge('n23','n20')
    G.add_edge('n23','n24')
    G.add_edge('n23','n13')
    G.add_edge('n23','n03')
    G.add_edge('n23','n33')
    G.add_edge('n23','n43')


    G.add_edge('n24','n23')
    G.add_edge('n24','n22')
    G.add_edge('n24','n21')
    G.add_edge('n24','n20')
    G.add_edge('n24','n14')
    G.add_edge('n24','n04')
    G.add_edge('n24','n34')
    G.add_edge('n24','n44')
    G.add_edge('n24','n13')
    G.add_edge('n24','n02')
    G.add_edge('n24','n33')
    G.add_edge('n24','n42')
    

    G.add_edge('n30','n31')
    G.add_edge('n30','n32')
    G.add_edge('n30','n33')
    G.add_edge('n30','n34')
    G.add_edge('n30','n20')
    G.add_edge('n30','n10')
    G.add_edge('n30','n00')
    G.add_edge('n30','n40')
    

    G.add_edge('n31','n30')
    G.add_edge('n31','n32')
    G.add_edge('n31','n33')
    G.add_edge('n31','n34')
    G.add_edge('n31','n21')
    G.add_edge('n31','n11')
    G.add_edge('n31','n01')
    G.add_edge('n31','n41')
    G.add_edge('n31','n20')
    G.add_edge('n31','n42')
    G.add_edge('n31','n40')
    G.add_edge('n31','n22')
    G.add_edge('n31','n13')
    G.add_edge('n31','n04')

    G.add_edge('n32','n31')
    G.add_edge('n32','n30')
    G.add_edge('n32','n33')
    G.add_edge('n32','n34')
    G.add_edge('n32','n22')
    G.add_edge('n32','n12')
    G.add_edge('n32','n02')
    G.add_edge('n32','n42')
    

    G.add_edge('n33','n32')
    G.add_edge('n33','n31')
    G.add_edge('n33','n30')
    G.add_edge('n33','n34')
    G.add_edge('n33','n23')
    G.add_edge('n33','n13')
    G.add_edge('n33','n03')
    G.add_edge('n33','n43')
    G.add_edge('n33','n24')
    G.add_edge('n33','n42')
    G.add_edge('n33','n22')
    G.add_edge('n33','n11')
    G.add_edge('n33','n00')
    G.add_edge('n33','n44')

    G.add_edge('n34','n33')
    G.add_edge('n34','n32')
    G.add_edge('n34','n31')
    G.add_edge('n34','n30')
    G.add_edge('n34','n24')
    G.add_edge('n34','n14')
    G.add_edge('n34','n04')
    G.add_edge('n34','n44')
    

    G.add_edge('n40','n41')
    G.add_edge('n40','n42')
    G.add_edge('n40','n43')
    G.add_edge('n40','n44')
    G.add_edge('n40','n30')
    G.add_edge('n40','n20')
    G.add_edge('n40','n10')
    G.add_edge('n40','n00')
    G.add_edge('n40','n31')
    G.add_edge('n40','n22')
    G.add_edge('n40','n13')
    G.add_edge('n40','n04')
    

    G.add_edge('n41','n40')
    G.add_edge('n41','n42')
    G.add_edge('n41','n43')
    G.add_edge('n41','n44')
    G.add_edge('n41','n31')
    G.add_edge('n41','n21')
    G.add_edge('n41','n11')
    G.add_edge('n41','n01')
    

    G.add_edge('n42','n41')
    G.add_edge('n42','n40')
    G.add_edge('n42','n43')
    G.add_edge('n42','n44')
    G.add_edge('n42','n32')
    G.add_edge('n42','n22')
    G.add_edge('n42','n12')
    G.add_edge('n42','n02')
    G.add_edge('n42','n33')
    G.add_edge('n42','n24')
    G.add_edge('n42','n31')
    G.add_edge('n42','n20')
    

    G.add_edge('n43','n42')
    G.add_edge('n43','n41')
    G.add_edge('n43','n40')
    G.add_edge('n43','n44')
    G.add_edge('n43','n33')
    G.add_edge('n43','n23')
    G.add_edge('n43','n13')
    G.add_edge('n43','n03')
    

    G.add_edge('n44','n43')
    G.add_edge('n44','n42')
    G.add_edge('n44','n41')
    G.add_edge('n44','n40')
    G.add_edge('n44','n34')
    G.add_edge('n44','n24')
    G.add_edge('n44','n14')
    G.add_edge('n44','n04')
    G.add_edge('n44','n33')
    G.add_edge('n44','n22')
    G.add_edge('n44','n11')
    G.add_edge('n44','n00')
    

    triangles = set()
    #print(list(G.nodes()))
    for c in range(5):
        for r in range(5):
            triangles |= trianglesFromNode(G,'n'+str(r)+str(c))
    print(len(triangles))
    #print(list(G.edges()))
    #print(list(G.edges('n00')))
    #A = nx.nx_agraph.to_agraph(G)
    #A.write('grid.dot')     # write to dot file
    render(G,'t.gv')

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
                triangles.add(frozenset([node,n1,n2]))
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
        for c in range(5):
            for r in range(5):
                for edge in G.edges('n'+str(r)+str(c)):
                    fHandle.write('		%s -> %s\n' % edge)
        fHandle.write(boilerplateEnd)
        fHandle.close()

def viz():
    G = nx.complete_graph(5)   # start with K5 in networkx
    A = nx.nx_agraph.to_agraph(G)        # convert to a graphviz graph
    X1 = nx.nx_agraph.from_agraph(A)     # convert back to networkx (but as Graph)
    X2 = nx.Graph(A)          # fancy way to do conversion
    G1 = nx.Graph(X1)          # now make it a Graph
    A.write('k5.dot')     # write to dot file
    X3 = nx.nx_agraph.read_dot('k5.dot') # read from dotfile


def main():
    ChaseDorset()
    #viz()

main()
