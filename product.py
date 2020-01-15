products = []
while True:
	name = input('Plase enter a product: ')
	if name == 'q':
		break
	price = input('Please enter the price of the product: ')
	#p = []
	#p.append(name)
	#p.append(price)
	p = [name, price]
	products.append(p)
print(products)

for p in products:
	print(p)