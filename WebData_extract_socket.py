import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()

# ip = socket.gethostbyname('www.w3schools.com')
# print(ip)
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.w3schools.com', 80))
# cmd = 'GET https://www.w3schools.com/python/  HTTP/1.0\n\n'.encode()
# mysock.send(cmd)
# while True:
#     data = mysock.recv(512)
#     if(len(data)<1):
#         break
#     print(data.decode())
# mysock.close()