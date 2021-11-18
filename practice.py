
# # def countVaowels(message):
# #     count=0
# # 	for ch in message:
        
# #     print(count)
# # message ="hey there how are you. Byeeee"
# # countVaowels(message)

# def reverse(s):
#   rev_str = ""
#   for i in s:
#     rev_str = i + rev_str
#   return rev_str

# def isPalindrome(str):
#     if len(str)%2==0:
#         return false
#     else:
#         return str==reverse(str)
 
 
# def main():
#     string =input("Enter the string :")
#     print("palindrome :",isPalindrome(string))


# main()

# Write  a  python  program  to  create  a  function called computation() which  takes  as  parameter num.  If  num  is  even  it  should  return  num//2  and  if  num  is  odd  then  it  should  return 3*number+1. Print the returned value in main and use this returned value to call computation(). Repeat this till the return value is 1.
# def computation(num):
#     if num%2==0:
#         return num//2
#     else:
#         return 3*num + 1

# def main():
#     num=int(input("Enter the number "))
#     print(computation(num))
#     if(computation(num)==1):
#         print("Function returned 1\nExiting the program")
#         exit()
#     else:
#         main()

# main()


# def fun(s):
#     k=len(s)
#     m=""
#     for i in range(0,k):
#         if(s[i].isupper()):
#             m=m+s[i].lower()
#         elif s[i].isalpha():
#             m=m+s[i].upper()
#         else:
#             m=m+'bb'
#     print(m)

# fun('school2@com')




# def Change(P ,Q=30):
#     P=P+Q 
#     Q=P-Q 
#     print( P,"#",Q) 
#     return (P)
# R=150 
# S=100 
# R=Change(R,S) 
# print(R,"#",S)
# S=Change(S)

# print(int("74")+2)



# def increment(x):
# 	x += 1
# 	print(id(x))
# 	print(x)
# 	print(id(x))

# def main():
# 	x =10
# 	print(x)
# 	print(id(x))
# 	increment(x);
# 	print(x)
# 	print(id(x))

# main()



# def main():
# 	# Initialize times
# 	times = 3
# 	print( "Before the call, variable" ,
# 	"times is" , times)
# 	# Invoke nPrintln and display times
# 	nPrint( "Welcome to CS!" , times)
# 	print( "After the call, variable" ,
# 	"times is" , times)
# 	# Print the message n times
# def nPrint(message, n):
# 	while n > 0 :
# 		print( "n = " , n)
# 		print(message)
# 		n -= 1
# main()




# def f(x, y = 1 , z = 2 ):
# 	return x + y + (z + 1)

# print(f( 1 , 1 , 1 ))
# print(f(1 , y = 10 , z = 30 ))
# print(f( 1 , z = 3 ))


# char1 = "z"
# char2 = "A"

# import random
# print(ord(char1))
# print(ord(char2))
# mid_char = random.randint(ord(char2), ord(char1))

# print(chr(mid_char)) 





# class Count:
# 	def __init__(self, count = 0):
# 		self.count = count

# def main():
# 	c = Count()
# 	n = 1
# 	m(c, n)
# 	print("count is", c.count)
# 	print("n is", n)

# def m(c, n):
# 	print(id(c))
# 	n = 3

# main()


# class A:
# 	def __init__(self, i):
# 		self.__i = i
# 	def __increment(self):
# 		self.__i += 1
# 	def print_i(self):
# 		self.__increment()
# 		print(self.__i)


# def main():
# 	a = A(5)
# 	print(type(a))
# 	a.print_i()

# if __name__ == '__main__':
# 	main()


# string1 = " "
# string2 = "andc"
# print(id(string1))
# print(id(string2))
# string1 += string2
# print(id(string1))


# s = "abc"
# v = "ab"
# print(s >= v)

# import os

# os.system("whoami")


# fileVariable = open(filename, mode)


# readfile = open("a.txt","r")
# writefile = open("b.txt","w")
# line_string = " "
# char_count = 0
# while line_string != "":
# 	line_string = readfile.readline()
# 	print(line_string)
# 	char_count += len(line_string)
# 	writefile.write(line_string)

# print(char_count)
# readfile.close()
# writefile.close()


# from random import randint
# def main():
# 	# Open file for writing data
# 	abc = input("Enter file name :")
# 	outfile = open(abc, "w")
# 	for i in range(10):
# 		outfile.write(str(randint(0, 9)) + "")

# 	outfile.close() # Close the file
# 	# Open file for reading data
# 	infile = open("Numbers.txt", "r")
# 	s = infile.read()
# 	numbers = [int(x) for x in s.split() ]
# 	print(type(numbers))

# 	for number in numbers:
# 		print(number, end = "  ")
# 	infile.close() # Close the file
# main()

# from tkinter.filedialog import askopenfilename
# from tkinter.filedialog import asksaveasfilename
# filenameforReading = askopenfilename()
# print("You can read from " + filenameforReading)
# file = open(filenameforReading,"w")

# file.write("abcd")
# print(type(filenameforReading))
# # filenameforWriting = asksaveasfilename()
# # print("You can write data to " + filenameforWriting)


# read_file = open("a.txt","r")

# chars = {}
# i = 0
# for lines in read_file:
# 	while i < len(lines):
		
# import urllib.request
# infile = urllib.request.urlopen("https://www.youtube.com/watch?v=fXw0jcYbqdo")
# print(infile.read().decode())



# def a_function():
# 	pass
# def main():
# 	print(type(a_function()))

# if __name__ == '__main__':
# 	main()

# import pickle
# def main():
# 	# Open file for writing binary
# 	outfile = open("pickle.dat", "wb")
# 	pickle.dump(1, outfile)
# 	pickle.dump(56.6, outfile)
# 	pickle.dump("Programming is fun", outfile)
# 	pickle.dump([1, 2, 3, 4], outfile)
# 	outfile.close() # Close the output file
# 	# Open file for reading binary
# 	infile = open("pickle.dat", "rb")
# 	print(pickle.load(infile))
# 	print(pickle.load(infile))
# 	print(pickle.load(infile))
# 	print(pickle.load(infile))
# 	infile.close() # Close the input file
# main() # Call the main function





# try:
# 	raise error("error error error ")
# except error:
# 	print(error)

# class A:
# 	def __init__(self, i = 0):
# 		self.__i = i
# 	def m1(self):
# 		self.__i += 1
# 	def __str__(self):
# 		return str(self.__i)

# x = A(8)
# print(x)



# class A:
# 	def __new__(self):
# 		self.__init__(self)
# 		print("A's _ _ new _ _ () invoked")
# 	def __init__(self):
# 		print("A's _ _ init _ _ () invoked")


# class B(A):
# 	def __new__(self):
# 		self.__init__(self)
# 		print("B's _ _ new _ _ () invoked")
# 	def __init__(self):
# 		print("B's _ _ init _ _ () invoked")
# def main():
# 	a = A()
# 	b = B()
	




# class A:
# 	def abc(self):
# 		print("I am a parent class function")

# class B(A):
# 	def abc(self):
# 		print("I am a child class function")
	

# class C(A):
# 	def abc(self):
# 		A.abc(self)


# b = B() 
# c = C()
# b.abc()
# c.abc()










# s1 = {1,3,2}
# s2 = {1,2,3}
# print(s1,s2)
# def recursive_factorial(num):
# 	if num == 0:
# 		return 1
# 	else :
# 		return num * recursive_factorial(num - 1)

# print(recursive_factorial(4))



def f(n):
	if n > 0 :
		print(n % 10 )
		f(n // 10 )

f( 123456 )


