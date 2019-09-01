def bubbleSort(input_array):
    n = len(input_array)
    for i in range(n):
        swap = 0 ##to break the loop early if it gets sorted. 
        for j in range(n-1):
            if(input_array[j]>input_array[j+1]):
                temp = input_array[j]
                input_array[j] = input_array[j+1]
                input_array[j+1] = temp
                swap =1
        if(swap == 0):
            break
    

input_array = [5,4,3,2,1]
bubbleSort(input_array)
print(input_array)