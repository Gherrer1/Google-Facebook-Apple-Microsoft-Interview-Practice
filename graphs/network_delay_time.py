from heapq import heappush, heappop
weighted_edges = [
    (1,2,1),
    (1,4,7),
    (2,1,7),
    (2,6,8),
    (2,7,1),
    (3,2,9),
    (3,4,3),
    (4,2,10),
    (4,7,6),
    (4,5,4),
    (5,1,3),
    (5,3,1),
    (6,5,6),
    (6,4,4),
    (6,7,7),
    (7,1,4),
    (7,3,6)
]

N = 7
K = 7

def network_delay_time(times, n, k):
    graph = { i: [] for i in xrange(1, n + 1) }
    for (start, end, weight) in times:
        graph[start].append((end, weight))
    spt_set = {}
    unvisited_pq = [(0, k)]
    while unvisited_pq:
        dist, node = heappop(unvisited_pq)
        if node in spt_set:
            continue
        spt_set[node] = dist
        for neighbor, weight in graph[node]:
            if neighbor not in spt_set:
                heappush(unvisited_pq, (weight + dist, neighbor))
    if len(spt_set) < N:
        return -1
    return max(spt_set.values())

print network_delay_time(weighted_edges, 7, 7)
