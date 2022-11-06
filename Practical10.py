def counting_words(string):
	word_count_dictionary = {}
	for ele in string:
		if (ele in word_count_dictionary.keys()) :
			word_count_dictionary[ele] += 1
		else :
			word_count_dictionary[ele] = 1
	return word_count_dictionary			


def main():
	input_string = input("Enter the sentence :")
	word_count_dictionary = counting_words(input_string)
	print("The word counts is :",word_count_dictionary)

if __name__ == '__main__':
	main()