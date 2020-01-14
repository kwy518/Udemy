weight = input('Please enter your weight(kg): ')
height = input('Please enter your height(cm): ')

height = float(height)
weight = float(weight)

height /= 100

BMI = weight / (height * height)
print('Your BMI is: ', BMI)