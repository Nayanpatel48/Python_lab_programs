#and operator
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))

if num1 > num2 and num1 > num3:
    print("{0} is greatest.".format(num1))

#or operator
if num1 > num2 or num1 > num3:
    print("{0} is not the smallest.".format(num1))