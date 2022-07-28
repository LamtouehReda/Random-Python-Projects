import random, numpy as np
import matplotlib.pyplot as plt

from deap import base
from deap import creator
from deap import tools

no_of_generations = 100

population_size = 300

size_of_individual = 100

probability_of_mutation = 0.05

tournSel_k = 10

no_of_variables = 2

bounds = [(-2, 2), (-2, 2)]

CXPB, MUTPB = 0.5, 0.2

creator.create("FitnessMin", base.Fitness, weights=(1.0,))

creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)

toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, size_of_individual)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def decode_all_x(individual, no_of_variables, bounds):
    len_chromosome = len(individual)
    len_chromosome_one_var = int(len_chromosome / no_of_variables)
    bound_index = 0
    x = []

    for i in range(0, len_chromosome, len_chromosome_one_var):
        chromosome_string = ''.join((str(xi) for xi in individual[i:i + len_chromosome_one_var]))
        binary_to_decimal = int(chromosome_string, 2)

        lb = bounds[bound_index][0]
        ub = bounds[bound_index][1]
        precision = (ub - lb) / ((2 ** len_chromosome_one_var) - 1)
        decoded = (binary_to_decimal * precision) + lb
        x.append(decoded)
        bound_index += 1

    return x


def objective_fxn(individual):
    x = decode_all_x(individual, no_of_variables, bounds)

    decoded_x = x[0]
    decoded_y = x[1]

    obj_function_value = decoded_x + decoded_y

    return [obj_function_value]


def check_feasiblity(individual):
    var_list = decode_all_x(individual, no_of_variables, bounds)
    if sum(var_list) < 0:
        return True
    else:
        return False


def penalty_fxn(individual):
    x = decode_all_x(individual, no_of_variables, bounds)
    decoded_x = x[0]
    decoded_y = x[1]
    return (x[0]**2+x[1]**2)-2


# registering objetive function with constraint
toolbox.register("evaluate", objective_fxn)  # privide the objective function here
toolbox.decorate("evaluate",
                 tools.DeltaPenalty(check_feasiblity, 1000, penalty_fxn))  # constraint on our objective function

# registering basic processes using bulit in functions in DEAP
toolbox.register("mate", tools.cxTwoPoint)  # strategy for crossover, this classic two point crossover
toolbox.register("mutate", tools.mutFlipBit,
                 indpb=probability_of_mutation)  # mutation strategy with probability of mutation
toolbox.register("select", tools.selTournament, tournsize=tournSel_k)  # selection startegy

hall_of_fame = tools.HallOfFame(1)

stats = tools.Statistics()

stats.register('Min', np.min)
stats.register('Max', np.max)
stats.register('Avg', np.mean)
stats.register('Std', np.std)

logbook = tools.Logbook()

pop = toolbox.population(n=population_size)

fitnesses = list(map(toolbox.evaluate, pop))

for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

g = 0

hall_of_fame.clear()

while g < no_of_generations:

    g = g + 1

    offspring = toolbox.select(pop, len(pop))

    offspring = list(map(toolbox.clone, offspring))

    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < CXPB:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    this_gen_fitness = []  # this list will have fitness value of all the offspring
    for ind in offspring:
        this_gen_fitness.append(ind.fitness.values[0])

    hall_of_fame.update(offspring)

    stats_of_this_gen = stats.compile(this_gen_fitness)

    # creating a key with generation number
    stats_of_this_gen['Generation'] = g

    # printing for each generation
    print(stats_of_this_gen)

    logbook.append(stats_of_this_gen)

    pop[:] = offspring

# print the best solution using HallOfFame object
for best_indi in hall_of_fame:
    # using values to return the value and
    # not a deap.creator.FitnessMin object
    best_obj_val_overall = best_indi.fitness.values[0]
    print('Minimum value for function: ', best_obj_val_overall)
    print('Optimum Solution: ', decode_all_x(best_indi, no_of_variables, bounds))