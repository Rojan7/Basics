# weighted graph in python

import networkx as nx
import matplotlib.pyplot as plt

# Define the graph as an adjacency list
graph = {
    'a': {'b': 1, 'c': 2},
    'b': {'d': 3, 'e': 4},
    'c': {'f': 5},
    'd': {'g': 6},
    'e': {'h': 7},
    
}

# Create a weighted graph using NetworkX
G = nx.Graph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# Configure plot size
plt.figure(figsize=(10, 8))

# Generate positions for the graph nodes
pos = nx.spring_layout(G, seed=42)  # Seed ensures consistent layout

# Draw nodes with specific styles
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Add edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.show()