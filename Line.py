import networkx as nx
import matplotlib.pyplot as plt

# Create original graph
G = nx.Graph()

# Input edges
e = int(input("Enter number of edges: "))

for _ in range(e):
    u, v = input("Enter edge (u v): ").split()
    G.add_edge(u, v)

# Create Line Graph
L = nx.line_graph(G)

# Print line graph edges
print("\nEdges in Line Graph:")

for edge in L.edges():
    print(edge)

# ---------------- DRAWING ----------------
plt.figure(figsize=(12, 5))

# -------- ORIGINAL GRAPH --------
plt.subplot(1, 2, 1)

pos1 = nx.spring_layout(G)

nx.draw(
    G,
    pos1,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold'
)

plt.title("Original Graph")

# -------- LINE GRAPH --------
plt.subplot(1, 2, 2)

pos2 = nx.spring_layout(L)

nx.draw(
    L,
    pos2,
    with_labels=True,
    node_color='lightgreen',
    node_size=2500,
    font_size=10,
    font_weight='bold'
)

plt.title("Line Graph")

# Show graphs
plt.show()
