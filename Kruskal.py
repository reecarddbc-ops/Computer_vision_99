import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Input edges
e = int(input("Enter number of edges: "))

for _ in range(e):
    u, v, w = input("Enter edge and weight (u v w): ").split()
    G.add_edge(u, v, weight=int(w))

# Apply Kruskal Algorithm
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

print("\nMinimum Spanning Tree:")

total = 0

for u, v, data in mst.edges(data=True):
    print(u, "-", v, "=", data['weight'])
    total += data['weight']

print("Total Cost:", total)

# ---------------- DRAW ORIGINAL GRAPH ----------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold'
)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Original Graph")

# ---------------- DRAW MST ----------------
plt.subplot(1, 2, 2)

nx.draw(
    mst,
    pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    edge_color='red',
    width=2
)

mst_labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_labels)

plt.title("Kruskal Minimum Spanning Tree")

plt.show()
