# TSP
import numpy as np
import random
import time

num_cities = 5

city_coordinates = [
    (0, 0),
    (1, 2),
    (2, 4),
    (3, 1),
    (4, 3)
]

def create_population(num_individuals, num_cities):
    population = []
    for _ in range(num_individuals):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population
    
def calculate_total_distance(route, coordinates):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        x1, y1 = coordinates[city1]
        x2, y2 = coordinates[city2]
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total_distance += distance
    return total_distance
    
population_size = 100
generations = 1000
mutation_rate = 0.01
start_time = time.time()

population = create_population(population_size, num_cities)

for generation in range(generations):
    fitness_scores = [1 / calculate_total_distance(individual, city_coordinates) for individual in
population]
    selected_indices = np.random.choice(range(population_size), size=population_size,
p=fitness_scores / sum(fitness_scores))
selected_population = [population[i] for i in selected_indices]
new_population = []

while len(new_population) < population_size:
    parent1, parent2 = random.sample(selected_population, 2)
    crossover_point = random.randint(1, num_cities - 1)
    child = parent1[:crossover_point] + [city for city in parent2 if city not in
    parent1[:crossover_point]]
    new_population.append(child)
    
for i in range(population_size):
    if random.random() < mutation_rate:
        swap_indices = random.sample(range(num_cities), 2)
        new_population[i][swap_indices[0]], new_population[i][swap_indices[1]] = new_population[i][swap_indices[1]], new_population[i][swap_indices[0]]
        
population = new_population

best_route = min(population, key=lambda x: calculate_total_distance(x, city_coordinates))
best_distance = calculate_total_distance(best_route, city_coordinates)

end_time = time.time()
execution_time = end_time - start_time

print("Best route:", best_route)
print("Best distance:", round(best_distance, 2))
print("Execution time:", round(execution_time, 2), "seconds")

# String Generation
import random 

POPULATION_SIZE = 100

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

TARGET = "yash"

class Individual(object): 
	def __init__(self, chromosome): 
		self.chromosome = chromosome 
		self.fitness = self.cal_fitness() 

	@classmethod
	def mutated_genes(self): 
		global GENES 
		gene = random.choice(GENES) 
		return gene 

	@classmethod
	def create_gnome(self): 
		global TARGET 
		gnome_len = len(TARGET) 
		return [self.mutated_genes() for _ in range(gnome_len)] 

	def mate(self, par2): 
		child_chromosome = [] 
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):	 

			prob = random.random() 

			if prob < 0.45: 
				child_chromosome.append(gp1) 
			elif prob < 0.90: 
				child_chromosome.append(gp2) 
			else: 
				child_chromosome.append(self.mutated_genes()) 

		return Individual(child_chromosome) 

	def cal_fitness(self): 
		global TARGET 
		fitness = 0
		for gs, gt in zip(self.chromosome, TARGET): 
			if gs != gt: fitness+= 1
		return fitness 

def main(): 
	global POPULATION_SIZE 

	generation = 1

	found = False
	population = [] 

	for _ in range(POPULATION_SIZE): 
				gnome = Individual.create_gnome() 
				population.append(Individual(gnome)) 

	while not found: 
		population = sorted(population, key = lambda x:x.fitness) 
		
		if population[0].fitness <= 0: 
			found = True
			break

		new_generation = [] 

		s = int((10*POPULATION_SIZE)/100) 
		new_generation.extend(population[:s]) 

		s = int((90*POPULATION_SIZE)/100) 
		for _ in range(s): 
			parent1 = random.choice(population[:50]) 
			parent2 = random.choice(population[:50]) 
			child = parent1.mate(parent2) 
			new_generation.append(child) 

		population = new_generation 

		print("Generation: {}\tString: {}\tFitness: {}".
			format(generation, 
			"".join(population[0].chromosome), 
			population[0].fitness)) 

		generation += 1

	print("Generation: {}\tString: {}\tFitness: {}".
		format(generation, 
		"".join(population[0].chromosome), 
		population[0].fitness)) 

main()