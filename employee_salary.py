#class Employee is declared 

class Employee:

	# initializing the class and setting employee details 
	def __init__(self, name , age , department, phone_no ):

		self.__name = name
		self.__age = age
		self.__department = department
		self.__phone_no = phone_no
		# initially salary is an empty dictionary
		self.__salaries = {}


	def input_working_days(self):
		i = 1
		#asking the number of working days for every month (Note : Months are denoted by their occurance number )
		while i <= 12:

			print("Enter the number of working days for month ", i ," : ", end= "")
			working_days = input() 
			if working_days.isnumeric():
				# handling the exception of invalid number of days 
				try:
					working_days = int(working_days)
					if working_days < 5 or working_days > 30:
						# raising an exception if days <5 or >30
						raise Exception("working days cannot be less than 5 or greater than 30")			
					self.__salaries[i] = self.compute_salary(working_days)
				except Exception as invalid_working_days:
					# salary for the month is set 0 is invalid number of days entered
					print(invalid_working_days)
					print("your salary for this month is settled 0 ")
					self.__salaries[i] = 0				
			else :
				# ATQ default number of days = 22
				print("default working days = 22 has been set for this month")
				self.__salaries[i] = self.compute_salary()			
			i += 1
		print("Salary of the employee for this year:")
		print(self.__salaries)


	# computing net salary and calcualting tax and total salary
	def compute_salary(self, working_days = 22):
		total_salary = working_days * 1000
		print(total_salary)
		tax = total_salary *0.1
		net_salary = total_salary - tax
		return net_salary

	# getting details of employee stored in private variables
	def get_names(self):
		return self.__name



# taking employee details from the user
def employee_details():
	# asking for a valid name 
	while True:
		name = input("Enter employee name : ")
		if name == "" or name.isnumeric():
			print("invlid name, Please Enter a valid name ")
		else :	
			break
	# is wrong age entered no employee is created
	age = input("Enter employee age : ")
	if age.isnumeric():
		try:
			age = int(age)
			if age < 18:
				raise Exception("age must be >= 18")
		except Exception as invalid_age_exception:
			print(invalid_age_exception)
			print("minimum age to be an employee is 18")
			return -1,-1,-1,-1
	elif age.isalpha() :
		print("cannot create employee of age ", age)
		return -1,-1,-1,-1

	
	# asking to enter a valid non numeric department 
	while True:
		department = input("Enter the department of the employee : ")
		if department == "" or department.isnumeric():
			print("No department named ", department,"\nTry again")
			pass
		else:
			break


	# asking for a 10 digit phone number 
	while True:		
		phone_no = input("Enter employee phone number :")
		if phone_no.isnumeric() and len(phone_no) == 10:
			phone_no = int(phone_no)
			break
		else:
			print("Invalid phone number, Try again")

	# returning all details  as a list 
	return name, age , department, phone_no



def main():
	print("EMPLOYEE AND SALARY MANAGER ")
	# creating a list to store objects of Employee class
	employees_list = list()
	# counting the number of employees created
	employee_count = 0 
	while True:
		more = input("Do you want to create employee : (press n/N to exit) ")
		if more != 'n' and more != 'N' :
			employee_name , employee_age, employee_department, employee_phone_no = employee_details()
			if employee_age == -1:
				continue
			else:
			# creating emp object and calling __init__ method 
				emp = Employee(employee_name , employee_age, employee_department, employee_phone_no)
			#aking the number of working days for the year  
			emp.input_working_days()
			# appending the list to the employee_list list
			employees_list.append(emp)
			employee_count +=1
		else:
			# printing names of all the employees created 
			print("Total number of employees created : ", employee_count)
			print("Names of all employees ")
			i = 1
			for employees in employees_list:
				print("Employee ", i ," details : ", employees.get_names(),"\n")
				i += 1
			exit()


# calling the main function
if __name__ == '__main__':
	main()







