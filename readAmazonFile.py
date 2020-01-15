data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)

sum = 0		
for d in data:
	sum += len(d)
	
print(sum / len(data))
