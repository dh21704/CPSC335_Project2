
# sort
tup = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
tup.sort(key=lambda x: x[1])

selected = []
last = 0


for x, y in tup:
    if x >= last:
        selected.append((x, y))
        last = y


print(selected)
