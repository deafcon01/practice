import heapq
from collections import defaultdict
 graph = defaultdict(list)
 v,e= map(int, input().split())
 for i in range(e):
    u,v,w=input().split()
    graph[u].append((v,int(w)))
