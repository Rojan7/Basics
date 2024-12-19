# weighted graph in python

import networkx as nx
import matplotlib.pyplot as plt

# Define the graph as an adjacency list
graph = {
    'biratnagar': {'rangeli': 25, 'itahari': 22},
    'rangeli': {'biratnagar': 25, 'kanepokhari': 25},
    'itahari': {'biratnagar': 22,'dharan':20 },
    'biratchowk': {'itahari': 11,'biratnagar':30},
    'kanepokhari': {'biratchowk': 10,'rangeli':25},
    'urlabari' :{'kanepokhari' :12,'damak':6},
    'damak' :{'urlabari':6}

    
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