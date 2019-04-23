INCREASING = 1
DECREASING = 2
BOUNCY = 3

expected_percent = input('Type the percent (%): ')


def get_type_number(number):
	str_number = str(number)
	number_type = BOUNCY
	digit_amount = len(str_number)

	for i in range(digit_amount):
		digit = str_number[i]
		if i < digit_amount - 1:
			next_digit = str_number[i + 1]
			if i == 0:
				number_type = INCREASING if digit < next_digit else BOUNCY
				number_type = DECREASING if digit > next_digit else number_type
			elif (number_type == INCREASING and digit > next_digit) or (number_type == DECREASING and digit < next_digit):
				number_type = BOUNCY
				break
			elif digit < next_digit:
				number_type = INCREASING
			elif digit > next_digit:
				number_type = DECREASING
		else:
			return None

	return number_type


amount = 0
number = 0

bouncy_percent = 0

while bouncy_percent != expected_percent:
	number += 1
	if get_type_number(number) == BOUNCY:
		amount += 1
	bouncy_percent = amount * 100 / number


print('Percent: %s' % expected_percent)
print('The min number was %s' % number)