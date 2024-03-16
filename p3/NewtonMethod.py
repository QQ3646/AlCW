from math import exp

# You can look at the function: https://www.desmos.com/calculator/pgc4nubqnk
def function(x: float):
    return 4 - exp(x) - 2 * x ** 2


def derivative(x: float):
    return -4 * x - exp(x)


real_root = 0.88677

abs_precision = 0.001

point = 2

iter_counter = 0
while abs(function(point)) > abs_precision:
    if -1e-6 < derivative(point) < 1e-6:
        break
    point = point - function(point) / derivative(point)
    iter_counter += 1

print(f"root = {point}")
print(f"function value = {function(point)}")
print(f"iteration counter = {iter_counter}")
