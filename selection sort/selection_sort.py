
def selection_sort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1 ,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
                arr[i] , arr[minIndex] = arr[minIndex] , arr[i]
    return arr
result = selection_sort([1,5,2,10,8,0])
print(result)

