import datetime

client_info = open('.client', 'r')
x = client_info.readline().rstrip()
print(x.dtype)