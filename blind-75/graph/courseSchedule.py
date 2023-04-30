from typing import List

from graph.basic import buildgraph, hasPathCycles, hasPathDFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph =  self.buildgraph(prerequisites)
        return self.DFS(graph, source , set())

    def buildgraph(self, edges):
        graph = dict()
        for edge in edges:
            a,b = edge
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph
    