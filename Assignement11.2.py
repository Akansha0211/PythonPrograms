##  In this assignment you will read through and parse a file with text and numbers.
#   You will extract all the numbers in the file and compute the sum of the numbers.
##  Handling the data:
##  The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.


import re
fh = open('Data_For_Assignement11.2')
sum = 0
lst = list()
for line in fh:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    lst = lst + y
print(lst)
for element in lst:
    sum = sum + int(element)
print(sum)


# Optional: Just for Fun
#
# There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:
#
# Python 2
# import re
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )
#
# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
#
# Please don't waste a lot of time trying to figure out the shortest solution until you have completed the homework. List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.
#
#
