#!/usr/bin/python3
# Script to read a file

# easy reading of file
testFile = open("testfile.txt", "r")
print(testFile.read(12))
testFile.close()


