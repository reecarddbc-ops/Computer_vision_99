import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Input edges
e = int(input("Enter number of edges: "))

for _ in range(e):
    u, v = input("Enter edge (u v): ").split()
    G.add_edge(u, v)

# ---------------- EULERIAN CIRCUIT CHECK ----------------

if nx.is_eulerian(G):

    print("\nGraph has Eulerian Circuit")

    # Get Eulerian Circuit
    circuit = list(nx.eulerian_circuit(G))

    print("\nEulerian Circuit:")

    for edge in circuit:
        print(edge)

else:
    print("\nGraph does NOT have Eulerian Circuit")

# ---------------- DRAW GRAPH ----------------

plt.figure(figsize=(6, 6))

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2500,
    font_size=12,
    font_weight='bold',
    edge_color='black',
    width=2
)

plt.title("Eulerian Circuit Graph")

plt.show()
