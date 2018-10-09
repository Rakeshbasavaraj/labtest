import sys
a=sys.argv[1]
with open('file2.txt') as p:
	line = p.readlines()
for x in line:
	x=x.split(' ')
	if a == x[0]:
		print("IP found")
		break
	else:
		print("IP not found")