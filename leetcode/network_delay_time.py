import heapq
from collections import defaultdict

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2 # start

dist = defaultdict(int)     # cost
graph = defaultdict(list)   # connection

Q = [(0, k)]

for u, v, w in times:
    graph[u].append((v, w)) # cost(w) from u to v

while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]: # nearby nodes
            heapq.heappush(Q, (time + w, v)) # (cost, node) => cost = priority criteria

if len(dist) == n:
    print(max(dist.values()))
else:
    print(-1)


