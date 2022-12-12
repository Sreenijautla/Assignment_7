# Reverse a number entered by the user
# Take a number as input from the user. Print the number in reversed order. For example, for input 567, output should be: 765

def Reverse(num):
    num=str(num)
    return num[::-1]
num=int(input('Enter a number : '))
result=Reverse(num)
print('The given number in reversed order is :',result)