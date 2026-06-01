import random
import math

from algorithms.fitness import calculate_coverage

def simulated_annealing(
        width,
        height,
        num_routers,
        radius):

    current = [
        (
            random.randint(0,width-1),
            random.randint(0,height-1)
        )
        for _ in range(num_routers)
    ]

    current_score = calculate_coverage(
        width,
        height,
        current,
        radius
    )

    temperature = 100

    while temperature > 1:

        neighbor = current.copy()

        idx = random.randint(
            0,
            num_routers-1
        )

        neighbor[idx] = (
            random.randint(0,width-1),
            random.randint(0,height-1)
        )

        neighbor_score = calculate_coverage(
            width,
            height,
            neighbor,
            radius
        )

        delta = (
            neighbor_score -
            current_score
        )

        if delta > 0:

            current = neighbor
            current_score = neighbor_score

        else:

            probability = math.exp(
                delta / temperature
            )

            if random.random() < probability:

                current = neighbor
                current_score = neighbor_score

        temperature *= 0.95

    return current, current_score