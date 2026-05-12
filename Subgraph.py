import networkx as nx

# Graph 1
G1 = nx.Graph()

e1 = int(input("Enter number of edges in Graph 1: "))

for _ in range(e1):
    u, v = input("Enter edge (u v): ").split()
    G1.add_edge(u, v)

# Graph 2
G2 = nx.Graph()

e2 = int(input("\nEnter number of edges in Graph 2: "))

for _ in range(e2):
    u, v = input("Enter edge (u v): ").split()
    G2.add_edge(u, v)

# Subgraph Check
if nx.is_isomorphic(G1, G2.subgraph(G1.nodes())):
    print("\nGraph 1 is a subgraph of Graph 2")
else:
    print("\nGraph 1 is NOT a subgraph of Graph 2")
