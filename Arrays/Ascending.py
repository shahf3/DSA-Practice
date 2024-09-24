def ascendingOrder(arr):

    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                swap = True
    
        if not swap:
            break
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(ascendingOrder(arr))