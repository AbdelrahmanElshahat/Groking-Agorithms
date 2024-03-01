def Find_smallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index
def Selection_sort(arr):
    new_arr=[]
    for i in range(len(arr)):
        smallest=Find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr        
print(Selection_sort([5,3,6,2,10,1,7,9,4,8,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]))