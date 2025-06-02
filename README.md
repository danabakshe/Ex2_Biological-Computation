# Ex2_Biological-Computation
Motif Analysis in Directed Graphs – Assignment 2
Biological Computation – Python Implementation

---

Overview

This project implements a two-part system for motif analysis in directed graphs. The goal is to:
1. Generate all non-isomorphic, weakly connected directed graphs of size `n` (motifs).
2. Count how many times each motif appears as a subgraph in a larger input graph.

---

Part 1 – Motif Generation

Given a number `n`, the program generates all directed graphs with:
- Exactly `n` nodes
- No self-loops
- Weak connectivity
- Non-isomorphic structures (duplicates filtered using isomorphism tests)

Each unique motif is saved to a file:
motifs_n=<n>.txt

Each motif includes:
#<index>
u v  (one line per edge)

---

Part 2 – Motif Counting

Given:
- A large directed graph (in input_graph.txt)
- A motif file (from Part 1)

The program counts how many subgraphs of size `n` in the input graph match each motif (based on isomorphism).

The output is written to:
motif_counts_output.txt

Format:
#<index>
count=<number of appearances>
u v
...

---

How to Run

1. Install Dependencies
pip install networkx

Also make sure to import these standard libraries in your code:
- from itertools import combinations
- import time

2. Generate Motifs
from motif_generator import generate_all_connected_motifs
generate_all_connected_motifs(n=3)

This will create motifs_n=3.txt

3. Count Motif Instances
from motif_counter import count_motif_instances
count_motif_instances("input_graph.txt", "motifs_n=3.txt", "motif_counts_output.txt")

---

File Structure

- ex1_a.py – Code for generating motifs
- ex1_b.py – Code for counting motif occurrences
- input_graph.txt – Input graph (edge list format)
- motifs_n=1.txt to motifs_n=4.txt – Generated motifs
- motif_counts_output.txt – Final output
