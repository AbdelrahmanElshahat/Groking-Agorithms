def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less = [i for i in arr[1:] if i<=pivot]
        greater = [i for i in arr[1:] if i>pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([5,3,6,2,10,1,7,9,4,8,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))