def algo1(arr):
    arr.sort()
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
        
        for j in range(half, n):
            r.append(arr[j])
        
        sorted_l = algo1(l)
        sorted_r = algo1(r)
        
        
        
        return sorted_l, sorted_r

def binary_search(left, x):
    return binary_search_range(left, x, 0, len(left))
    
def binary_search_range(v, q, s, e):
    if s == e:
        return None
        
    else:
        half = (s + e) // 2
        if q < v[half]:
            return binary_search_range(v, q, s, half)
        elif q == v[half]:
            return half
        else:
            return binary_search_range(v, q, half+1, e)
        
    
    
    
arr = [3, 7, 8, 3, 6, 1]
left, right = algo1(arr)
print('left: ', left)
print('right: ', right)

x = left[0]


j = binary_search(left, x)

print(j)


    
    
    
    
    
    
    
    
    
