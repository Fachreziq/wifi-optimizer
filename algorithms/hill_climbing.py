import random

from algorithms.fitness import calculate_coverage

def hill_climbing(width, height, num_routers, radius):

    current = [
        (
            random.randint(0, width-1),
            random.randint(0, height-1)
        )
        for _ in range(num_routers)
    ]

    current_score = calculate_coverage(
        width,
        height,
        current,
        radius
    )

    for _ in range(500):

        neighbor = current.copy()

        index = random.randint(
            0,
            num_routers-1
        )

        neighbor[index] = (
            random.randint(0, width-1),
            random.randint(0, height-1)
        )

        score = calculate_coverage(
            width,
            height,
            neighbor,
            radius
        )

        if score > current_score:

            current = neighbor
            current_score = score

    return current, current_score