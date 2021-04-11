from tools import djikstra, find_path

def greedy(graph, pairs):

    return fixed_greedy(graph, pairs)


def fixed_greedy(graph, pairs):

    soln = []
    residual = graph

    for pair in pairs:
        path = find_path(residual, pair)
        if path:
            soln.append(path)
            residual = compute_residual(residual, path)
            print(pair, "success")
        else:
            print(pair, "failed")

    return soln


def permute_sources(pairs):
    return []


def compute_residual(graph, path):

    residual = graph
    path_dict = {}
    for v in path:
        del residual.adjlist[v]
        path_dict[v] = True

    for v, adj in graph.adjlist.items():
        new_adj = []
        for u in adj:
            if not path_dict.get(u):
                new_adj.append(u)
        residual.adjlist[v] = new_adj

    return residual



