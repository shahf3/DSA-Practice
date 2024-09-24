#Given an unsorted array, find a peak element in it. An element is considered to be peak if its value is greater than or equal to the values of its adjacent elements (if they exist). There can be more than one peak elements in an array, we return any of them,

#Note: If the array is increasing then just print the last element will be the maximum value.

#Example:

#Input: arr[]= {5, 10, 20, 15}
#Output: 20
#Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

#Input: arr[] = {10, 20, 15, 2, 23, 90, 90}
#Output: 20 or 90
#Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.

#Input: arr[] = [1, 1, 1]
#Output : 1
#Explanation: All elements are peak in the given array, we can return any of them,

def PeakValue(arr, n):

    #if(n == 1):
    #    return 0

    if arr[0] >= arr[1]:
        return 0
    
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
    
    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i+1] and arr[i] >= arr[i-1]:
            return i

    

arr = [ 5, 10, 20, 15]
n = len(arr)
print("Index of a peak point is", PeakValue(arr, n))