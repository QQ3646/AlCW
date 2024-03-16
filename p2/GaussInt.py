from math import sin, cos


# You can look at the function: https://www.desmos.com/calculator/ga82otgf7b
def function(x: float):
    return sin(x) * x / 10 * cos(3 * x - 1)


# Calculated by WolframAlpha, you can calculate it yourself
# Integrate[sin(x)*x/10*cos(3x-1),{x,5,10}]
exact_value = 0.395352619620603

data = {
    '2': [[-0.5773503, 0.5773503], [1, 1]],
    '3': [[-0.7745967, 0, 0.7745967], [0.5555556, 0.8888889, 0.5555556]],
    '5': [[-0.9061798, -0.5384693, 0, 0.5384693, 0.9061798], [0.4786287, 0.2369269, 0.5688888, 0.2369269, 0.4786287]]
}

# [a, b] = [5, 10]
interval = (5, 10)

# Change this
items = ['2', '3', '5']

obtained_values = []
for item in items:
    sum = 0
    for i in range(0, int(item)):
        sum += (interval[1] - interval[0]) / 2 * data[item][1][i] * function((interval[1] - interval[0]) / 2 * data[item][0][i] + (interval[0] + interval[1]) / 2)
    obtained_values.append(sum)

for v in range(len(obtained_values)):
    print(f"{items[v]}: {obtained_values[v]}")

    for i in range(0, int(items[v])):
        print(f"   x{i + 1} = {(interval[1] - interval[0]) / 2 * data[items[v]][0][i] + (interval[0] + interval[1]) / 2}")

    print()
    for i in range(0, int(items[v])):
        print(f"   f(x{i + 1}) = {function((interval[1] - interval[0]) / 2 * data[items[v]][0][i] + (interval[0] + interval[1]) / 2)}")

    print()
    for i in range(0, int(items[v])):
        print(f"   c{i + 1} = {data[items[v]][1][i]}")

    rel_diff = abs(exact_value - obtained_values[v]) / exact_value
    print(f"\n   rel difference = {rel_diff}")

    abs_diff = abs(exact_value - obtained_values[v])
    print(f"   abs difference = {abs_diff}")
