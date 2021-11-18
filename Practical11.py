def input_list():
	li = list()
	size = input("Enter the number of students ")
	if size.isnumeric():
		size = int(size)
	else :
		print("Invalid number of students")
		exit()
	print("Enter the names of the students :")
	for i in range(size):
		ele = input("Student name :")
		li.append(ele)
	return li

def linear_search(li, search_element):
	for item in li:
		if search_element == item:
			return True 
	return False

def binary_search(li, search_element):
	start = 0
	last = len(li)
	new_sorted_list = bubble_sort(li)
	while last > start:
		mid = (start + last) / 2
		mid = round(mid)
		if li[mid] == search_element :
	 		return True
		elif li[mid] > search_element :
	 		last = mid
		elif li[mid] < search_element :
	 		start =  mid
	return False

def bubble_sort(li):
	sorted_list = li
	length_of_list = len(sorted_list)
	for i in range(length_of_list):
		for j in range(length_of_list-i-1):
			if sorted_list[j] > sorted_list[j+1]:
				temp = sorted_list[j]
				sorted_list[j] = sorted_list[j+1]
				sorted_list[j+1] = temp
	return sorted_list

def insertion_sort(li):
	sorted_list = li
	length_of_list = len(sorted_list)
	for i in range(1, length_of_list):
		key = sorted_list[i]
		j = i-1
		while j >= 0 and key < sorted_list[j] :
			sorted_list[j + 1] = sorted_list[j]
			j -= 1
		sorted_list[j + 1] = key
	return sorted_list

def selection_sort(li):
	sorted_list = li
	length_of_list = len(sorted_list)
	for i in range(0, length_of_list):
		min_element_index = i
		for j in range(i+1, length_of_list):
			if sorted_list[j] < sorted_list[min_element_index]:
				min_element_index = j
		temp = sorted_list[min_element_index]
		sorted_list[min_element_index] = sorted_list[i]
		sorted_list[i] = temp
	return sorted_list

def main():
	input_student_l = input_list()
	while True:
		print("\na)linear_search")
		print("b)binary_search")
		print("c)bubble_sort")
		print("d)selection_sort")
		print("e)insertion_sort")
		print("f)Exit the program")
		choice = input("Enter the operation you want to perform :")
		if choice == 'a':
			search_student= input("Enter the element you want to search in list :")
			if linear_search(input_student_l, search_student):
				print("Student named ",search_student, " found in the list !")
			else:
				print("No student was found with name ", search_student)
		elif choice == 'b':
			search_student= input("Enter the element you want to search in list :")
			if binary_search(input_student_l, search_student):
				print("Student named ",search_student, " found in the list !")
			else:
				print("No student was found with name ", students_name)
		elif choice == 'c':
			sorted_student_list = bubble_sort(input_student_l)
			print("sorted student list: ", sorted_student_list)
		elif choice == 'd':
			sorted_student_list = selection_sort(input_student_l)
			print("sorted student list: ", sorted_student_list)
		elif choice == 'e':
			sorted_student_list = insertion_sort(input_student_l)
			print("sorted student list: ", sorted_student_list)
		elif choice == 'f':
			exit()
		else:
			print("Invalid input")
			exit()

if __name__ == '__main__':
	main()

