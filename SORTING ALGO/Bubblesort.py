# BUBBLE SORT
arr=[9,3,7,5,2,1]
n=len(arr)
for i in range(0,n-1):
    flag=0
    for j in range(0,n-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            flag=1    
        else:
            pass
        
    if flag==0:
            break
    
    
print(arr)