def Prim_matrix(G):
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    visited[0] = True
    MST = []
    taken = 0
    while taken < len(G)-1:
        minimum = inf
        for i in range(len(G)):
            if visited[i]:
                for j in range(len(G)):
                    if not visited[j]:
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
    