import networkx as nx
import matplotlib.pyplot as plt

# Create graphs
G1 = nx.Graph()
G2 = nx.Graph()

# ---------------- GRAPH 1 INPUT ----------------
e1 = int(input("Enter edges in Graph 1: "))

for _ in range(e1):
    u, v = input("Enter edge: ").split()
    G1.add_edge(u, v)

# ---------------- GRAPH 2 INPUT ----------------
e2 = int(input("\nEnter edges in Graph 2: "))

for _ in range(e2):
    u, v = input("Enter edge: ").split()
    G2.add_edge(u, v)

# ---------------- ISOMORPHIC CHECK ----------------
if nx.is_isomorphic(G1, G2):
    print("\nGraphs are Isomorphic")
else:
    print("\nGraphs are NOT Isomorphic")

# ---------------- DRAWING ----------------
plt.figure(figsize=(10, 5))

# Graph 1
plt.subplot(1, 2, 1)

pos1 = nx.spring_layout(G1)

nx.draw(
    G1,
    pos1,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold'
)

plt.title("Graph 1")

# Graph 2
plt.subplot(1, 2, 2)

pos2 = nx.spring_layout(G2)

nx.draw(
    G2,
    pos2,
    with_labels=True,
    node_color='lightgreen',
    node_size=2000,
    font_size=12,
    font_weight='bold'
)

plt.title("Graph 2")

# Show graphs
plt.show()
