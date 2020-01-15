import os

# read a file
def read_file(filename):
	products = []
	with open(filename, 'r') as f1:
		for line in f1:
			if 'Product, Price' in line:
				continue
			s = line.strip().split(',')
			name = s[0]
			price = s[1]
			products.append([name, price])
		print(products)
	return products

# Let user input
def user_input(products):
	while True:
		name = input('Plase enter a product: ')
		if name == 'q':
			break
		price = input('Please enter the price of the product: ')
		price = int(price)
		p = [name, price]
		products.append(p)
	print(products)
	return products

# Print all the purchase histories
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is', p[1])

# Write a file
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('Product, Price\n')  # add two titles, product and price 
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # distinguish if there is the file
		products = read_file(filename)
	else:
		print('Could not find the file.')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()