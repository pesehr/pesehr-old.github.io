
import sys

# function gets a file name and mode and opens file using the given parameters
# after that returns the file object
def load_file(file_name, mode = "r"):
	try:
		f = open(file_name, mode)
		return f
	except:
		print("file does not exist")
		sys.exit(1)

# function gets file object, student's name and grade
# write information to file
def add_new_student(_file,name, grade):
	try:
		_file.write("{0}-{1}\n".format(name,grade))
	except:
		print("file is not writable")

# function get file object and a name and search for the student in the file.
# if the information exists in the file, the function returns name and grade
def search_name(_file, name):
	try:
		line = _file.readline()
		while line != "":
			student = line.split("-")
			if student[0] == name:
				return student[0],student[1][0:1]
			line = _file.readline()
	except:
		print("file is not readable")


def main():
    order = ""
    try:
        while order != "e" :
            order = input("Please enter your command: (a: add new student, s:search for student, e:exit)\n")
            if order == "a":
                name = input("please enter the student's name: ")
                grade = input("please enter the student's grade: ")
                file = load_file(sys.argv[1],"a")
                add_new_student(file,name,grade)
            elif order == "s":
                name = input("please enter the student's name: ")
                file = load_file(sys.argv[1], "r")
                grade = search_name(file,name)
                if grade != None:
                    print(name, grade)
                else:
                    print("Student not found!")
    except IndexError as e:
        print("Please enter a valid file name!")


main()
