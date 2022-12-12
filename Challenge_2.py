# Write a Python Program to print full pyramid using '*' symbol. The pattern should be as shown below:

# *

# * * *

# * * * * *

# * * * * * * *

# * * * * * * * * *


n=int(input('Enter the number of rows : '))
for i in range(n):
    for j in range(i):
        print("*",end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print('\n')