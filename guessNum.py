import random

r = random.randint(1, 100)
count = 0

while True:
	yourNum = input('Guess a number: ')
	count += 1
	if int(yourNum) == r:
		print('You are correct!')
		break
	elif int(yourNum) > r:
		print('Your number is bigger.')
	else:
		print('Your number is smaller.')
	print('This is your', count, 'tries')