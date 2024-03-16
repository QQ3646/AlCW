from math import factorial

def f_in_xk(k: int):
    return values[item][k][1]


def finite_difference(k: int, order: int):
    if order > 1:
        return finite_difference(k + 1, order - 1) - finite_difference(k, order - 1)
    elif order == 1:
        return f_in_xk(k + 1) - f_in_xk(k)
    else:
        return f_in_xk(k)


# Значения из пунктов a) и b)
# Вида [(x1, y1), (x2, y2), ..., (xN, yN)]
values = {
    'a': [(1, 0), (2, 0.3010), (4, 0.6021), (6, 0.7782), (8, 0.9031)],
    'b': [(2, 0.3010), (4, 0.6021), (6, 0.7782), (8, 0.9031), (10, 1)],
    'c': [(3, 0.4771), (4, 0.6021), (5, 0.6990), (6, 0.7782), (7, 0.8451)]
}

correct_value = (5.25, 0.7202)

obtained_values = []

# Change this
items = ['a', 'b', 'c']

for item in items:
    points_count = len(values[item])

    # h = x2 - x1
    h = values[item][1][0] - values[item][0][0]
    sum = 0

    # q = (x - x0) / h
    q = lambda x: (x - values[item][0][0]) / h
    x = correct_value[0]

    for i in range(0, points_count):
        temp_sum = finite_difference(0, i)

        for j in range(0, i):
            temp_sum *= q(x) - j

        temp_sum /= factorial(i)

        sum += temp_sum

    obtained_values.append(sum)

for v in range(len(obtained_values)):
    print(f"{v}: {obtained_values[v]}")

    rel_diff = abs(correct_value[1] - obtained_values[v]) / correct_value[1]
    print(f"   rel difference = {rel_diff}")

    abs_diff = abs(correct_value[1] - obtained_values[v])
    print(f"   abs difference = {abs_diff}")
