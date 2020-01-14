country = input('Where are you from: ')
age = input('What is your age: ')
age = int(age)

if country == 'Taiwan':
	if age >= 18:
		print('You can drive.')
	else:
		print('You can not drive.')
elif country == 'USA':
	if age >= 16:
		print('You can drive.')
	else:
		print('You can not drive.')
else:
	print('You can only enter Taiwan/USA.')
