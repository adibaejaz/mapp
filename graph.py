from tools import NUM_VERTICES

class Graph:

    def __init__(self, nodes):
        # Store the adjacency list as a dictionary
        # 0 : { 1, 2 }
        # 1 : { 3, 4 }
        self.adjlist = {}
        for x in range(nodes):
            self.adjlist[x] = []
        self.nodes = nodes

    def add_edge(self, src, dst):
        self.adjlist[int(src)].append(dst)

    def display_adjlist(self) :
        for item in self.adjlist.items() :
            print(f"{item[0]}: {item[1]},")