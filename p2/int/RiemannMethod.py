from math import sin, cos


# You can look at the function: https://www.desmos.com/calculator/ga82otgf7b
def function(x: float):
    return sin(x) * x / 10 * cos(3 * x - 1)


# Calculated by WolframAlpha, you can calculate it yourself
# Integrate[sin(x)*x/10*cos(3x-1),{x,5,10}]
exact_value = 0.395352619620603

# [a, b] = [5, 10]
interval = (5, 10)

# default value = [20, 50, 100]
grids = [20, 50, 100]

obtained_values = []

for i in range(0, len(grids)):
    sum = 0

    # h = (b - a) / number_of_segments_i
    # number_of_segments_i := grid_i
    h = (interval[1] - interval[0]) / grids[i]
    for j in range(0, grids[i]):
        x_i = interval[0] + h * j
        x_ip1 = interval[0] + h * (j + 1)
        sum += function((x_i + x_ip1) / 2) * (x_ip1 - x_i)
    obtained_values.append(sum)

for v in range(len(obtained_values)):
    print(f"{v}: {obtained_values[v]}")

    rel_diff = abs(exact_value - obtained_values[v]) / exact_value
    print(f"   rel difference = {rel_diff}")

    abs_diff = abs(exact_value - obtained_values[v])
    print(f"   abs difference = {abs_diff}")
