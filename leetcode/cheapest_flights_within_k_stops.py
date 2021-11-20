import heapq
from collections import defaultdict

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0 # at most stop

dist = defaultdict(int)
graph = defaultdict(list)

for u, v, w in flights:
    graph[u].append((v, w))

Q = [(0, src, k)]
while Q:
    cost, node, k = heapq.heappop(Q) # pop the cheapest path

    if node == dst:
        print(cost)
        exit()

    if node not in dist:
        dist[node] = cost

    if k >= 0: # check if stop more
        for v, w in graph[node]:
            alt = cost + w
            heapq.heappush(Q, (alt, v, k - 1))

print(-1)