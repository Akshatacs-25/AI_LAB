
import random
import math

def objective(x):
    return x * x

def simulated_annealing():
    current = random.randint(-10, 10)
    T = 100
    cooling = 0.95

    while T > 0.1:
        new = current + random.uniform(-1, 1)

        delta = objective(new) - objective(current)

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = new

        T *= cooling

    print("Best solution:", round(current, 4))
    print("Minimum value:", round(objective(current), 4))

simulated_annealing()
