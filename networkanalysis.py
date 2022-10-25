import networkx as nx
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])
H = nx.path_graph(10)
G.add_nodes_from(H)
# G.add_node(H)
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*
G.add_edges_from([(1, 2), (1, 3)])
# G.add_edges_from(H.edges)
print(list(H.nodes))
print(list(G.nodes))
print(list(H.edges))
print(list(G.edges))

G.clear()
print ("clearing...")
print("list(G.nodes) {}".format(list(G.nodes)))
print("list(G.edges) {}".format(list(G.edges)))

#
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')
print("G.number_of_nodes() {}".format(G.number_of_nodes()))
print("G.number_of_edges() {}".format(G.number_of_edges()))
print("list(G.nodes) {}".format(list(G.nodes)))
print("list(G.edges) {}".format(list(G.edges)))
a = list(G.adj[1])  # or list(G.neighbors(1))
print("list(G.adj[1]) {}".format(a))
d = G.degree[1]  # the number of edges incident to 1
print("G.degree[1] {}".format(d))

#
DG = nx.DiGraph()
DG.add_edge(2, 1)   # adds the nodes in order 2, 1
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)
print("list(DG.successors(2)) {}".format(list(DG.successors(2))))
print("list(DG.edges) {}".format(list(DG.edges)))

#
print("G.edges([2, 'm']) {}".format(G.edges([2, 'm'])))
print("G.degree([2, 3]) {}".format(G.degree([2, 3])))

# removing
G.remove_node(2)
G.remove_nodes_from("spam")
G.remove_edge(1, 3)
print("list(G.nodes) {}".format(list(G.nodes)))
print("list(G.edges) {}".format(list(G.edges)))

#Using the graph constructors
G.add_edge(1, 2)
print("list(G.edges) {}".format(list(G.edges)))
H = nx.DiGraph(G)  # create a DiGraph using the connections from G
print("list(H.edges) {}".format(list(H.edges)))

