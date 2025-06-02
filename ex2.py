import networkx as nx
from itertools import combinations

def load_graph_from_file(filename):
    """
    Load a directed graph from a file containing lines of 'u v'.
    """
    G = nx.DiGraph()
    with open(filename, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            G.add_edge(u, v)
    return G

def load_motifs_from_file(motif_file):
    """
    Load all motifs from a motif file (format as in question 1).
    Returns a list of DiGraph objects.
    """
    motifs = []
    current_edges = []
    with open(motif_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('n=') or line.startswith('count='):
                continue
            elif line.startswith('#'):
                if current_edges:
                    G = nx.DiGraph()
                    G.add_edges_from(current_edges)
                    motifs.append(G)
                    current_edges = []
            else:
                u, v = map(int, line.split())
                current_edges.append((u, v))
        if current_edges:
            G = nx.DiGraph()
            G.add_edges_from(current_edges)
            motifs.append(G)
    return motifs

def count_motif_instances(graph, motifs, n):
    """
    Count how many times each motif of size n appears in the graph.
    """
    counts = [0] * len(motifs)
    for nodes in combinations(graph.nodes, n):
        subgraph = graph.subgraph(nodes).copy()
        if not nx.is_weakly_connected(subgraph):
            continue
        for i, motif in enumerate(motifs):
            if nx.is_isomorphic(subgraph, motif):
                counts[i] += 1
                break  # assume only one matching motif
    return counts

def output_motif_counts(motifs, counts, motif_file, output_file):
    """
    Write output in required format: motif structure + count=m.
    """
    with open(output_file, 'w') as f:
        for i, (motif, count) in enumerate(zip(motifs, counts), 1):
            f.write(f"# {i}\n")
            f.write(f"count={count}\n")
            for u, v in motif.edges():
                f.write(f"{u} {v}\n")

#example
if __name__ == "__main__":
    n = 3  # or any desired size
    motif_file = f"motifs_n={n}.txt"
    input_graph_file = "input_graph.txt"
    output_file = "motif_counts_output.txt"

    graph = load_graph_from_file(input_graph_file)
    motifs = load_motifs_from_file(motif_file)
    counts = count_motif_instances(graph, motifs, n)
    output_motif_counts(motifs, counts, motif_file, output_file)
    print(f"Finished counting motif instances. Output written to: {output_file}")
