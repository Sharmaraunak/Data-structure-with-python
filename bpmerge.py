'''bottomup merge-sort is an approach in which we divide the array up until last i.e going down to 1 element while dividing
and then callng merge on arr each single unit one time.
In the mergeSort function:
A array in inputted to be sorted
in other function sort
taken start = 0 and end = len(inputted array)
recurse the array t divide end  i.e to one element.
find mid = start+end/2
call the mergerSort function recursively on two halves to divide it further into smaller parts.
now call the merge function with array,start,mid,end
In the merge function:
needs:
1.an extra array with size of start+end
2.2 pointers to point at different halves of array to be merged and 1 for new array
while first pointer is lesser than mid and another is lesser than end 
do the comparisons to fill the new array
if left in any one copy whole
put all merged valued in an origial array.
-Raunak Kumar Sharma
'''

#merge functions
def merge(input_array,start,mid,end):
    arr = []
    i,j = start,mid+1
    
    while(i<=mid and j<= end):
        if(input_array[i]< input_array[j]):
            arr.append(input_array[i])
            i+=1
        else:
            arr.append(input_array[j])
            j+=1
    
    while(i<=mid):
        arr.append(input_array[i])
        i+=1
    while(j<=end):
        arr.append(input_array[j])
        j+=1
    
    i = 0
    while start <= end:
        input_array[start] = arr[i]
        start +=1
        i+=1

def sort(input_array,start,end):

    n = len(input_array)
    length = 1
    while length < n:
        low = 0
        while low < n-length:
            mid = int((low+length)-1)
            end = min(low+2*length-1,n-1) 
            merge(input_array,low,mid,end)
            low += 2*length
        length *=2


#mergeSort function
def mergeSort(input_array):
    start = 0
    end = len(input_array)-1
    sort(input_array,start,end)



input_array = [6,4,5,3,2,1,7]
mergeSort(input_array)
print(input_array)