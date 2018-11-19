
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import graphviz as gv


import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

def grDraw(n, weights):
    labels = range(1,n+1)
    Gr = nx.Graph()
    Gr.add_nodes_from(labels)
    for j in range(n):
        for k in range(j, n):
            if (weights[j][k] != 0):
                Gr.add_edge(j+1, k+1, weight=weights[j][k])

    pos = nx.spring_layout(Gr)
    nx.draw_networkx_edge_labels(Gr, pos,node_size=1000, font_size= 6, label_pos = 1.)
    nx.draw_spring(Gr,with_labels = True, node_size=100, font_size= 10)
    pylab.show()

def grViz(n, weights, Name):
    g = gv.Graph(Name, filename=Name, engine='circo')
    g.node_attr.update(color='lightblue2', style='filled')
    g.attr(rankdir='LR', size='8,5')
    labels = range(1, n + 1)
    for i in labels:
        g.node(str(i))
    for j in range(n):
        for k in range(j, n):
            if (weights[j][k] != 0):
                g.edge(str(j+1), str(k+1), label=str(weights[j][k]))
    g.render('Graphs/'+Name, view=True)
    g.view()

    # print(g.source)
    # dot.render('test-output/round-table.gv', view=True)