def isMonotonic(array):
    if len(array) <= 1:
        return True
    counter = 0
    for i in range(len(array) - 1):
        if array[i] <= array[i+1]:
            counter += 1
        if array[i] >= array[i+1]:
            counter -= 1
            
    if abs(counter) != len(set(array))-1:
        return False
    else:
        return True

array = [1,2,3,4]
print(isMonotonic(array))
