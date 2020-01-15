import os

products = []

if os.path.isfile('products.csv'): # distinguish if there is the file
	# read a file
	with open('products.csv', 'r') as f1:
		for line in f1:
			if 'Product, Price' in line:
				continue
			s = line.strip().split(',')
			name = s[0]
			price = s[1]
			products.append([name, price])
	print(products)

else:
	print('Could not find the file.')


# Let user input
while True:
	name = input('Plase enter a product: ')
	if name == 'q':
		break
	price = input('Please enter the price of the product: ')
	price = int(price)
	p = [name, price]
	products.append(p)
print(products)

# Print all the purchase histories
for p in products:
	print('The price of', p[0], 'is', p[1])

# Write a file
with open('products.csv', 'w') as f:
	f.write('Product, Price\n')  # add two titles, product and price 
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')