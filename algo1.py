#precondition: recieves a list of integers
def algo1(arr): 
    n = len(arr) #grab length of array 
    half = n // 2 #hafl the array 
    
    #create empty list for left and right 
    selected_right = []
    selected_left = []
    
    #grab first and last element in list 
    last = arr[-1]
    first = arr[0]
    
    #iterate through the list (looking through the left side of the towers)
    for i in range(len(arr)):
        if arr[i] >= first: #if element is greater than the first number
            selected_left.append(i) #add said element to the list 
            first = arr[i] #set new element to the 'tallest' tower now 
            

    for i in range(len(arr) - 1, -1, -1): #iterate through list backwards
        if arr[i] >= last: #if current element is greater than the last element 
            selected_right.append(i) #add current element to the lis t 
            last = arr[i] #last element is now the 'tallest' tower from the right side 
            

    
    return selected_left, selected_right #return both views 
    
    
arr = [3, 7, 8, 3, 6, 1]
left, right = algo1(arr)
print(left)
print(right)
