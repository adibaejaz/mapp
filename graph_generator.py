from tools import NUM_VERTICES, NUM_PAIRS
from random import sample, randint


def generate_graph():
    """Function to generate and print a random graph in specified format."""
    graph = {}
    print("EDGES")
    for x in range(NUM_VERTICES):
        print(f"{x}:", end=" ")
        graph.update({x: []})
        randomlist = sample(range(NUM_VERTICES), randint(5, 10))
        for num in randomlist:
          if num != x:
                print(num, end=" ")
                graph[x].append(num)
                if num > 99:
                    print("BAD NUM!!")
        print("")

    return graph

def generate_pairs(graph):

    print("PAIRS")
    paths = []
    rand_srcs = sample(range(NUM_VERTICES), NUM_PAIRS)
    print(rand_srcs)
    rand_lens = [randint(1, 10) for x in range(NUM_PAIRS)]
    used = [False] * NUM_VERTICES
    for src in rand_srcs:
        used[src] = True

    for x in range(NUM_PAIRS):
        src = rand_srcs[x]
        len = rand_lens[x]
        path = [src]
        while len > 0:
            for v in graph[src]:
                if not used[v]:
                    path.append(v)
                    used[v] = True
                    len -= 1
                    break
            src = v
        print(f"{path[0]} {path[-1]}")
        paths.append(path)

    print("SOLUTIONS")
    for path in paths:
        print(path)



graph = generate_graph()
generate_pairs(graph)
