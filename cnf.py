
def astar(graph, heuristic, start, goal):
    open_list = [(0, start)]
    g = {start: 0}
    parent = {}

    while open_list:
        open_list.sort()
        f, node = open_list.pop(0)

        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            print("Path:", path[::-1])
            print("Cost:", g[goal])
            return

        for neighbor, cost in graph[node]:
            new_cost = g[node] + cost

            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                parent[neighbor] = node
                open_list.append(
                    (new_cost + heuristic[neighbor], neighbor)
                )

    print("Goal not found")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 6, 'B': 5, 'C': 3,
    'D': 4, 'E': 2, 'G': 0
}

astar(graph, heuristic, 'A', 'G')
