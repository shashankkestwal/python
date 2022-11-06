def length_of_strings(s1 ,s2, s3):
	l1 = len(s1)
	l2 = len(s2)
	l3 = len(s3)
	return l1, l2, l3

def maximum_string(s1, s2, s3):
	if s1 > s2 and s1 > s3:
		return s1
	elif s2 > s1 and s2 > s3:
		return s2
	else :
		return s3

def replace_vowels_with_hash(s):
	vowel = "AEIOUaeiou"
	for ele in vowel:
		s = s.replace(ele, "#")
	return s

def count_alphabets(s) :
	words_count = 0
	for ele in s:
		if ele.isalpha():
			words_count += 1
	return words_count
	
def check_string_palindrome(s) :
	s = s.lower()
	if len(s) == 1 :
		return False
	elif len(s) == 2 and s[0] == s[1]:
		return True
	else:
		for i in range(len(s),0,-1):
			if s == s[::-1]:
			 	return True
			else:
				return False


def main ():
	print("Program to perform various operations on a string")
	string1 = input("Enter string1 :")
	if len(string1) == 0:
		print("Empty string is not allowed")
		exit()
	string2 = input("Enter string2 :")
	if len(string2) == 0:
		print("Empty string is not allowed")
		exit()
	string3 = input("Enter string3 :")
	if len(string3) == 0:
		print("Empty string is not allowed")
		exit()

	while True:
		print("\n\na)Find the length of string.")
		print("b)Return maximum of three strings.")
		print("c)Accept a string and replace all vowels with “#”")
		print("d)Find number of words in the given string.")
		print("e)Check whether the string is a palindrome or not.")
		print("f)Exit the program")
		choice = input("Enter the operation you want to perform :")

		if choice == 'a':
			length1, length2, length3 = length_of_strings(string1, string2, string3)
			print("Length of string 1 is :", length1)
			print("Length of string 2 is :", length2)
			print("Length of string 3 is :", length3)
		elif choice == 'b':
			max_string = maximum_string(string1, string2, string3)
			print("Maximum of the two string is :", max_string)
		elif choice == 'c':
			replaced_string1 = replace_vowels_with_hash(string1)	
			replaced_string2 = replace_vowels_with_hash(string2)	
			replaced_string3 = replace_vowels_with_hash(string3)
			print("Strings after replacing the vowels with # ")
			print(replaced_string1,"   ",replaced_string2,"   ",replaced_string3)	
		elif choice == 'd':
			word_count_string1 = count_alphabets(string1)
			word_count_string2 = count_alphabets(string2)
			word_count_string3 = count_alphabets(string3)
			print("The number of counts in string1 , string2 and string3 respectively are ")
			print(word_count_string1,"   ",word_count_string2,"   ",word_count_string3,"   ")
		elif choice == 'e':
			is_palindrome1 = check_string_palindrome(string1)
			if is_palindrome1:
				print("String1 is a palindrome ")
			else:
				print("String1 is not a palindrome")

			is_palindrome2 = check_string_palindrome(string2)
			if is_palindrome2:
				print("String2 is a palindrome ")
			else:
				print("String2 is not a palindrome")

			is_palindrome3 = check_string_palindrome(string3)
			if is_palindrome3:
				print("String3 is a palindrome ")
			else:
				print("String3 is not a palindrome")
		elif choice == 'f':
			print("exit")
			exit()
		else :
			print("Invalid input ")
			exit()
	
if __name__ == '__main__':
	main()