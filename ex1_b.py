import networkx as nx
from itertools import combinations
import time


def generate_all_directed_graphs(n):
    """
    Generate all possible directed graphs with n nodes and all edge combinations.
    """
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
    """
    Check if the graph is isomorphic to any graph already in the list.
    """
    for existing in graph_list:
        if nx.is_isomorphic(graph, existing):
            return False
    return True

def generate_connected_unique_graphs(n):
    """
    Generate all connected and non-isomorphic directed graphs with n nodes.
    """
    all_graphs = generate_all_directed_graphs(n)
    unique_connected = []
    for g in all_graphs:
        if nx.is_weakly_connected(g) and is_new_graph(g, unique_connected):
            unique_connected.append(g)
    return unique_connected

def save_graphs_to_file(graphs, n):
    """
    Save the list of graphs in the required textual format to a flat file.
    """
    filename = f"motifs_n={n}.txt"
    with open(filename, "w") as f:
        f.write(f"n={n}\n")
        f.write(f"count={len(graphs)}\n")
        for i, g in enumerate(graphs, 1):
            f.write(f"# {i}\n")
            for u, v in g.edges():
                f.write(f"{u} {v}\n")
    print(f"Saved {len(graphs)} motifs to {filename}")
    return filename

def main():
    for n in range(1, 4):
        print(f"Generating motifs for n={n}...")
        start = time.time()
        motifs = generate_connected_unique_graphs(n)
        end = time.time()
        print(f"n={n}, number of motifs: {len(motifs)}, runtime: {end - start:.2f} seconds")
        save_graphs_to_file(motifs, n)

if __name__ == "__main__":
    main()
