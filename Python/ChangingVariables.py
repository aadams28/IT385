#!/usr/bin/python3
# working with variables

myVar ='hi'
def readVar():
  print(myVar)
def changeLocal():
  myVar ='Bye'
  print(myVar)
def changeGlobal():
  global myVar
  myVar = 'Adios'
  print(myVar)

readVar()
changeLocal()
print(myVar)
changeGlobal()
readVar()
