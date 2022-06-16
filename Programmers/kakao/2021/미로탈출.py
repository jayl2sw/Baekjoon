import heapq

def solution(n, start, end, roads, traps):
    def changeDirections(graph, node):
        res = [graph[i][:] for i in range(len(graph))]

        for i in range(n+1):
            res[i][node], res[node][i] = res[node][i], res[i][node]

        return res

    graph = [[-1] * (n+1) for _ in range(n+1)]
    for P, Q, S in roads:
        if graph[P][Q] == -1:
            graph[P][Q] = S
        else:
            graph[P][Q] = min(S, graph[P][Q])

    # print(graph)

    q = []
    heapq.heappush(q, (0, graph, start))
    answer = 9999999
    while q:
        k, current_graph, current_node = heapq.heappop(q)

        if answer <= k:
            continue

        if current_node == end:
            answer = k

        for next_node in range(len(current_graph[current_node])):
            cost = current_graph[current_node][next_node]
            if cost != -1:

                if next_node in traps:
                    next_graph = changeDirections(current_graph, next_node)
                    q.append((k+cost, next_graph, next_node))

                else:
                    q.append((k+cost, current_graph, next_node))

    return answer


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

print(solution(n, start, end, roads, traps))

