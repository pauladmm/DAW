import pdmm_library as lib
from sys import argv, exit

LOAD_DATA_COMMAND = "-r"
STUDENT_DATA_COMMAND = "-s"
STUDENTS_MARKS_COMMAND = "-m"
STUDENTS_WITH_MARK_COMMAND = "-p"
AVERAGE_MARK_COMMAND = "-a"
STUDENTS_OVER_AVERAGE_COMMAND = "-o"
COMMANDS_WITHOUT_ARGUMENTS = ["-a", "-m", "-o"]


def main(command, optional_argument=None):
    """
    Executes a function for a specific command.

    Parameters:
        command (str): The command to execute.
        optional_argument (any, optional): An optional argument required for the command.

    Raises:
        FileFormatError: If there is an error with the file format.
        StudentNotFoundError: If a student is not found.
        InvalidMarkError: If the mark is invalid.
        InvalidCommandError: If the command is invalid.


    """

    if command == LOAD_DATA_COMMAND:
        try:
            lib.loads_data(optional_argument)

        except lib.FileFormatError as e:
            print(e.message)

    elif command == STUDENT_DATA_COMMAND:
        try:
            lib.student_data(optional_argument)
        except lib.StudentNotFoundError as e:
            print(e.message)

    elif command == STUDENTS_MARKS_COMMAND:
        lib.marks_datalist()

    elif command == STUDENTS_WITH_MARK_COMMAND:
        try:
            lib.students_mark(optional_argument)
        except lib.InvalidMarkError as e:
            print(e.message)
            print("The mark must be a number between 0 and 10.")

    elif command == AVERAGE_MARK_COMMAND:
        lib.average_mark()

    elif command == STUDENTS_OVER_AVERAGE_COMMAND:
        lib.students_above_average()

    else:
        print(lib.InvalidCommandError(command).message)
        exit()


if len(argv) == 2:
    if argv[1] not in COMMANDS_WITHOUT_ARGUMENTS:
        print(lib.InvalidCommandError(argv[1]).message)
        exit()
    else:
        main(argv[1])
elif len(argv) == 3:
    main(argv[1], argv[2])
else:
    print(lib.InvalidCommandError().message)
    exit()
