
def hill_climbing(x):
    while True:
        current = x
        neighbors = [x - 1, x + 1]

        best = max(neighbors, key=lambda n: -(n - 3) ** 2)

        if -(best - 3) ** 2 <= -(current - 3) ** 2:
            break

        x = best

    return x

result = hill_climbing(0)

print("Best solution:", result)
print("Maximum value:", -(result - 3) ** 2)
