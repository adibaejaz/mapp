from tools import djikstra, find_path

def greedy(graph, pairs):

    # permuted_pairs =
    return fixed_greedy(graph, pairs)


def fixed_greedy(graph, pairs):

    soln = []
    residual = graph
    endpts = []
    for pair in pairs:
        endpts.append(pair[0])
        endpts.append(pair[1])

    for pair in pairs:
        path = find_path(graph, pair, endpts)
        if path:
            soln.append(path)
            residual = compute_residual(residual, path)
            print(pair, "success")
        else:
            print(pair, "failed")

    return soln


def permute_sources(pairs):

    pass


def compute_residual(graph, used_v):

    residual = graph
    used_dict = {}
    for v in used_v:
        del residual.adjlist[v]
        used_dict[v] = True

    for v, adj in graph.adjlist.items():
        new_adj = []
        for u in adj:
            if not used_dict.get(u):
                new_adj.append(u)
        residual.adjlist[v] = new_adj

    return residual



