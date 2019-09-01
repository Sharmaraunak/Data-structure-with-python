"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

#swap function
def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

#function to do divide
def sort(array,start,end):
    if(start>= end):
        return
    pIndex = partition(array,start,end)
    sort(array,start,pIndex-1)
    sort(array,pIndex+1,end)


def partition(array,start,end):

    pivot = array[end] 
    pIndex = 0
    for i in range(end):
        if(array[i]<= pivot):
            swap(array,i,pIndex)
            pIndex+=1
    
    swap(array,end,pIndex)
    return pIndex



def quicksort(array):
    start = 0
    end = len(array)-1
    sort(array,start,end)

    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))