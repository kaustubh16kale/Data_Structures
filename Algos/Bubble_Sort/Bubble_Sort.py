def bubblesort(arr):
    print(f"initial array {arr}")
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[1,14,0,1,2,5,8,13,5,7,100,25,63]
print(bubblesort(arr))