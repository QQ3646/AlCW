from math import exp


# You can look at the function: https://www.desmos.com/calculator/pgc4nubqnk
def function(x: float):
    return 4 - exp(x) - 2 * x ** 2


real_root = 0.88677

# [a, b] = [5, 10]
interval = [0, 2]

abs_precision = 0.001

if function(interval[0]) * function(interval[1]) >= 0:
    print("There are no roots here. Well, or a multiple of them.")
    exit(0)

iter_counter = 0
while abs(function((interval[1] + interval[0]) / 2)) > abs_precision:
    midpoint = (interval[1] + interval[0]) / 2
    if function(interval[0]) * function(midpoint) <= 0:
        interval[1] = midpoint
    else:
        interval[0] = midpoint
    iter_counter += 1

print(f"root = {(interval[1] + interval[0]) / 2}")
print(f"function value = {function((interval[1] + interval[0]) / 2)}")
print(f"iteration counter = {iter_counter}")
