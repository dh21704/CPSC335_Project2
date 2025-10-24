def algo1(arr):
    n = len(arr)
    half = n // 2
    l = arr[:half]
    r = arr[half:]
    return l, r


def solve_right(arr):
    last = arr[-1]
    selected = []
    for val in reversed(arr):
        if val >= last:
            selected.append(val)
            last = val
    return selected

def solve_left(arr):
    first = arr[0]
    selected = []
    for i in arr:
        if i >= first:
            selected.append(i)
            first = i 

arr = [3, 7, 8, 3, 6, 1]
left, right = algo1(arr)
print('left:', left)
print('right:', right)

visible_right = solve_right(right)
visible_left = solve_left(left)
print('visible_right:', visible_right)
