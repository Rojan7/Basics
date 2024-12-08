#8)WAP to sort the list {5, 4, 11, 13, 51}
# list_to_sort = [5,4,11,13,51]
# list_to_sort.sort()
# for items in range(len(list_to_sort)-1,-1,-1):
#     print(list_to_sort[items])

def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    
    pivot = arr[-1]
    
   
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
   
    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [5, 4, 11, 13, 51]
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)
