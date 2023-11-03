# Hill Climbing
import math
import random

def objective_function(x):
    return -x * x

def hill_climbing(initial_x, step_size, max_iterations):
    current_x = initial_x
    current_objective = objective_function(current_x)

    for iteration in range(max_iterations):
        neighbor_x = current_x + step_size
        neighbor_objective = objective_function(neighbor_x)

        if neighbor_objective > current_objective:
            current_x = neighbor_x
            current_objective = neighbor_objective
        else:
            break

    return current_x


initial_x = 2.0
step_size = 0.1
max_iterations = 100

result = hill_climbing(initial_x, step_size, max_iterations)

print("Optimal solution:", result)
print("Objective value:", objective_function(result))

# Simulated Anealing
import math
import random
import time

def objective_function(x):
    return x * x

def simulated_annealing(initial_x, initial_temperature, cooling_rate, max_iterations):
    current_x = initial_x
    best_x = current_x
    current_objective = objective_function(current_x)
    best_objective = current_objective

    random.seed(int(time.time()))  

    for iteration in range(max_iterations):
        candidate_x = current_x + (random.uniform(-1, 1) * 2.0)  
        candidate_objective = objective_function(candidate_x)

        acceptance_probability = math.exp((current_objective - candidate_objective) / initial_temperature)

        if candidate_objective < current_objective or random.random() < acceptance_probability:
            current_x = candidate_x
            current_objective = candidate_objective

            if current_objective < best_objective:
                best_x = current_x
                best_objective = current_objective

        initial_temperature *= 1.0 - cooling_rate

    return best_x


initial_x = 5.0
initial_temperature = 100.0
cooling_rate = 0.003
max_iterations = 10000

result = simulated_annealing(initial_x, initial_temperature, cooling_rate, max_iterations)

print("Optimal solution:", result)
print("Objective value:", objective_function(result))