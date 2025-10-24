def algo1(arr):
    n = len(arr)
    half = n // 2
    
    selected_right = []
    selected_left = []
    
    last = arr[-1]
    first = arr[0]
    
    for i in range(len(arr)):
        if arr[i] >= first:
            selected_left.append(i)
            first = arr[i]
            

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= last:
            selected_right.append(i)
            last = arr[i]
            

    
    return selected_left, selected_right
    
    
arr = [3, 7, 8, 3, 6, 1]
left, right = algo1(arr)
print(left)
print(right)
