summation = 0
product = 1

while True:
	x = int(input('x = '))

	if x == 0:
		break

	if x % 2 == 0:
		summation += x
	else:
		product *= x

print('Summation:', summation)
print('Product:', product)