import networkx as nx
from itertools import combinations, product
import os

def generate_all_directed_graphs(n):
    nodes = list(range(1, n + 1))
    all_possible_edges = [(i, j) for i in nodes for j in nodes if i != j]

    all_graphs = []
    for k in range(1, len(all_possible_edges) + 1):
        for edges in combinations(all_possible_edges, k):
            G = nx.DiGraph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)
            all_graphs.append(G)
    return all_graphs

def is_new_graph(graph, graph_list):
    for existing in graph_list:
        if nx.is_isomorphic(graph, existing):
            return False
    return True

def generate_connected_unique_graphs(n):
    all_graphs = generate_all_directed_graphs(n)
    unique_connected = []
    for g in all_graphs:
        if nx.is_weakly_connected(g) and is_new_graph(g, unique_connected):
            unique_connected.append(g)
    return unique_connected

def save_graphs_to_file(graphs, n, filename="motifs_output.txt"):
    with open(filename, "w") as f:
        f.write(f"n={n}\n")
        f.write(f"count={len(graphs)}\n")
        for i, g in enumerate(graphs, 1):
            f.write(f"# {i}\n")
            for u, v in g.edges():
                f.write(f"{u} {v}\n")

#example n=2
if __name__ == "__main__":
    n = 6
    motifs = generate_connected_unique_graphs(n)
    save_graphs_to_file(motifs, n)
    print(f"Saved {len(motifs)} connected motifs for n={n} to file.")
