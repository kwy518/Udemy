correctPass = 'a123456'
count = 3

while True:
	password = input('Please enter your password: ')
	count = count - 1 
	if password == correctPass:
		print('Login successful!')
		break
	else:
		if count == 0:
			print('You try too many wrong times!')
			break
		else:
			print('Incorrect password! You still have', count,'chances')
