#create list of  tuples
tup = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]

#sorts the tupples based on the second element of each tuple 
tup.sort(key=lambda x: x[1])

selected = [] #empty list to store tuples 
last = 0 #keep track of last element 


for x, y in tup: #loop through each tupple first and second key 
    if x >= last: #if first is greater than the last element we iterated through 
        selected.append((x, y)) #add the tuple to the the list 
        last = y


print(selected) #print the list 
