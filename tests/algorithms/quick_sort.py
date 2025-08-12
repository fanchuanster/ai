def quick_sort_hoare(arr,low,high):
    if low >= high: return
    pivot = arr[low]
    # pivot = arr[(low + high) // 2]
    left, right = low, high
    while True:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left >= right:
            break
        arr[left],arr[right] = arr[right], arr[left]
        left += 1
        right -= 1        

    quick_sort_hoare(arr, low, right)
    quick_sort_hoare(arr, right+1, high)

def quick_sort_lomuto(arr, low, high):
    if low >= high: return
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    quick_sort_lomuto(arr, low, i)
    quick_sort_lomuto(arr, i+2, high)

def quick_sort(arr):
    # quick_sorti(arr,0,len(arr)-1)
    quick_sort_lomuto(arr,0,len(arr)-1)
    return arr