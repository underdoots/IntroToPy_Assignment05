# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Andrew Collins>,<18-Nov-20>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFileName = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# <CODE ADDED by Andrew Collins>

objFile = open(objFileName, "r") #load file, append future data as table in dictionary
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# for row in objFileName: WHY IS THIS WRONG?
#     strData = row.split(",")
#     dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
#     lstTable.append(dicRow)
# objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # <CODE ADDED by Andrew Collins>
        print("Here is what's on your Task List")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
            print ("--------------------")
        continue
    # Step 4 - Add a new item to the list/Table by getting user input
    elif (strChoice.strip() == '2'):
        # TODO: <CODE ADDED by Andrew Collins>
        #print ("Enter a new task: ")
        strTask = str(input("Enter a new task: ").strip())
        strPriority = str(input("What is the task priority? [high | low] ")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print ("Current Data in Task list: ")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: <CODE ADDED by Andrew Collins>
        strTaskRemove = input("Which task to remove?")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strTaskRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
        if (blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: <CODE ADDED by Andrew Collins>
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
                input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
