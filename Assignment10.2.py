# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
lst = list()
handle = open(name)
lst = list()
di = dict()
for line in handle:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        words = line.rstrip().split()
        time = words[5]
        hrs = time.split(':')
        # print(hrs)
        h = hrs[0]
        # print(h)
        di[h] = di.get(h, 0) + 1
# print(di)
dict1 = sorted(di.items())
for k,v in dict1:
    print(k, v)

# dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}
# dict1 = sorted(dict.items())
# for k ,v in dict1:
#     print(k, v)
