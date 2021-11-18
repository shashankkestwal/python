def input_list():
	l= list()
	size = input("Enter the size of the list :")
	if size.isnumeric():
		if int(size) < 0:
			exit()
		for i in range(int(size)):
			item = input("Enter the item for the list :")
			l.append(item)
		return l
	else:
		print("Invalid input ")
		return None

def check_numeric_list(l):
	numeric = True
	for item in l:
		if not item.isnumeric():
			numeric = False
	return numeric

def odd_items_in_list(l):
	odd_items = 0
	if not check_numeric_list(l):
		return None
	else :
		for item in l:
			if int(item) % 2 != 0:
				odd_items += 1
	return odd_items


def largest_string(l):
	if check_numeric_list(l):
		return None, None
	else :
		max_len = 0
		largerst_string = ""
		for item in l:
			if max_len < len(item):
				max_len = len(item)
				largerst_string = item

	return max_len ,largerst_string

def reverse_list(l):
	reversed_list = l[::-1]
	return reversed_list

def search_in_list(l, search_element):
	for item in l:
		if item == search_element or int(item) == search_element:
			return True
	return False

def remove_element_from_list(l, remove_element):
	if search_in_list(l, remove_element):
		for item in l:
			if item == remove_element or int(item) == remove_element :
				l.remove(item)
	return l


def sorted_list(l):
	l.sort()
	l = l[::-1] 
	return l

def list_of_common_elements(l1, l2):
	common_element_list = list()
	for item1 in l1:
		for item2 in l2:
			if item1 == item2:
				common_element_list.append(item2)
				break
	return common_element_list



def main():
	print("Program to perform various operations on a list ")

	l1 = input_list()
	print("The list is  :",l1)

	while True:
		print("_________________________________________________________________________")
		print("\n\na)Check if all elements in list are numbers or not.")
		print("b)If it is a numeric list,then count number of odd values in it.")
		print("c)If list contains all Strings,then display largest String in the list.")
		print("d)Display list in reverse form.")
		print("e)Find a specified element in list.")
		print("f)Remove the specified element from the list.")
		print("g)Sort the list in descending order.")
		print("h)accept 2 lists and find the common members in them")
		print("i)Exit the program")


		choice = input("Enter the operation you want to perform :")
		print("\n")

		if choice == 'a':
			is_numeric = check_numeric_list(l1)
			if is_numeric:
				print("List is numeric")
			else:
				print("List is not numeric")

		elif choice == 'b':
			odd_items = odd_items_in_list(l1)
			print("Odd items in list are :", odd_items)

		elif choice == 'c':
			str_len, largest_str = largest_string(l1)
			print("Largest string of length ",str_len,"in the list is :",largest_str)

		elif choice == 'd':
			reversed_list = reverse_list(l1)
			print("List in reversed form is :",reversed_list)

		elif choice == 'e':
			search_element = input("Enter the element you want to search in list :")
			found_in_list = search_in_list(l1, search_element)
			if found_in_list:
				print("Element found in the list")
			else :
				print("Element not found in the list")

		elif choice == 'f':
			remove_element = input("Enter the element you want to remove from list :")
			l1 =  remove_element_from_list(l1, remove_element)
			print("The list is :", l1)

		elif choice == 'g':
			sorted_li = sorted_list(l1)
			print("The sorted list is :",sorted_li)

		elif choice == 'h':
			l2 = input_list()
			common_element_list = list_of_common_elements(l1, l2)
			print("The elements common in both the list are :", common_element_list)

		elif choice == 'i':
			print(exit)
		else :
			print("Invalid input")
			exit()

		

if __name__ == '__main__':
	main()