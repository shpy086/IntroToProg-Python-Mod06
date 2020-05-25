# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# SHuang, 5.23.2020,Modified code to complete assignment 6
# SHuang, 5.23.2020,Updated processor code and got file path error. Checked file and start script was in downloads
# SHuang, 5.23.2020,Moved starter script to Assignment06 folder and file opened successfully
# Shuang, 5.23.2020,Completed Processor class code and IO class code
# Shuang, 5.23.2020,Updated code in main body of script to finalize program
# Shuang, 5.23.2020,Ran program and 'remove item' option not working correctly. Need to troubleshoot
# Shuang, 5.24.2020,Fixed remove_data_from list function
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows

        """
        list_of_rows.clear()  # clear current data
        objFile = open(file_name, "r")
        for line in objFile:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        objFile.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds row of data to list of rows

        :param task: (string) task to be completed
        :param priority: (string) priority of task
        :param: (list) list of rows to be filled with file data
        :return: (list) of dictionary rows

        """
        dicRow = {"Task": task.strip(), "Priority": priority.strip()}
        list_of_rows.append(dicRow)  # this code was similar to the 'add item' code from Assignment5
        print("Task added to list! ")
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(strTask, list_of_rows):
        """ removes row of data to list of rows

            :param task: (string) task to be completed
            :param: (list) list of rows to be filled with file data
            :return: (list) of dictionary rows
        """
        strStatus = False
        for task in list_of_rows:
            if strTask.lower() == task["Task"].lower():
                list_of_rows.remove(task)
                strStatus = True
        if strStatus == True:
            print("Task removed successfully! \n")
        else:
            print("Task does not exist \n")  # this code block is also similar to 'remove item' code in /
        print("Remaining Tasks: ")
        for task in list_of_rows:
            print(task['Task'] + ',' + task['Priority'])
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data a file into a list of dictionary rows

             :param file_name: (string) with name of file:
             :param list_of_rows: (list) you want filled with file data:
             :return: (list) of dictionary rows

             """
        objFile = open(file_name, "w")
        for row in list_of_rows:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        print("All items have been saved.")
        objFile.close()  # TODO: Add Code Here!
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: ******* \n")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        task = input("Name of task: ")
        priority = input("Priority level: ")
        return task, priority  # TODO: Add Code Here!
        # return task, priority

    @staticmethod
    def input_task_to_remove():
        task = input("Which task would you like to remove? ")
        return task  # TODO: Add Code Here!


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(task, priority, lstTable)  # TODO: Add Code Here
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        Processor.remove_data_from_list(task, lstTable)  # TODO: Add Code Here
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)  # TODO: Add Code Here!
            IO.input_press_to_continue(strStatus)
            print("Your data has been saved! ")
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName, lstTable)  # TODO: Add Code Here!
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
