def DFS(graph, source):
    stack=[source]
    while len(stack)>0:
        top=stack.pop()
        print(top)
        for neighbor in graph[top]:
            stack.append(neighbor)

def BFS(graph, source):
    queue=[source]
    while len(queue)>0:
        top=queue.pop(0)
        print(top)
        for neighbor in graph[top]:
            queue.append(neighbor)

#Has Path        
def hasPathDFS(graph, src, dest):
    if src==dest:
        return True
    for node in graph[src]:
        if hasPathDFS(graph, node, dest) == True:
            return True
    return False

def hasPathBFS(graph, src, dest):
    queue=[src]
    while len(queue)>0:
        current= queue.pop(0)
        if current ==  dest:
            return True
        for node in graph[current]:
            queue.append(node)
    return False

def buildgraph(edges):
    graph = dict()
    for edge in edges:
        a,b =edge
        if a not in graph:
            graph[a]=[]
        if b not in graph:
            graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def undirectedPath(edges, nodeA, nodeB):
    graph = buildgraph(edges)
    return hasPathCycles(graph, nodeA, nodeB, set())

def hasPathCycles(graph, src, dst, visited):
    if src==dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for node in graph[src]:
        if hasPathCycles(graph, node, dst, visited)==True:
            return True

if __name__ == '__main__':
    graph = {
        'a':['b','c'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'e':[],
        'f':[]
    }
    edges = [
        ['i','j'],
        ['k','i'],
        ['m','k'],
        ['k','l'],
        ['o','n']
    ]
    # DFS(graph, 'a')
    # BFS(graph, 'a')
    # print(hasPathDFS(graph, 'a', 'd'))
    # print(hasPathBFS(graph, 'a', 'd'))
    # print(undirectedPath(edges, 'i','m'))
    print(buildgraph())