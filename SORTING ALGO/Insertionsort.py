# INSERTION SORT

arr=[100,44,55,99,2,3,1,23]

for i in range(len(arr)):
    key=i
    while arr[key]<arr[key-1] and key>=1:
        arr[key],arr[key-1]=arr[key-1],arr[key]
        key-=1
        
print(arr)