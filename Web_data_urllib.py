import urllib.request,urllib.parse,urllib.error
## Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') ## does all the socket work i.e establish server connetion, send GET request
# for line in fhandle:
#     print(line.decode().strip())

count = dict()
for line in fhandle:
    words = line.decode().strip().split()
    for word in words:
        count[word] = count.get(word,0)+1
print(count)