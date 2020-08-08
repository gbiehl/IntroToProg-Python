# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# GBiehl,08.07.2020,Added code to complete all steps
# GBiehl,08.08.2020,Adjusted the for loop in choice 4
# 
# ------------------------------------------------------------------------ #
#
# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
# row - a single row in ToDoList.txt
strData = ''   # A row of text data from the file
dicRow = {}    # A row of data containing Task and Priority
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ''   # A menu of user options
strChoice = '' # A Capture the user option selection
strTask = ''    # The task to add or delete
strPri =''      # The priority of the task being added
booFound = False   # Boolean for when task is found or not found
#
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here --- Completed
# This program assumes ToDoList.txt exists at the start
objFile = open("ToDoList.txt","r")
for row in objFile:
    strData = row.split(",")               # Reads one row from the file and removes the commas
    dicRow = {"Task": strData[0],"Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()
#
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user --- Completed
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
        # TODO: Add Code Here --- Completed
        for dicRow in lstTable:
            print(dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here -- Completed
        strTask = str(input('What task should be added?: '))
        strPri = str(input('What priority should it have?: '))
        dicRow = {"Task": strTask, "Priority": strPri}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here --- Completed
        strTask = str(input('What task should be removed?: '))   # using a row number in the table would be better
        booFound = False
        for dicRow in lstTable:
            if dicRow["Task"] == strTask:
                lstTable.remove(dicRow)
                print("Entry removed")   # Prints again for duplicate entries+
                booFound = True
                continue
        if (booFound == False):      # Notifies user if requested deletion didn't happen
            print('Entry not found. Nothing  deleted. Check your typing.')
            continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here --- Completed
        objFile = open('ToDoList.txt', 'w')
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here -- Completed
        print('Goodby')
        break                   # and Exit the program