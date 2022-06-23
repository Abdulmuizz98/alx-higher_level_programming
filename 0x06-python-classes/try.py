#!/usr/bin/python3
Square = __import__('101-square').Square

my_square_1 = Square(3)
print(my_square_1)

print("--")

my_square_2 = Square(3, (1, 1))
print(my_square_2)

print("--")

my_square_3 = Square(3, (3, 0))
print(my_square_3)

print("--")
