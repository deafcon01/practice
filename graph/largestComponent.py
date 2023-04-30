def largestComponent(graph):
    visited=set()
    largest=0
    for node in graph:
        size = exploreSize(graph, node, visited)
        largest = max(largest, size)
    return largest

def exploreSize(graph, current, visited):
    if current in visited:
        return 0
    size = 1
    visited.add(current)
    for node in graph[current]:
        size += exploreSize(graph, node, visited)
    return size

if __name__ == "__main__":
    graph = {
        0:[8,1,5],
        1:[0],
        5:[0,8],
        8:[0,5],
        2:[3,4],
        3:[2,4],
        4:[3,2]
    }
    print(largestComponent(graph))