
def dls(graph, node, goal, limit):
    if node == goal:
        return True

    if limit <= 0:
        return False

    for child in graph[node]:
        if dls(graph, child, goal, limit - 1):
            return True

    return False


def ids(graph, start, goal):
    for depth in range(10):
        print("Depth limit:", depth)
        if dls(graph, start, goal, depth):
            print("Goal found:", goal)
            return
    print("Goal not found")


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

ids(graph, 'A', 'F')
