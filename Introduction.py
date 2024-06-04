#This is a python introduction
#Author: @CodeBearY

# 00 - First Hello World
print("Hello World")

# 01 - Variables
a = 5
b = "John"
b2 = 'John2'
c = str(2)
d = str("log")
e = float(2)
f = 0.2

g, h, i = "Orange", "Banana", "Cherry"
j = k = l = "Orange"

fruits = ["apple", "banana", "cherry"]
m, n, o = fruits

print(a, b, c)

z = -87.7e100 # scientific number
z = 1j   # complex number

# 02 - If else

a = 33
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# 03 - Loops

## While
i = 1
while i < 6:
  print(i)
  i += 1

##For
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Functions
def my_function():
  print("Hello from a function")