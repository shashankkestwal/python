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


def input_marks():
	marks_list = list()
	for i in range(3):
		print("Enter marks in subject ",i+1," : ", end="" )
		marks = int(input())
		marks_list.append(marks)
	return marks_list

def main():

	while True:
		print("do you want to continue ?(press n/N to exit ) ", end = "")
		choice = input()
		if choice !="N" and choice != "n" :
			
			name = input("Enter your name : ")
			student_marks_list = input_marks()
			s = student(name, student_marks_list)
			if s.student_average > student.max_average:
				student.max_average = s.student_average	
		else:
			print("Maximum average marks by any student is :",student.max_average)
			exit()


if __name__ == '__main__':
	main()


