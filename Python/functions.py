#!/usr/bin/python3


# Basic function
def func1():
  print("Something Func-y")

# Function that takes an argument
def addNums(val1, val2):
  print(val1 + val2)


# function that returns a value
def cube(x):
  return x * x * x

# Function with default value
def power(num, power=2):
  result =1
  for i in range(power):
    result = result * num
  print(result)

# Variable number of parameters
def multiAdd(*args):
  result = 0
  for x in args:
    result += x
  return result

  
# Call function
#func1()
#print(func1())
#print(func1)


#addNums(5, 6)
#addNums(val2 = 11, val1= 9)

#print(cube(5))


#power(6,6)
#power(6,2)
#power(6)

print(multiAdd(5, 6, 9, 15, 9))
print(multiAdd())
print(multiAdd(25, 32, 89, 88, 36, 22, 55, 174))


