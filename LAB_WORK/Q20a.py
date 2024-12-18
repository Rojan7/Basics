import networkx as nx
import matplotlib.pyplot as plt

# Define the graph as an adjacency list
graph = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f'],
    'd': ['g'],
    'e': ['h'],
    'f': [],
    'g': [],
    'h': []
}

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Configure plot size
plt.figure(figsize=(10, 8))

# Generate positions for the graph nodes
pos = nx.spring_layout(G, seed=42)  # Seed ensures consistent layout

# Draw nodes with specific styles
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="lightblue", edgecolors="black")

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color="gray", width=1.5)

# Add labels to the nodes
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold", font_color="black")

# Add edge labels (optional, shows connections explicitly)
edge_labels = {(u, v): f"{u}→{v}" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.5)

# Add title and adjust margins
plt.title("Structured Visualization of the Graph", fontsize=16, fontweight="bold")
plt.tight_layout()

# Show the graph
plt.show()
