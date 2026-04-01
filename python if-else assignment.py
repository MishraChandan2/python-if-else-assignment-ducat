# que 3:

age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2:"))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))

yng = age1
if age2 < yng:
    yng = age2
if age3 < yng:
    yng = age3
if age4 < yng:
    yng = age4
print("The youngest age is:", yng)


#que 5:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a >= b and a <= c) or (a <= b and a >= c):
    second = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    second = b
else:
    second = c
print("Second largest number is:", second)

# que 8:

# Take input from user
num = int(input("Enter a number: "))

# Check if multiple of 5
if num % 5 == 0:
    print("hello")
else:
    print("bye")
     


#que 9:

num = int(input("Enter a number:"))
last_digit = num % 10
if last_digit % 3 == 0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")


#que 10:


num = int(input("Enter a number: "))
num = abs(num)
if num >= 100 and num <= 999:
    print("It is a three-digit number")
else:
    print("It is not a three-digit number")