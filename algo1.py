def algo1(arr):
    arr.sort()
    n = len(arr)
    print(arr)
    
    if n == 0:
        return None
    
    size_even = 0
    
    if n % 2 == 0:
        size_even = True
    else:
        size_even = False
    
    
    
    
    l = []
    r = []
    
    if (size_even):
        half = n//2
    else:
        half = (n//2) + 1
    
    li = ri = 0
    
    
    
    

arr = [3, 7, 8, 3, 6, 1]
algo1(arr)
