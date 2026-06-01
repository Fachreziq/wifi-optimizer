import random

from algorithms.fitness import calculate_coverage

POPULATION_SIZE = 20

GENERATIONS = 50

def create_individual(
        width,
        height,
        num_routers):

    return [

        (
            random.randint(0,width-1),
            random.randint(0,height-1)
        )

        for _ in range(num_routers)
    ]

def genetic_algorithm(
        width,
        height,
        num_routers,
        radius):

    population = [

        create_individual(
            width,
            height,
            num_routers
        )

        for _ in range(POPULATION_SIZE)
    ]

    for _ in range(GENERATIONS):

        population.sort(

            key=lambda x:
            calculate_coverage(
                width,
                height,
                x,
                radius
            ),

            reverse=True
        )

        parent1 = population[0]
        parent2 = population[1]

        child = []

        for i in range(num_routers):

            child.append(

                random.choice(
                    [
                        parent1[i],
                        parent2[i]
                    ]
                )
            )

        mutate = random.randint(
            0,
            num_routers-1
        )

        child[mutate] = (
            random.randint(0,width-1),
            random.randint(0,height-1)
        )

        population[-1] = child

    best = population[0]

    score = calculate_coverage(
        width,
        height,
        best,
        radius
    )

    return best, score