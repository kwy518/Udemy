correctPass = 'a123456'
count = 3

while count > 0:
	password = input('Please enter your password: ')
	count = count - 1 
	if password == correctPass:
		print('Login successful!')
		break
	else:
		if count > 0:
			print('Incorrect password! You still have', count,'chances')
		else:
			print('You try too many times! Bye~')

