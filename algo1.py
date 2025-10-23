def algo1(arr):
    n = len(arr)
    
    if n <= 1:
        return arr 
        
    else:
        half = n // 2
        
        
        l = []
        r = []
        k = half
        
        for i in range(0, half):
            l.append(arr[i])
        
        
        
        sorted_l = algo1(l)
        sorted_r = algo1(r)
        
        
        
        return sorted_l, sorted_r

arr = [3, 7, 8, 3, 6, 1]
left, right = algo1(arr)

