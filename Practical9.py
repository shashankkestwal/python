student_dictionary = {}

def input_marks(name):
	marks_list = list()
	print("Input the marks of the student in four subjects ")
	for j in range(4):
		print("Enter the marks in subject", j+1 )
		sub_marks = input()
		if sub_marks.isnumeric() and int(sub_marks) <= 100 and int(sub_marks) >= 0:
			marks_list.append(int(sub_marks))
		else:
			print("Invalid input ")
			exit()
		student_dictionary[name] = marks_list
	
def linear_search(li, search_element):
	for item in li:
		if search_element == item:
			return True 
	return False

def highest_percent_and_student (students_list, student_dictionary):
	highest_marks = -1
	
	student_name = ""
	for name in students_list:
		total_marks= 0
		for marks in student_dictionary[name]:
			total_marks += marks

		if highest_marks < total_marks:
			highest_marks = total_marks
			students_name = name

	max_percent = (highest_marks * 100) / (len(student_dictionary[name]) * 100)
	return max_percent, students_name


def main():
	no_of_students = input("Enter the number of the student: ")
	if no_of_students.isnumeric() :
		no_of_students = int(no_of_students)
	else :
		print("Invalid number of students")
		exit()

	students_list = list()

	i = 0

	while i < no_of_students:
		print()
		name = input("Enter the name of the student :")
		if name.isnumeric():
			print("Invalid name")
			exit()
		else :
			if linear_search(students_list, name):
				pass
				print("Name already present.\nNames of the student must be unique")

			else :
				i += 1
				students_list.append(name)
				input_marks(name)

	print("The dictionary is ",student_dictionary)

	best_percent, best_student = highest_percent_and_student(students_list, student_dictionary)
	print("Student with highest marks is ", best_student, " and his percentsge is ", best_percent)

if __name__ == '__main__':
	main()