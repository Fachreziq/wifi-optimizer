from algorithms.hill_climbing import hill_climbing

routers, score = hill_climbing(
    20,
    20,
    3,
    5
)

print(score)
print(routers)