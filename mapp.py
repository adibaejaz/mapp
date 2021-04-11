from sys import argv
from greedy import greedy
from tools import NUM_VERTICES, NUM_PAIRS
# from planar import planar


def main():

    if len(argv) != 2:
        raise ValueError("enter command: python mapp.py <input file name>")

    input_file = argv[1]
    graph, pairs = build_graph(input_file)

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
        if not line:
            break
        line = line.strip().split(" ")
        pairs.append((int(line[0]), int(line[1])))

    # print(pairs)
    return graph, pairs

# graph structure from https://algotree.org/algorithms/data_structures/graph_as_adjacency_list_python/
# adjacency list representation


class Graph:

    def __init__(self, nodes) :
        # Store the adjacency list as a dictionary
        # 0 : { 1, 2 }
        # 1 : { 3, 4 }
        self.adjlist = {}
        self.nodes = nodes

    def add_edge(self, src, dst):

        if src not in self.adjlist:
            self.adjlist[int(src)] = []

        self.adjlist[int(src)].append(dst)

    def display_adjlist(self) :
        for item in self.adjlist.items() :
            print(f"{item[0]}: {item[1]},")

main()

"""MULTI-START GREEDY APPROACH"""
