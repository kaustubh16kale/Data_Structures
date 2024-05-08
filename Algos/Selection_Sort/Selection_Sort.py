def selectionsort(arr,size):
    for i in range(size):
        min_idx=i

        for j in range(i+1,size):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]


arr=[7,4,5,8,1,2,3,5,6,70,5,100,25,43,20]
selectionsort(arr,len(arr))
print(arr)
