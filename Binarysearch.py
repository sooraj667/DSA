# BINARY SEARCH

arr=[1,2,3,4,5,6,7,100,150,200,260,280,300]
l=0
r=len(arr)-1
mid=(l+r)//2
searchvalue=400

while l<=r:
    if arr[mid]==searchvalue:
        print(f"{searchvalue} found at position {mid}")
        break
    else:
        if searchvalue<arr[mid]:
            r=mid-1
            mid=(l+r)//2
            
        elif searchvalue>arr[mid]:
            l=mid+1
            mid=(l+r)//2
if l>r:
    print("Element Not found!")


