# Значения из пунктов a) и b)
# Вида [(x1, y1), (x2, y2), ..., (xN, yN)]
values = {
    'a': [(0, 1), (0.1, 1.10517), (0.2, 1.22140), (0.3, 1.34986)],
    'b': [(0.1, 1.10517), (0.2, 1.22140), (0.3, 1.34986)]
}

correct_value = (0.15, 1.16183)

obtained_values = []

# Change this
items = ['a', 'b']

for item in items:
    points_count = len(values[item])
    coeff_list = []
    another_list = []
    for i in range(0, points_count):
        inner_coeff_list = []
        inner_another_list = []

        inner_range = list(range(points_count))
        inner_range.remove(i)
        for j in inner_range:
            inner_coeff_list.append(1 / (values[item][i][0] - values[item][j][0]))
            inner_another_list.append(values[item][j][0] / (values[item][i][0] - values[item][j][0]))

        coeff_list.append(inner_coeff_list)
        another_list.append(inner_another_list)

    x = correct_value[0]
    value = 0
    for i in range(0, points_count):
        temp_value = values[item][i][1]
        for j in range(0, points_count - 1):
            temp_value *= x * coeff_list[i][j] - another_list[i][j]
        value += temp_value

    obtained_values.append(value)

for v in range(len(obtained_values)):
    print(f"{v}: {obtained_values[v]}")

    rel_diff = abs(correct_value[1] - obtained_values[v]) / correct_value[1]
    print(f"   rel difference = {rel_diff}")

    abs_diff = abs(correct_value[1] - obtained_values[v])
    print(f"   abs difference = {abs_diff}")
