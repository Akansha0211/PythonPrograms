#  7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
#
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
#
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input('Enter the file name: ')  # input file name returns string
fh = open(fname)  # opens up file by-default in read-mode
count = 0
sum = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        data = line.strip()
        # print(data)
        pos = data.find('0')
        num = data[pos:]
        sum = sum + float(num)
print('Average spam confidence:',sum/count)










