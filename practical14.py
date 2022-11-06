import sys
import os

def copyFiles(readFile, writeFile):
	lines_list = readFile.readlines()
	total_lines = len(lines_list)

	i = 0;
	while i < total_lines:
		writeFile.write(lines_list[i])
		i +=2;
	print("data of alternate lines copied successfully :-)")


def main():
	no_of_files = len(sys.argv)
	more = True;

	try:
		if(no_of_files == 3 ):
			if(os.path.exists(sys.argv[1])):
				if sys.argv[1] == sys.argv[2]:
					raise NameError
				else:
					file1 = open(sys.argv[1], "r")
					file2 = open(sys.argv[2], "w")
					print("reading from file :", sys.argv[1] )
					print("writing from file :", sys.argv[2] )
					more = False
					copyFiles(file1, file2)
					file1.close()
					file2.close()
			else:
				raise Exception
		else:
			file1 = input("Enter the readfile name ")
			file2 = input("Enter the writefile name ")
			if(os.path.exists(file1)):
				if file1 == file2:
					raise NameError
				else:
					read_file = open(file1, "r")
					write_file = open(file2, "w")
					print("reading from file :", file1 )
					print("writing from file :", file2 )
					more = False
					copyFiles(read_file, write_file)
					read_file.close()
					write_file.close()
			else:
				raise Exception
	
	except NameError as e:
		print("Read and write files cannot be same ")
	except Exception as e:
		print("Read file doesn't exists.")
	

	# file1.close()
	# file2.close()

main()


