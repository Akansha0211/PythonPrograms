##  In this assignment you will read through and parse a file with text and numbers.
#   You will extract all the numbers in the file and compute the sum of the numbers.
##  Handling the data:
##  The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.


import re
# name = input('Enter file name')
fhandle = open('Data_For_Assignement11.2')
number = list()
for line in fhandle:
    number = re.findall('[0-9]',line)
