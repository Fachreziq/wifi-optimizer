import math

def calculate_coverage(width, height, routers, radius):
    covered = 0
    total = width * height

    for x in range(width):
        for y in range(height):

            for rx, ry in routers:

                distance = math.sqrt(
                    (x - rx) ** 2 +
                    (y - ry) ** 2
                )

                if distance <= radius:
                    covered += 1
                    break

    return (covered / total) * 100