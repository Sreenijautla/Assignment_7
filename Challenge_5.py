# Program to cyclically rotate an array by one
# Given an array, cyclically rotate the array clockwise by one. 
# Examples:  
# Input: arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}


arr=[1, 2, 3, 4, 5]
length=len(arr)
last=arr[length-1]
for i in range(length-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=last
print("Output is :",arr)