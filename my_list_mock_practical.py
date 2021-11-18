class MyList:

	def __init__(self, size):
		self.__size_of_list = size
		self.my_list = self.input_list()
		

	def input_list(self):
		create_list = list()
		for i in range(self.__size_of_list):
			element = int(input("Enter list element "))
			create_list.append(element);
		return create_list



def main():
	list_object  = MyList (size)

		