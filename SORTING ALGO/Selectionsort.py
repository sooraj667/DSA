arr=[100,44,55,99,2,3,1,23]

for i in range(len(arr)):
    current=arr[i]
    smallest=None
    for j in range(i+1,len(arr)):
        if arr[j]<current:
            smallest=j
            current=arr[j]
    if smallest!=None:
        arr[i],arr[smallest]=arr[smallest],arr[i]

print(arr)
        