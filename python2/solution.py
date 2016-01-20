import socket
import pickle
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))

print s.recv(100)
print s.recv(100)
s.send("AmourDeMai\n")
print s.recv(100)
s.send('dbf1f284168cb314f28b11aaf3c28826\n')
print s.recv(100)

# guess the number
found = False
first = 0
last = 10000
while first <= last and not found:
	mid = (first + last) / 2
	s.send(str(mid) + "\n")
	res = s.recv(100).split()
	if res[0] != 'nope.': 
		found = True
	else:
		if res[3] == 'bigger':
			first = mid
		else:
			last = mid

# de-pickle
string =  s.recv(500)
strings = string.split("\n")
i = 1
objectString = ""
while i < 9:
	objectString = objectString +  strings[i]
	if (i != 8):
		objectString = objectString + "\n"
	i = i + 1

a = pickle.loads(objectString)
s.send(str(a.microsecond) + "\n")
print s.recv(100)

# weekday
word = s.recv(100)
words = word.split(" ")
months = ['Begin', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
year = words[7]
month =  months.index(words[6])
day = words[5]
weekDate =  datetime.date(int("20" + year[0:2]), month, int(day)).strftime("%A")
s.send(weekDate+"\n")

# secret code
word = s.recv(1000)
words = word.split("\n")
#print words
if len(words) >= 3: 
	print words[2]
print s.recv(100)
s.close()


