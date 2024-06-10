import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_graph_with_min_cuts(num_nodes, min_cuts):
    # Create a random graph
    G = nx.gnm_random_graph(num_nodes, num_nodes * 2)

    # Assign random capacities to edges
    for (u, v) in G.edges():
        G[u][v]['capacity'] = random.randint(1, 10)

    # Ensure the graph has the desired number of minimum cuts
    while True:
        min_cut_value, partition = nx.minimum_cut(G, 0, num_nodes - 1)
        if min_cut_value >= min_cuts:
            break
        # Add a new edge to increase the min cut value
        u, v = random.sample(range(num_nodes), 2)
        if not G.has_edge(u, v):
            G.add_edge(u, v, capacity=random.randint(1, 10))

    return G

def draw_graph(G):
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): f"{d['capacity']}" for u, v, d in G.edges(data=True)}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))
    min_cuts = int(input("Enter the minimum number of cuts: "))

    G = generate_graph_with_min_cuts(num_nodes, min_cuts)
    draw_graph(G)

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))
    min_cuts = int(input("Enter the minimum number of cuts: "))

    G = generate_graph_with_min_cuts(num_nodes, min_cuts)
    draw_graph(G)
