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

def shortestpath(edges, nodeA, nodeB):
    graph = buildgraph(edges)
    visited= set()
    # store node and distance
    queue = [[nodeA, 0]]
    visited.add(nodeA)
    while len(queue)>0:
        node, distance = queue.pop(0)
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append([neighbor, distance+1])
                visited.add(neighbor)
        return -1
if __name__ == "__main__":
    edges= [
        ['w','x'],
        ['x','y'],
        ['z','y'],
        ['z','v'],
        ['w','v']
    ]
    print(shortestpath(edges, 'w', 'z'))