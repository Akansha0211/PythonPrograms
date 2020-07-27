# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
# lst = list()  no use
di = dict()
for line in handle:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        words = line.rstrip().split()
        time = words[5]  # extract whole time eg 19:23:45
        hrs = time.split(':')   #split by : results in list having string ['19', '23', '45']
        # print(hrs)
        h = hrs[0]  # extract only time in hr
        # print(h)
        di[h] = di.get(h, 0) + 1  #count frequency of time in hr
# print(di)
dict1 = sorted(di.items())   # sort the dictionary items based on key (here key is time in hr)
for k,v in dict1:
    print(k, v)

# dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'}
# dict1 = sorted(dict.items())
# for k ,v in dict1:
#     print(k, v)
