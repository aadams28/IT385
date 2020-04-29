#!/usr/bin/python3
# Example of writing a file


# Open the file
testFile = open("testfile.txt", "w")


# write to the file
testFile.write("Always look on the bright side of life\n")
testFile.write("Your mother was Xxxx and your father smells of elderberries\n")

# Close the file
testFile.close()


