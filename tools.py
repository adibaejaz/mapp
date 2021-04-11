NUM_VERTICES = 100
NUM_PAIRS = 10

def djikstra(graph, pair):
    pass


def find_path(graph, pair, endpts):
    """"
    Function to check if there exists a path for a given source-destination pair
    Adapted from https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/
    """
    src = pair[0]
    dst = pair[1]
    visited = [False] * (NUM_VERTICES + 1)
    prev = [None] * (NUM_VERTICES + 1)
    queue = [src]
    visited[src] = True

    while queue:
        v = queue.pop(0)
        if v == dst:
            path = [dst]
            while prev[v]:
                path.append(prev[v])
                v = prev[v]
            path.reverse()
            return path
        elif v != src and v in endpts:
            continue

        for u in graph.adjlist[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
                prev[u] = v

    return None






