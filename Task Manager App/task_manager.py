#=====IMPORTING LIBRARIES===========

import re
from datetime import datetime


#====FUNCTIONS====
    
# Admin menu
def admin_menu():
    # Menu for 'admin' with feature to register new users and view user and task stats
    menu = input('''\nPlease select one of the following options:
r\t- register user
a\t- add task
va\t- view all tasks
vm\t- view my tasks
gr\t- generate reports
ds\t- display statistics
e\t- exit
: ''').lower()

    # Logic for 'register' section
    if menu == "r":
        reg_user()

    # Logic for 'add task' section
    elif menu == "a":
        add_task()

    # Logic for 'view all tasks' sections
    elif menu == "va":
        view_all()

    # Logic for 'view my tasks' section
    elif menu == "vm":
        view_mine()

    # Logic for 'generate reports' section
    elif menu == "gr":
        gen_reports()

    # Logic for 'display statistics' section
    elif menu == "ds":
        display_stats()

    # Exit program        
    elif menu == "e":
        print(f"\nGoodbye!!!")
        exit()

    # Option for accidental input
    else:
        print("You have made a wrong choice, Please Try again")


# Non-admin menu
def non_admin_menu():
    # Limited menu for non-administrative users
    menu = input('''\nPlease select one of the following options:
a\t- add task
va\t- view all tasks
vm\t- view my tasks
e\t- exit
: ''').lower()

    # Logic for 'add task' section
    if menu == "a":
        add_task()

    # Logic for 'view all tasks' sections
    elif menu == "va":
        view_all()

    # Logic for 'view my tasks' section
    elif menu == "vm":
        view_mine()

    # Exit program        
    elif menu == "e":
        print(f"\nGoodbye!!!")
        exit()

    # Option for accidental input
    else:
        print("You have made a wrong choice, Please Try again")


# Register user
def reg_user():
    # User input for username and password
    new_username = input("Please enter a new username: ")

    # Check if username exists
    while new_username in login_details.keys():
        print("\nSorry, this user already exists.")
        new_username = input("Please enter a new username: ")

    new_password = input("Please enter a new password: ")
    new_password_validation = input("Please re-enter your new password: ")

    # Logic to validate password
    while new_password_validation != new_password:
        print("\nThe passwords do not match. Please try again.")
        new_password = input("Please enter a new password: ")
        new_password_validation = input("Please re-enter your new password: ")
    print(f"\nCongratulations, you have registered the new user '{new_username}'.\n")

    # Append new user to 'user.txt' file
    with open ("user.txt", "a", encoding = "utf-8") as f:
        f.write(f"\n{new_username}, {new_password}")


# Add task
def add_task():
    # User input for task entry fields
    task_user = input("\nEnter the username of the person whom the task is assigned to: ")
    task_title = input("Enter a title of the task: ")
    task_description = input("Enter a description of the task: ")
    today = datetime.today().strftime("%d %b %Y")
    task_duedate = input("Enter a due date for the task: ")
    task_complete = "No"
    print("\nYou have successfully added a new task.")

    # Append task to 'tasks.txt' file
    with open ("tasks.txt", "a", encoding = "utf-8") as f:
        f.write(f"\n{task_user}, {task_title}, {task_description}, {today}, {task_duedate}, {task_complete}")


# View all tasks
def view_all():
    # Read all tasks, delimit line by line and create a list to output all values
    with open ("tasks.txt", "r", encoding = "utf-8") as f:
        for line in f:
            line_items = re.split(r', |\n', line)
            underscore = "—" * 79
            print(f"\n{underscore}\nTask\t\t\t{line_items[1]}\nAssigned to:\t\t{line_items[0]}\nDate assigned:\t\t{line_items[3]}\nDue date:\t\t{line_items[4]}\nTask complete:\t\t{line_items[5]}\nTask description:\t{line_items[2]}\n{underscore}")


# View my tasks
def view_mine():
    # Read all tasks, delimit line by line and create a list to output specific values
    with open ("tasks.txt", "r", encoding = "utf-8") as f:
        my_tasks = []
        underscore = "—" * 79

        for line in f:
            line = line.strip().split(", ")
            if line[0].lower() == username.lower():
                my_tasks.append(line)

        # Print message if there are no available tasks
        if len(my_tasks) == 0:
            print("\nYou have no pending tasks.")
        else:
            # Add counter to tasks and print output
            for count, task in enumerate(my_tasks):
                print(f"\n{underscore}\nTask number:\t\t{count + 1}\nTask:\t\t\t{my_tasks[count][1]}\nAssigned to:\t\t{my_tasks[count][0]}\nDate assigned:\t\t{my_tasks[count][3]}\nDue date:\t\t{my_tasks[count][4]}\nTask complete?\t\t{my_tasks[count][5]}\nTask description:\t{my_tasks[count][2]}\n{underscore}")

            # Task selection
            select_task = int(input("Would you like to select a specific task? Type -1 to exit: "))
            if select_task == -1:
                pass
            else:
                # Change user input to index value
                count = select_task - 1

                # Check if task has already been completed
                if my_tasks[count][5] == "Yes":
                    print("\nSorry, this task has already been completed.")
                else:

                    # Menu to select edit option
                    select_menu = input('''\nPlease select one of the following options:
    m\t- mark the task as complete
    ed\t- edit the task
    : ''').lower()

                    # Logic for 'task completed' section
                    if select_menu == "m":

                        # Store original task string
                        original_task = ", ".join(my_tasks[count])

                        # Change 'No' to 'Yes'
                        my_tasks[count][5] = "Yes"
                        updated_task = ", ".join(my_tasks[count])

                        # Replace 'No' to 'Yes' in 'tasks.txt' file
                        with open ("tasks.txt", "r", encoding = "utf-8") as f:
                            # Read entire file content
                            data = f.read()
                            # Search and replace
                            data = data.replace(original_task, updated_task)

                        with open ("tasks.txt", "w", encoding = "utf-8") as f:
                            # Write replaced data
                            f.write(data)
                        
                        # Print confirmation message to console
                        print("\nTask successfully marked as complete.")

                    # Logic for 'edit the task' section
                    elif select_menu == "ed":

                        select_submenu = input('''\n Please select one of the following options:
    u\t- change the username of the person to whom the task is assigned
    d\t- change the due date of the task
    : ''').lower()

                        # Logic for 'change assigned user' section
                        if select_submenu == "u":

                            # Store original task
                            original_task = ", ".join(my_tasks[count])

                            # Enter the username of the new user
                            change_username = input("\nEnter the username of the new user: ")

                            # Check if the username entered is already the assigned user
                            if change_username.lower() == my_tasks[count][0].lower():
                                print(f"\nError!!! The task is already assigned to {change_username}.")
                            # Check if the username entered is a registered user
                            elif change_username.lower() not in login_details.keys():
                                print(f"\nError!!! This user does not exist.")
                            # Change the username in the list
                            else:
                                my_tasks[count][0] = change_username
                                
                                # Store updated task string
                                updated_task = ", ".join(my_tasks[count])

                                # Replace original username to updated username in 'tasks.txt' file
                                with open ("tasks.txt", "r", encoding = "utf-8") as f:
                                    # Read entire file content
                                    data = f.read()
                                    # Search and replace
                                    data = data.replace(original_task, updated_task)

                                # Write replaced data
                                with open ("tasks.txt", "w", encoding = "utf-8") as f:
                                    f.write(data)

                                print(f"\nTask successfully assigned to '{change_username}'.")
                        
                        elif select_submenu == 'd':

                            # Store original task
                            original_task = ", ".join(my_tasks[count])

                            # Enter the new due date
                            new_date = input("Please enter the new due date as 'DD MMM YYYY': ")

                            # Check if the new due date is not the same as the old due date
                            while new_date == my_tasks[count][4]:
                                print(f"\nError!!! This due date already exists")
                                new_date = input("Please enter the new due date as 'DD MMM YYYY': ")
                            
                            # Change the due date in the list
                            my_tasks[count][4] = new_date

                            # Store updated task string
                            updated_task = ", ".join(my_tasks[count])

                            # Replace original due date to updated due date in 'tasks.txt' file
                            with open ("tasks.txt", "r", encoding = "utf-8") as f:
                                # Read entire file content
                                data = f.read()
                                # Search and replace
                                data = data.replace(original_task, updated_task)

                            # Write replaced data
                            with open ("tasks.txt", "w", encoding = "utf-8") as f:
                                f.write(data)

                            print(f"\nDue date successfully changed to '{new_date}'.")


# Generate reports
def gen_reports():
    task_overview()
    user_overview()

    print(f"\nReports generated successfully.")


# Task overview report
def task_overview():
    
    # Counters
    total_tasks = 0
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0

    with open ("tasks.txt", "r", encoding = "utf-8") as f:
        for line in f:
            
            # Count number of tasks
            total_tasks += 1
            line = line.strip().split(", ")
            
            # Count number of completed/incompleted tasks
            if line[5] == "Yes":
                completed_tasks += 1
            elif line[5] == "No":
                incomplete_tasks += 1
            
            # Count number of incomplete and overdue tasks
            duedate = datetime.strptime(line[4], '%d %b %Y').date()
            today = datetime.today().strftime('%Y-%m-%d')
            today = datetime.strptime(today, '%Y-%m-%d').date()
            if line[5] == "No" and duedate < today:
                overdue_tasks += 1

    # Percentage of completed/incompleted tasks
    pct_incomplete = (incomplete_tasks / total_tasks) * 100
    pct_overdue = (overdue_tasks / total_tasks) * 100

    # Write 'task_overview' text file
    with open ("task_overview.txt", "w", encoding = "utf-8") as f:
        f.write(f"TASK OVERVIEW\n\n")
        f.write(f"Total number of tasks:\t\t {total_tasks}\n")
        f.write(f"Number of completed tasks:\t {completed_tasks}\n")
        f.write(f"Number of incompleted tasks:\t {incomplete_tasks}\n")
        f.write(f"Number of overdue tasks:\t {overdue_tasks}\n")
        f.write(f"Percentage of completed tasks:\t {pct_incomplete:.2f} %\n")
        f.write(f"Percentage of overdue tasks:\t {pct_overdue:.2f} %\n")


# User overview report
def user_overview():

    # Counters
    user_num = 0
    total_tasks = 0
    user_tasks = {}

    with open ("user.txt", "r", encoding = "utf-8") as f_user:
        with open ("tasks.txt", "r", encoding = "utf-8") as f_tasks:
            for line in f_user:
                line = line.strip().split(", ")
                
                # Total registered users
                user_num += 1
                
                # Append users to a dictionary with a counter of 0
                user_tasks[line[0]] = {'tasks' : 0, 'completed' : 0, 'incompleted' : 0, 'overdue' : 0}

            for line in f_tasks:
                line = line.strip().split(", ")
                
                # Total number of tasks
                total_tasks += 1
               
                # Add count to a users task
                user_tasks[line[0]]['tasks'] += 1
                if line[0] in user_tasks:
                    if line[5] == "Yes":
                        user_tasks[line[0]]['completed'] += 1
                    elif line[5] == "No":
                        user_tasks[line[0]]['incompleted'] += 1
                
                # Count number of incomplete and overdue tasks
                duedate = datetime.strptime(line[4], '%d %b %Y').date()
                today = datetime.today().strftime('%Y-%m-%d')
                today = datetime.strptime(today, '%Y-%m-%d').date()
                if line[5] == "No" and duedate < today:
                    user_tasks[line[0]]['overdue'] += 1

    # Write 'user_overview' text file
    with open ("user_overview.txt", "w", encoding = "utf-8") as f:
        f.write(f"USER OVERVIEW\n\n")
        f.write(f"Total number of registered users:\t\t{user_num}\n")
        f.write(f"Total number of tasks:\t\t\t\t{total_tasks}\n\n")
        
        for key in user_tasks:
            f.write(f"Username:\t\t\t\t\t{key}\n")
            f.write(f"Number of assigned tasks:\t\t\t{user_tasks.get(key).get('tasks')}\n")
            f.write(f"Percentage of total number of assigned tasks:\t{(((user_tasks.get(key).get('tasks')) / total_tasks) * 100):.2f} %\n")
            
            if user_tasks.get(key).get('tasks') == 0:
                f.write(f"Percentage of completed assigned tasks:\t\tN/A\n")
            else:
                f.write(f"Percentage of completed assigned tasks:\t\t{((user_tasks.get(key).get('completed') / user_tasks.get(key).get('tasks')) * 100):.2f} %\n")
            
            if user_tasks.get(key).get('tasks') == 0:
                f.write(f"Percentage of incompleted assigned tasks:\tN/A\n")
            else:
                f.write(f"Percentage of incompleted assigned tasks:\t{((user_tasks.get(key).get('incompleted') / user_tasks.get(key).get('tasks')) * 100):.2f} %\n")

            if user_tasks.get(key).get('tasks') == 0:
                f.write(f"Percentage of overdue assigned tasks:\t\tN/A\n\n")
            else:
                f.write(f"Percentage of overdue assigned tasks:\t\t{((user_tasks.get(key).get('overdue') / user_tasks.get(key).get('tasks')) * 100):.2f} %\n\n")


def display_stats():
    gen_reports()
    underscore = "—" * 79

    # Print 'task_overview.txt'
    with open ("task_overview.txt", "r", encoding = "utf-8") as f:
        print(f"\n{underscore}\n")
        for line in f:
            line = line.strip()
            print(line)
        print(f"\n{underscore}\n")

    # Print 'user_overview.txt'
    with open ("user_overview.txt", "r", encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            print(line)
        print(underscore)


#====LOGIN SECTION====

login_details = {}

# Compile usernames and passwords to dictionary
with open ("user.txt", "r", encoding = "utf-8") as f:
    for line in f:
        line = line.strip().split(", ")
        login_details.update({line[0]:line[1]})

# Login verification
username = input("Please enter your username: ")
while username not in login_details.keys():
    username = input("Username not found. Please try again: ")

password = input("Please enter your password: ")
while password != login_details[username]:
    password = input("Incorrect password. Please try again: ")

print(f"Login successful. Welcome {username}.")

# Select appropriate menu        
while True:

    # if statement for the user 'admin'
    if username == 'admin':
        admin_menu()
    
    # if statement for all other users
    else:
        non_admin_menu()