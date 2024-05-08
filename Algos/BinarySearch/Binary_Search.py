def search(lst, n):
    left = 0
    right = len(lst) - 1  
    while left <= right:
        mid = (left + right) // 2  
        if lst[mid] == n:
            return mid
        elif lst[mid] < n:
            left = mid + 1  
        else:
            right = mid - 1  
    return -1  

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(search(lst, 7))  
