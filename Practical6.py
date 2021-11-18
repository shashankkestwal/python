def even_elements_tuple(t):
	list_t = list(t)
	list_even = list()
	for i in list_t:
		if i % 2 == 0:
			list_even.append(i)
	t_even = tuple(list_even)
	return t_even

def concatenate_tuple(t1 , t2):
	t_concatenate = t1 + t2 
	return t_concatenate

def max_and_min_tuple(t):
	maximum = max(t)
	minimum = min(t)
	return maximum ,minimum


def main() :
	t1 = (1,2,5,7,9,2,4,6,8,10) 
	t2 = (11,13,15)
	print("The tuple is :", t1)
	while True:
		print("\na)Print another tuple whose values are even numbers in the given tuple.\n"
		"b)Concatenate a tuple t2={11,13,15) with t1.\n"
		"c)Return maximum and minimum value from this tuple.\n"
		"d)Exit the program \n")

		choice = input("Enter the operation you want to perform :")

		if choice == 'a':
			even_tuple = even_elements_tuple(t1)
			print(even_tuple)
		elif choice == 'b':
			concatenated_tuple = concatenate_tuple(t1,t2)
			print(concatenated_tuple)
		elif choice == 'c':
			max_in_tuple , min_in_tuple = max_and_min_tuple(t1)
			print("Maximun element in tuple is ", max_in_tuple)
			print("Minimum element in tuple is ", min_in_tuple)
		elif choice == 'd':
			exit()
		else:
			print("Invalid choice")
			exit()

if __name__ == '__main__':
	main()

