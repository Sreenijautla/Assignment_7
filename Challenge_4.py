# Given an array arr[] of integers. Find a peak element i.e. an element that is not smaller than its neighbors. 
# Note: For corner elements, we need to consider only one neighbor. 
# Example:
# Input: array[]= {5, 10, 20, 15}
# Output: 20
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.
# Input: array[] = {10, 20, 15, 2, 23, 90, 67}
# Output: 20 or 90
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.


def Peak_elements(arr):
    arr1=[]
    n=len(arr)
    if arr[0]>arr[1]:
        arr1.append(arr[0])
    if arr[n-1]>arr[n-2]:
        arr1.append(arr[n-1])
    else:
        for i in range(1,n-1):
            if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
                arr1.append(arr[i])
    print("The peak elements which are greater than it's neighbours :")
    for i in arr1:
        print(i)
arr=[10, 20, 15, 2, 23, 90, 67]
# arr=[5, 10, 20, 15]
# arr=[20,10,30]
Peak_elements(arr)