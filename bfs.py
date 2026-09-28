from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))
        z = state.index(0)
        r, c = divmod(z, 3)

        for x in [z-3, z+3, z-1, z+1]:
            if 0 <= x < 9 and abs(x-z) in [1, 3]:
                new = state.copy()
                new[z], new[x] = new[x], new[z]
                queue.append((new, path + [state]))

    return None


print("Enter puzzle (0 for blank):")
start = []

for i in range(3):
    start += list(map(int, input().split()))

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

ans = bfs(start, goal)

if ans:
    for s in ans:
        print(s[:3])
        print(s[3:6])
        print(s[6:])
        print()
else:
    print("No solution")