def insertion_sort(arr):
    for i in range(1,len(arr)):
        a=arr[i]
        j=i-1
        while j>=0 and a<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=a
    return arr

arr=[25,12,4,56,0,12,45,150,25,65,8,5,9,1,3]
print(insertion_sort(arr))