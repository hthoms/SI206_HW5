import re

fle = input('Enter file name: ')

f = open(fle)

lst = []
total = 0
for line in f:
	line = line.rstrip()
	found = re.findall('[0-9]+', line)
	lst.extend(found)

for item in lst:
	total += int(item)

print(total)
