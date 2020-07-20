# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input('Enter the file name')
if len(name) < 1: name = 'mbox-short.txt'
handle = open(name)
lst = list()
dict = dict()
for line in handle:
    if not line.startswith('From'):
        continue
    if not line.startswith('From:'):
        continue
    else:
        words = line.rstrip().split()
        # print(words)
        email = words[1]
        # print(email)
        dict[email] = dict.get(email, 0) + 1

        # print(dict)
# print(dict)
# max_key = max(dict, key= dict.get)
# max_value = max(dict.values())
#
# print(max_key)
# print(max_value)

maximum = 0
max_key = None
for k in dict:
    if dict[k] >maximum:
        maximum = dict[k]
        max_key = k
print(max_key , maximum)


# a = {"a":1, "b":2, "c":3}
# max_key = max(a , key= a.get)
# print(max_key)



# name = input('Enter file name')
# if len(name) < 1 : name = 'mbox-short.txt'
# handle = open(name)
# di = dict()
# for line in handle:
#     line = line.rstrip()
#     # print(line)
#     words = line.split()
#     # print(words)
#     for word in words:
#         if word in di:
#             di[word] = di[word]+1
#         else:
#             di[word] = 1
#         # print(word, di[word])
# print(di)
# # now we want to find the most common word
# largest = -1  ## since values (v are always number >1)
# theword = None
# for k, v in di.items():
#     # print(k,v)
#     if v > largest:
#         largest = v
#         theword = k
# print(theword, largest)


