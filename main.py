# def int(a,b):
#     print("sum of number", (a+b))
#     print("difference of two number", (a-b))
#     print("product of two number", (a*b))

# int(5,2)

# def detail(roll):
#     x = [10,20,30,12,32,40]
#     if roll in x:
#         print(f"Roll Number {roll} is present")
#     else:
#         print(f"Roll Number {roll} is absent")

# roll = int(input("Enter roll number. "))
# detail(roll)

# def result(a, b):
#     sum = a+b
#     sub = a-b
#     mul = a*b
#     print(f"Sum is {sum}, Sub is {sub}, & Multiply is {mul}")

# a = int(input("Enter value of a: "))  # 7
# b = int(input("Enter value of b: "))  # 5
# result(a,b)


# def max(a,b,c):
#     if a>b and a>c:
#         print(f"{a}is the maximum value")
#     elif b>a and b>c:
#         print(f"{b}is the maximum number")
#     else:
#         print(f"{c}is the maximum number")

# max(30,20,10)

# def detail(roll):
#     x = [23,43,22,56]
#     if roll in x:
#         print(f"Roll number {roll} is present")
#     else:
#         print(f"Roll number {roll} is absent")
# roll = int(input("Enter roll no. ")) # 24
# detail(roll)



# import string


# if __name__ == '__main__':
#     n = int(input())

#     x = 1<= n <=150

#     def int(string):
#         for i in x:
#             print(list(range(1,20)))
#             print(i)
#     string = x
#     int(x)
    
# x = lambda a:a+10
# print(x(5))

# class phone:
#     def makes_call(saelf):
#         print("making phone call")

#     def play_game(self):
#         print("playing game")

#     p1 = phone()
        
                                    #object oriented programming
# class student:
#     def check_pass_fail(self):
#         if self.marks >= 40:
#             return True
#         else:
#             return False

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# student1 = student("harry", 85)
# student2 = student("arif khan", 30)
# did_pass = student1.check_pass_fail()
# print(did_pass)
# did_pass = student2.check_pass_fail()
# print(did_pass)


# class complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def add(self, number):
#         real = self.real + number.real
#         imag = self.imag + number.imag
#         result = complex(real, imag)
#         return result

# n1 = complex(5, 6)
# n2 = complex(-2,8)
# result = n1.add(n2)
# print("real =", result.real)
# print("imag =", result.imag)



# Print the first 10 natural numbers using for loop
#  Python program to calculate the sum of all the odd numbers within the given range.


# x = 10
# sum = 0
# for i in range(1,x+1):
#     if i % 2 == 0:
#         sum+=i
# print(sum)


# def myFun(*argv):
# 	for arg in argv:
# 		print(arg)


# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# def generator_func():
# 	num = 1
# 	print("first time ")
# 	yield num

# 	num = 10
# 	print("second time ")
# 	yield num

# 	num = 100
# 	print("third time ")
# 	yield num

	

# obj = generator_func()

# print(next(obj))
# print(next(obj))
# print(next(obj))


                 #DECORATOR FUNTION

# def decor(addition):
#     def inner():
#         result = addition()
#         num3 = float(input("Enter third number:"))
#         result = result + num3
#         return result
#     return inner
       
# @decor
# def addition():
#     num1 = float(input("Enter first number:"))
#     num2 = float(input("Enter second number:"))
#     result = num1 + num2
#     return result


# print("addition is:",addition())

# code for testing decorator chaining
# def decor1(func):
# 	def inner():
# 		x = func()
# 		return x * x
# 	return inner

# def decor(func):
# 	def inner():
# 		x = func()
# 		return 2 * x
# 	return inner

# @decor1
# @decor
# def num():
# 	return 10

# print(num())

# input


#Write a program to create a function that takes two arguments, name and age, and print their value.

# def func(name, age):
#   print(name, age)

# func("hurry",56)

# Write a program to create function func1() to accept a variable length of arguments and print their value

# def func1(*args, **kwargs):
#     for i in args and kwargs:
#         print(i)

# func1(20,30,60)
# func1("apple", "orange", "banana")
# func1("apple":20, "orange":30, "banana":60)

import numpy as np
import qrcode
import image
import json

qr = qrcode.QRCode(
    version= 15,
    box_size= 15,
    border= 5,
)
fruitList = {}
for i in range(5):
    myfruit = str(input())
    fruitList[myfruit[0]] = myfruit
print(fruitList)
s=json.dumps(str(fruitList))
print(s)
qr.add_data(s)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white")
img.save("text.png")