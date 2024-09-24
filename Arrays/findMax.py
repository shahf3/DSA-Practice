#Given an array, write functions to find the minimum and maximum elements in it. 


def findMax(arr): # n = length of array
    
    n = len(arr)

    for i in range(n):
        swap = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                swap = True
    
        if not swap:
            break
    return arr[0], arr[-1]

a = [1, 423, 6, 46, 34, 23, 13, 53, 4]
print(findMax(a))            