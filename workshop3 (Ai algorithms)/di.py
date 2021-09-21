import math
import heapq
def dijkistra(graph,start_node):
    n = len(graph)
    weights = [math.inf]*n
    visited = [False]*n
    path = [None]* n
    queue = []
    weights[start_node] = 0
    heapq.heappush(queue, (0,start_node))
    while len(queue)>0:
        g,u = heapq.heappop(queue)
        visited [u] = True
        for node,weight in graph[u]:
            if not visited[node]:
                f = g + weight
                if f < weights[node]:
                    weights[node] = f
                   
                    path[node] = u
                   
                    heapq.heappush(queue, (f,node))
    return path,weights

G = [
    [(1,3),(2,1)],
    [(0,3),(2,7),(3,5),(4,1)],
    [(0,1),(1,7),(3,2)],
    [(1,5),(2,2),(4,7)],
    [(1,1),(3,7)]
]
p,w = dijkistra(G,2)
print(p,w)




# import math
# import heapq as hq
# def diji(graph,s):
#     n = len(graph)
#     path = [None]*n
#     weights = [math.inf]*n
#     visited = [False]*n
#     queue = []
#     hq.heappush(queue,(0,s))
#     weights[s] = 0
#     while len(queue)>0:
#         g,u = hq.heappop(queue)
#         visited[u] = True
#         for node,weight in graph[u]:
#             if not visited[node]:    
#                 f = g + weight
#                 if f < weights[node]:
#                     weights[node] = f
#                     path[node] = u
#                     hq.heappush(queue,(f,node))
#     return path,weights
