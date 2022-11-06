class student:
	max_average = 0

	def __init__(self, name, marks):
		self.__name = name
		self.__marks_list = marks
		self.student_average = self.calculate_average()

	def calculate_average(self):
		total_marks = 0
		for marks in self.__marks_list:
			total_marks += marks
		average_marks = total_marks // len(self.__marks_list)
		return average_marks

	def __del__(self):
		print("student object destructed.")

def input_marks():
	marks_list = list()
	for i in range(3):
		print("Enter marks in subject ",i+1," : ", end="" )
		marks = input()
		if marks.isnumeric():
			marks = int(marks)
			marks_list.append(marks)
		else:
			i-=1
	return marks_list

def main():
	choice ='y'
	while True:
		if choice !="N" and choice != "n" :
			
			name = input("Enter student name : ")
			student_marks_list = input_marks()
			s = student(name, student_marks_list)
			if s.student_average > student.max_average:
				student.max_average = s.student_average	
				del s

		else:
			print("Maximum average marks by any student is :",student.max_average)
			break
		print("Do you want to continue adding students ?(press n/N to exit ) ", end = "")
		choice = input()

if __name__ == '__main__':
	main()


