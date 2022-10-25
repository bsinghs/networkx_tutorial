import itertools
import random

import networkx as nx
from matplotlib import pyplot as plt

import scipy as sp
#import scipy.io  # for mmread() and mmwrite()
from scipy.io import mmread
import io

fh = io.BytesIO()
# G = nx.complete_graph(5)
# a = nx.to_numpy_array(G)
# print(a)
# sp.io.mmwrite(fh, a)
# print(fh.getvalue().decode('utf-8'))

#nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Generate Networkx Graph
# G = nx.Graph()
# G.add_nodes_from(nodes)

# # randomly determine vertices
# for (node1, node2) in itertools.combinations(nodes, 2):
#     if random.random() < 0.5:
#         G.add_edge(node1, node2)

#G = nx.read_gml("soc-twitter-follows.mtx")
#G = scipy.io.mmread('soc-twitter-follows.mtx')
#G = scipy.io.mmread('soc-youtube.mtx')
with open('soc-youtube.mtx') as mass_file:
    x = mmread(mass_file)
    # H = nx.from_numpy_array(mmread(mass_file))
    # print(H.edges())


# Draw generated graph
#nx.draw_networkx(G, pos=nx.circular_layout(G), with_labels=True)

# Compute Page Rank
#pr = nx.pagerank(G, alpha=0.85)

#plt.show()