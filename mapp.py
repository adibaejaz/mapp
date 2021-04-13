from sys import argv
from greedy import greedy
from graph import Graph
from tools import NUM_VERTICES, NUM_PAIRS
# from planar import planar

def main():

    if len(argv) != 2:
        raise ValueError("enter command: python mapp.py <input file name>")

    input_file = argv[1]
    graph, pairs = build_graph(input_file)

    for v, adj in graph.adjlist.items():
        print(v, ":", adj)

    # if is_planar(graph):
    #   return planar(graph, pairs)

    print(greedy(graph, pairs))

def build_graph(input_file):
    pairs = []
    graph = Graph(100)

    f = open(input_file, "r")
    f.readline()

    while(True):
        line = f.readline().strip().split(" ")
        if line[0] == "PAIRS":
            break
        src = line[0][:-1]
        for x in range(1, len(line)):
            graph.add_edge(src, int(line[x]))

    while(True):
        line = f.readline()
        line = line.strip().split(" ")
        if not line or line[0] == "SOLUTIONS":
            break
        pairs.append((int(line[0]), int(line[1])))

    return graph, pairs

# graph structure from https://algotree.org/algorithms/data_structures/graph_as_adjacency_list_python/
# adjacency list representation

main()

"""MULTI-START GREEDY APPROACH"""
