def f_in_xk(k: int):
    return values[item][k][1]


def divided_difference(va: list, order):
    if order >= 1:
        return (divided_difference(va[1:], order - 1) - divided_difference(va[:-1], order - 1)) / (values[item][va[-1]][0] - values[item][va[0]][0])
    else:
        return f_in_xk(va[0])


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
    sum = 0

    x = correct_value[0]

    for i in range(0, points_count):
        v = []
        for j in range(0, i + 1):
            v.append(j)

        temp_sum = divided_difference(v, i)

        for j in range(0, i):
            temp_sum *= (x - values[item][j][0])

        sum += temp_sum

    obtained_values.append(sum)

for v in range(len(obtained_values)):
    print(f"{v}: {obtained_values[v]}")

    rel_diff = abs(correct_value[1] - obtained_values[v]) / correct_value[1]
    print(f"   rel difference = {rel_diff}")

    abs_diff = abs(correct_value[1] - obtained_values[v])
    print(f"   abs difference = {abs_diff}")
