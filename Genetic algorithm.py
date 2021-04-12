""""
EARIN - Introduction to Artificial Intelligence - Exercise #2
Merve Rana Kızıl
Beste Baydur
"""

import numpy as np
import random


def binary_to_integer(signed_bin):
    binary = signed_bin[1:]
    result = int("".join(str(x) for x in binary), 2)
    if signed_bin[0]:
        return -result
    return result


def integer_to_binary(int_num, size):
    if int_num > 0:
        result = [int(x) for x in bin(int_num)[2:]]
        for i in range(size - len(result)):
            result.insert(0, 0)
    else:
        result = [int(x) for x in bin(-int_num)[2:]]
        for i in range(size - len(result) - 1):
            result.insert(0, 0)
        result.insert(0, 1)
    return np.array(result)


dimensions = int(input("Enter dimensions: "))
d = int(input("Enter d: "))
A = []
temp_list = []
print("Enter the elements of matrix A: ")
print("Press enter for each element, row-wise")
for i in range(dimensions):
    for j in range(0, dimensions):
        temp_list.append(float(input()))
    A.append(temp_list)
    temp_list = []


print("Enter the elements of vector b: ")
b = []
for i in range(0, dimensions):
    b.append(float(input()))
b = np.array(b)

c = float(input("Enter c: "))
population_size = int(input("Enter the population size: "))
crossover_prob = float(input("Enter the crossover probability: "))
while crossover_prob < 0 or crossover_prob > 1:
    crossover_prob = float(input("Probability should be between 0 and 1. Enter the crossover probability: "))
mutation_prob = float(input("Enter the mutation probability: "))
while mutation_prob < 0 or mutation_prob > 1:
    mutation_prob = float(input("Probability should be between 0 and 1. Enter the mutation probability: "))
iterations = int(input("Enter number of iterations: "))

"""
dimensions = 3
d = 3
A = [[-2, 1, 0], [1, -2, 1], [0, 1, -2]]
b = [-14, 14, -2]
c = -23.5
population_size = 50
crossover_prob = 0.9
mutation_prob = 0.05
iterations = 1000
"""

f = lambda x: c + np.dot(np.transpose(b), x) + np.dot(np.dot(np.transpose(x), A), x)


def evaluate_generation(population):
    scores = []
    for individual in population:
        int_individual = np.array([binary_to_integer(point) for point in individual])
        scores.append(f(int_individual))
    return scores


def initialize(population_size, dimension, limit):
    population = []
    for i in range(population_size):
        individual = []
        for j in range(dimension):
            random_num = np.random.randint(-2 ** limit + 1, 2 ** limit)
            individual.append(integer_to_binary(random_num, limit + 1))
        population.append(individual)
    return population


def roulette(population_fitness):
    population_fitness = np.array(population_fitness)
    population_fitness_ = (population_fitness - population_fitness.min()) / (
            population_fitness.max() - population_fitness.min())
    selection_prob = population_fitness_ / sum(population_fitness_)
    # if not np.logical_or.reduce(np.isnan(selection_prob)):
    return np.random.choice(len(population_fitness), size=2, p=selection_prob)


def single_point_crossover(a, b, probability):
    if random.random() > probability:
        index_point = np.random.randint(0, len(a))
        index_bit = np.random.randint(len(a[0]))
        tmp = b[index_point][:index_bit].copy()
        b[index_point][:index_bit], a[index_point][:index_bit] = a[index_point][:index_bit], tmp
        return a, b
    else:
        return a, b


def mutation(a, probability):
    for index in range(d):
        for bit in range(d + 1):
            if np.random.rand() < probability:
                a[index][bit] = 1 - a[index][bit]
    return a


def genetic_algorithm(population_size, d, limit, iter, cp, mp):
    population = initialize(population_size, d, limit)
    evaluations = evaluate_generation(population)
    max_idx = np.argsort(evaluations)[-1]
    maximum = evaluations[max_idx]
    optimum_result = population[max_idx]

    for i in range(iter):
        populations = []
        for j in range(int(population_size / 2)):
            a_i, b_i = roulette(evaluations)
            a = population[a_i]
            b = population[b_i]
            a, b = single_point_crossover(a, b, cp)
            a = mutation(a, mp)
            b = mutation(b, mp)
            populations.append(a)
            populations.append(b)

        evaluations = evaluate_generation(populations)
        index = np.argsort(evaluations)[-1]
        maximum_i = evaluations[index]
        result = populations[index]

        if maximum_i > maximum:
            maximum = maximum_i
            optimum_result = result

        # population = populations.copy()

        print("Maximum: ", maximum_i)
        print("Optimum result: ")
        # print(optimum_result)
        print(str([binary_to_integer(maxima) for maxima in optimum_result]))
        print("----------------------------------")


genetic_algorithm(population_size, dimensions, d, iterations, crossover_prob, mutation_prob)




