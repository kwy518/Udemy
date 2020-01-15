products = []
while True:
	name = input('Plase enter a product: ')
	if name == 'q':
		break
	price = input('Please enter the price of the product: ')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	p = [name, price]
	products.append(p)
print(products)

for p in products:
	print('The price of', p[0], 'is', p[1])

with open('products.csv', 'w') as f:
	f.write('Product, Price\n')  # add product and price two title
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')