data = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

rows = len(data)

averages = []
for col in range(len(data[0])):
    column_sum = 0
    for row in range(rows):
        column_sum += data[row][col]
    averages.append(column_sum / rows)

print(averages)

