from pickle import dumps, loads
from statistics import mean
from sys import exit

# ---------- CONSTANTS ------------
SEPARATOR1 = "="
SEPARATOR2 = ","
KEY1 = "Student name"
KEY2 = "Mark"
KEY3 = "Email"
KEY4 = "Phone"
LOWEST_MARK = 0
HIGHEST_MARK = 10


# --------- ERROR FUNCTIONS ------------


class StudentNotFoundError(ValueError):
    """Raised when a student is not found in the list
    Attributes:
        student -- the given student
        message -- explanation of the error
    """

    def __init__(
        self, student, message="The student you are trying to find does not exist: "
    ):
        self.student = student
        self.message = "StudentNotFoundError:" + message + student + ".\n"
        self.message += "Check spelling and try again."
        self.message += "Note that the name must be between double quotes."
        super().__init__(self.message)


class InvalidMarkError(ValueError):
    """
    Raised when a mark is not valid, above or below the range of 0-10
    Attributes:
        mark -- the given mark
        message -- explanation of the error
    """

    def __init__(self, mark, message="The mark you are trying to add is invalid: "):
        self.mark = mark
        self.message = "InvalidMarkError:" + message + str(mark) + "."
        super().__init__(self.message)


class FileFormatError(AttributeError):
    """
    Raised when the file format is not valid
    Attributes:
        file -- the given file
        message -- explanation of the error
    """

    def __init__(self, file, message="The file format is not valid: "):
        self.file = file
        self.message = "FileFormatError:" + message + file + "."
        super().__init__(self.message)


class InvalidCommandError(Exception):
    """
    Raised when the command is not valid
    """

    def __init__(self, command=" "):
        self.command = command
        self.message = f"Error: Command not valid: {command}\n"
        self.message += "Instructions:\n"
        self.message += "First load a correct file.\n"
        self.message += "-r <text filename>: loads <text filename> and adds this database, replacing a existing student when there is a match\n"
        self.message += "-s <student name>: shows data from <student name>. Name must be between double quotes.\n"
        self.message += (
            "-m: shows a list of students with their grades from high to low\n"
        )
        self.message += "-p <mark>: calculate the number of students above the given threshold grade\n"
        self.message += "-a: calculates the average of the grades for the whole class\n"
        self.message += "-o: shows students with above average grades\n"
        super().__init__(self.message)


# ------------ GENERAL FUNCTIONS ------------


def read_config_file(config_file="./students.cfg"):
    """
    Reads a configuration file and returns its content
    config_file(str): the file to be read
    """
    try:
        with open(config_file, "r") as file:
            data = file.readline()
        key, filename = data.strip().split(SEPARATOR1)
        filename = filename.strip()
        if not filename:
            raise FileNotFoundError
        return filename
    except FileNotFoundError as e:
        print(e)

    except ValueError:
        print("The file format is not valid: ", config_file)
        exit()


def binfile_to_dict(filename):
    """
    Reads a binary file and returns its content as a dictionary
    filename(str): the file to be read
    """
    try:
        with open(filename, "rb") as myfile:
            read_data = myfile.read()

            data = loads(read_data)
            return data

    except ValueError:
        raise FileFormatError(filename)


def dict_to_binfile(mydict, filename):
    """
    Writes a dictionary to a binary file
    filename(str): the file to be written
    mydict(dict): the dictionary to be written
    """
    try:
        with open(filename, "ab") as myfile:
            data = dumps(mydict)

            myfile.write(data)

    except ValueError:
        raise FileFormatError("Invalid data format in file: ", filename)


def remove_blank_last_line(filename):
    """
    Removes the last line of a file if it is blank
    filename(str): the file to be read
    """
    try:
        with open(filename, "r+") as file:
            lines = file.readlines()

        if lines and lines[-1].strip() == "":
            lines.pop()

        return lines

    except ValueError:
        raise FileFormatError(filename)


def check_repeated_names(mydict):
    """
    Checks if there are repeated names in a dictionary
    mydict(dict): the dictionary to be checked
    """
    names = [elem[KEY1] for elem in mydict]
    set_names = set(names)
    if len(names) != len(set_names):
        print("There are repeated names in the file.")
        print("Please check the file and load it again.")


def textfile_to_dict(filename):
    """
    Reads a text file and returns its content as a dictionary
    filename(str): the file to be read
    """
    try:
        file_as_dict = []
        clean_lines = remove_blank_last_line(filename)
        for myline in clean_lines:
            dict_student = {}
            split_line = myline.split(SEPARATOR2)

            dict_student[KEY1] = split_line[0].strip()
            dict_student[KEY2] = split_line[1].strip()
            dict_student[KEY3] = split_line[2].strip()
            dict_student[KEY4] = split_line[3].strip()
            file_as_dict.append(dict_student)
        return file_as_dict

    except IndexError:
        raise FileFormatError(filename)


def calculate_average(mydict):
    """
    Calculates the average of the marks in a dictionary
    data(str): the dictionary to be calculated
    """
    try:
        my_list = []
        for elem in mydict:
            my_list.append(float(elem[KEY2]))
        return mean(my_list)
    except ValueError:
        raise InvalidMarkError(message="The mark has no the correct format")


def order_function(mydict):
    """
    Returns the value to be order by in a dictionary
    mydict(dict): the dictionary to be ordered
    """
    return mydict[KEY2]


# ---------- COMMAND FUNCTIONS ---------


# COMMAND -r FUNCTION
def loads_data(filename):
    """
    Reads a configuration file and saves the data from filename into the file pointed inside configuration file
    filename(str): the file to be saved
    """
    try:
        mydict = textfile_to_dict(filename)
        check_repeated_names(mydict)
        data_file = read_config_file()
        dict_to_binfile(mydict, data_file)

        return
    except AttributeError:
        raise FileFormatError(filename)
    except FileNotFoundError as e:
        print(e)
        exit()


# COMMAND -s FUNCTION
def student_data(studentname):
    """
    Shows the data of a student
    studentname(str): the name of the student to be shown
    """
    try:
        data_file = read_config_file()
        mydict = binfile_to_dict(data_file)

    except FileNotFoundError:
        print("There is not data file. Please load a data file first.")
        exit()
    found_students_counter = 0
    for elem in mydict:
        if elem[KEY1].lower().find(studentname.lower()) > -1:
            print(", ".join(elem.values()))
            found_students_counter += 1
    if found_students_counter == 0:
        raise StudentNotFoundError(studentname)

    return


# COMMAND -m FUNCTION
def marks_datalist():
    """
    Shows the list of students with their marks ordered from high to low
    """
    try:
        data_file = read_config_file()
        mydict = binfile_to_dict(data_file)
        ordered_dict = sorted(mydict, key=order_function, reverse=True)
        for elem in ordered_dict:
            print(elem[KEY1], elem[KEY2])

        return

    except FileNotFoundError:
        print("There is not data file. Please load a data file first.")


# COMMAND -p FUNCTION
def students_mark(mark):
    """
    Shows the students above the given mark
    mark(int): the mark to be searched
    """
    try:
        data_file = read_config_file()
        mydict = binfile_to_dict(data_file)
    except FileNotFoundError:
        print("There is not data file. Please load a data file first.")

    if not isinstance(mark, int) and not isinstance(mark, float):
        raise InvalidMarkError(mark)

    if mark < LOWEST_MARK or mark > HIGHEST_MARK:
        raise InvalidMarkError(mark)

    else:
        mymark = float(mark)

        for elem in mydict:
            if float(elem[KEY2]) > mymark:
                print(elem[KEY1])
        return


# COMMAND -a FUNCTION
def average_mark():
    """
    Shows the average mark of the students
    """
    try:
        data_file = read_config_file()
        mydict = binfile_to_dict(data_file)
        print(calculate_average(mydict))
        return
    except FileNotFoundError:
        print("There is not data file. Please load a data file first.")


# COMMAND -o FUNCTION
def students_above_average():
    """
    Shows the students above the average mark
    """
    try:
        data_file = read_config_file()
        mydict = binfile_to_dict(data_file)
        avg_mark = float(calculate_average(mydict))
        for elem in mydict:
            if float(elem[KEY2]) > avg_mark:
                print(elem[KEY1])
        return
    except FileNotFoundError:
        print("There is not data file. Please load a data file first.")
