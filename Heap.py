# HEAP
# BUILD HEAP


def maxheap(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    
    
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
        
    if largest != i:
        arr[largest],arr[i]=arr[i],arr[largest]
        maxheap(arr,n,largest)


def insert(arr,val):
    arr.append(val)
    index = len(arr)-1
    parent_index = (index//2)-1
    
    while index!=0 and arr[index]>arr[parent_index]:
           
                 
            
            
            arr[parent_index],arr[index]=arr[index],arr[parent_index]

            index=parent_index
            parent_index=(index//2)-1
            if index==1:
                parent_index=0


def delete(arr):
    n=len(arr)
    arr[0]=arr[n-1]
    arr.pop()
    newlen=len(arr)
    maxheap(arr,newlen,0)
 

def heapsort(arr):
    buildheap(arr)
    n=len(arr)
    for i in range(n-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        maxheap(arr,i,0)
    return arr















arr=[2,4,5,1,7,10,6,19,20,11]

def buildheap(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        maxheap(arr,n,i)
        
       
    
# buildheap(arr)
# # print(arr)
# # insert(arr)
# print(arr)
# delete(arr)
print(heapsort(arr))

