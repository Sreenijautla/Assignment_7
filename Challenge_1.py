# Write a Python Program to print half pyramid using alphabets. The pattern should be as shown below:
# A

# B B

# C C C

# D D D D

# E E E E E


n=int(input('Enter the number of rows : '))
k=ord('A')
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=' ')
    k+=1
    print('\n')