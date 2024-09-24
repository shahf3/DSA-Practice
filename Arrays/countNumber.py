def countNumber(arr, x):

    i = 0
    count = 0
    while i < len(arr):
        if arr[i] == x:
            count += 1
        i += 1
    return count

arr = [1, 1, 2, 2, 2, 2, 3]
x = 2
print(countNumber(arr, x))
