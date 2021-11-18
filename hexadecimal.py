def add_to_hex(index):
	if index >= 0 and index <= 9:
		next_val = str(index)
	elif index >= 10 and index < 16:
		next_val = chr(65 +(index - 10))
		
	else :
		print("some error found")
	return next_val



def to_hexadecimal(decimal):
	hexadecimal = ""
	while decimal != 0:
		rem = decimal % 16
		next_val = add_to_hex(int(rem))

		hexadecimal = next_val + hexadecimal 
		decimal = decimal // 16
	return hexadecimal


def main():

	decimal = int(input("Enter the decimal value :"))
	a = to_hexadecimal(decimal)
	print(a)
	

if __name__ == '__main__':
	main()
