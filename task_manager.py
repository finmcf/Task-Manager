#=====importing libraries===========
import datetime

#import module to help check if given files exist

from os.path import exists


#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

#initialise function to generate the tasl_overview file

def generate_task_overview():

    #open task_overview in write setting

    with open("task_overview.txt", "w") as task_overview:

            #open tasks in read setting

            with open("tasks.txt", "r") as task_dataset:

              #create a list of each line of tasks

              task_data_lines = task_dataset.read().splitlines()

              #initalise counters for number of completed, uncompleted and overdue tasks

              completed_tasks = 0

              uncompleted_tasks = 0

              overdue_tasks = 0

              #get the total number of tasks

              total_tasks = len(task_data_lines)

              #loop through each task line

              for line in task_data_lines:

                #split each task into a list containing each piece of data about it

                task_data = line.split(", ")

                #get the due date from the task

                due_date = datetime.datetime.strptime(task_data[4], "%d %b %Y")

                #get the current date

                current_date = datetime.datetime.now()

                #check if the task is completed, if so increase completed_tasks by 1

                if task_data[5] == "Yes":

                    completed_tasks += 1

                #check if the task is completed and it is overdue, if so increase completed_tasks and overdue_tasks by 1


                elif task_data[5] == "No" and due_date < current_date:

                    uncompleted_tasks += 1

                    overdue_tasks += 1

                #check if the task is incomplete, if so increase uncompleted_tasks by 1

                elif task_data[5] == "No":

                    uncompleted_tasks += 1

              #with the counters of the tasks, write into the task_overview file all of the information

              task_overview.write(f"""Total Tasks: {str(total_tasks)}
Completed Tasks: {completed_tasks}
Uncompleted Tasks: {uncompleted_tasks}
Overdue Tasks: {overdue_tasks}
Percentage Incomplete: {round((uncompleted_tasks / total_tasks) * 100, 2)}%
Percentage Overdue: {round((overdue_tasks / total_tasks) * 100, 2)}%""")


              #close the file

              task_dataset.close()

            #close the task_ovewview file

            task_overview.close()

            

#initalise function to generate the user_overview file

def generate_user_overview():

    #initialise and empty string containing the text to write to this file

    file_to_write = ""

    #open user.txt in read mode

    with open("user.txt", "r") as all_users:

            #get a list of each user and their password

            user_information = all_users.read().splitlines()

            #for each user in the list

            for task_user in user_information:

                #split the user string into a list of their username and password, and get the username

                name = task_user.split(", ")[0]

                #intialise variables containing the each counts of completed, uncompleted and overdue tasks
                #for the user

                user_task_count = 0

                user_task_completed_count = 0

                user_task_uncompleted_count = 0

                user_task_overdue_count = 0

                #open the tasks.txt file in read mode

                with open("tasks.txt", "r") as user_tasks:

                    #get a list of each task

                    user_task_lines = user_tasks.read().splitlines()

                    #loop through each task

                    for line in user_task_lines:

                        #for each task get a list containing their details

                        current_line = line.split(", ")

                        #get the due date of the task

                        due_date = datetime.datetime.strptime(current_line[4], "%d %b %Y")

                        #get the current date

                        current_date = datetime.datetime.now()

                        #check if each task is assigned to each given user, if so increase their task count

                        if current_line[0] == name:
                            
                            user_task_count += 1

                            #if the task is complete, increase their completed task count

                            if current_line[5] == "Yes":

                                user_task_completed_count += 1

                            #if the task is incomplete and overdue, increase their uncompleted and overdue task count

                            elif current_line[5] == "No" and due_date < current_date:

                                user_task_overdue_count += 1

                                user_task_uncompleted_count += 1

                            #if the task is incomplete, increase their uncompleted task count

                            elif current_line[5] == "No":

                                user_task_uncompleted_count += 1

                #if the user has at least one task      

                if user_task_count > 0:

                    #add to the end of the text to write to task_overview, the following string containig details of the users tasks

                    file_to_write += f"User: {name}, Tasks Assigned: {user_task_count}, Percentage of total tasks: {round(user_task_count / len(user_task_lines) * 100, 2)}%, Percentage complete: {round((user_task_completed_count / user_task_count) * 100, 2)}%, Percentage Uncomplete: {round((user_task_uncompleted_count / user_task_count) * 100, 2)}%, Percentage overdue: {round((user_task_overdue_count / user_task_count) * 100, 2)}%\n"
               
                #if the user has no tasks

                else:

                    #add to the end of the text to write to task_overview, the following string where all of the values except user are 0

                    file_to_write += f"User: {name}, Tasks Assigned: 0, Percentage of total tasks: 0%, Percentage complete: 0%, Percentage Uncomplete: 0%, Percentage overdue: 0%\n"

            #open the user_overview.txt file in write mode and write our text to this file
                             
            with open("user_overview.txt", "w") as user_overview:

              user_overview.write(file_to_write)

              #close the file after writing

              user_overview.close()

            #close the text file containing the users

            all_users.close()







def reg_user():



    #prompt user for a username, a password and confirmation of the password

        new_user_name = input("Please enter a username: ")

        with open("user.txt", "r") as user_info:

            usernames = []


            for user in user_info.read().splitlines():


                usernames.append(user.split(", ")[0])


            while new_user_name in usernames:

                new_user_name = input("Username already taken, please enter a new one: ")


            user_info.close()    


        

        new_password = input("Please enter a password: ")

        new_password_confirm = input("Please confirm your password: ")

        #while the password and the confirmation do not match

        while new_password != new_password_confirm:

            #print to screen that they do not match and continue to prompt user for both

            print("passwords do not match")

            new_password = input("Please enter a password: ")

            new_password_confirm = input("Please confirm your password: ")

        #open the user text file in append mode, to append the new user name and password to a new
        #line in the file

        with open('user.txt', 'a') as user_information:    

         user_information.write(f"\n{new_user_name}, {new_password}")

         #close the text file

         user_information.close()



def add_task():



    #access todays date using the datetime module that was imported and its now method
        #and convert to "dd mmm yyyy" format

        todays_date = datetime.datetime.now().strftime("%d %b %Y")

        #prompt user to input their username, the task title, task description and due date

        task_username = input("Please enter a username: ")

        task_title = input("Please give the task a title: ")

        task_description = input("Please enter a description of the task: ")

        task_due = input("Please enter a due date for the task: ")

        #open the tasks file in append setting

        with open('tasks.txt', 'a') as tasks:

            #write onto a new line in the text file all of the information prompted for the user
            #in addition to the current date and "No", showing the task has not been completed

            tasks.write(f"\n{task_username}, {task_title}, {task_description}, {todays_date}, {task_due}, No")

            #close the text file

            tasks.close()



def view_all():

        #open the tasks in read setting

        with open('tasks.txt', 'r') as tasks:

            #read the tasks file and split it into list of its lines

            task_lines = tasks.read().splitlines()

            #loop through each line

            for lines in task_lines:

                #split each line into another list by the comma and space

                split_lines = lines.split(", ")
     
                #print the details of the tasks, accessing each detail by their index in the
                #list containing them

                print(f"""Task:           {split_lines[1]} 
Assigned to:    {split_lines[0]}
Date assigned:  {split_lines[3]}
Due date:       {split_lines[4]}
Task Complete?  {split_lines[5]}
Task description:
 {split_lines[2]}""")

                #print and empty line to space each of the tasks that are printed to the screen
              
                print()
 
            #close the text file

            tasks.close()



def view_mine():

            #open the tasks in read setting

        with open('tasks.txt', 'r') as tasks:

            #read the tasks file and split it into list of its lines

            task_lines = tasks.read().splitlines()

            user_tasks = []

            task_number = 0

            #loop through each line

            for lines in range(len(task_lines)):

                #split each line into another list by the comma and space

                split_lines = task_lines[lines].split(", ")

                #check the user of the task accessed by indexing the split_lines list
                #is the same as the one logged in, only then, print the tasks to the 
                #screen in the same way as with the va user slection

                if split_lines[0] == user:

                    #lines will be appended to keep track of the lines index in the original task text file

                    split_lines.append(lines)

                    user_tasks.append(split_lines)

                    task_number += 1




                    print(f"""Task:           {split_lines[1]} 
Task Number:    {task_number}         
Assigned to:    {split_lines[0]}
Date assigned:  {split_lines[3]}
Due date:       {split_lines[4]}
Task Complete?  {split_lines[5]}
Task description:
 {split_lines[2]}""")


                    #print and empty line to space each of the tasks that are printed to the screen

                    print()



            

            #enter an infinite loop

            while True:

                #prompt user to enter a number to select the task or go back to main menu

                user_choice = int(input("""Select a task by entering its task number, or enter -1 to
return to the main menu: """))

                #check the number is greater than 0 and less than the length of user_tasks (so a valid task number)

                if  user_choice > 0 and len(user_tasks) >= user_choice:

                    #get the task they selected by its index in user_tasks and print it out

                    selection = user_tasks[user_choice - 1]

                    print(f"""You have selected the following task:
Task:           {selection[1]} 
Task Number:    {user_choice}         
Assigned to:    {selection[0]}
Date assigned:  {selection[3]}
Due date:       {selection[4]}
Task Complete?  {selection[5]}
Task description:
 {selection[2]}""")
                    #enter into an infinite loop

                    while True:

                         

                        #prompt user for what action they would like to take                 

                        user_action = input("Enter e to edit (if incomplete), m to mark as complete, or -1 to select a new task: ")

                        #if they select mark as complete

                        if user_action == "m":
                            
                            #open the tasks file in read mode

                            with open("tasks.txt", "r+") as task_to_mark:

                                #get the text of the tasks in a list

                                text = task_to_mark.readlines()

                                #get specific task by its index which is store in the selected, and then convert to a list

                                line_to_mark = text[selection[6]].split(", ")

                                #convert mark the completed part of the task as Yes

                                line_to_mark[5] = "Yes\n"

                                #rejoin the task as one string again and update the list of tasks               

                                text[selection[6]] = ", ".join(line_to_mark)

                                #open the tasks file in write mode         

                                with open("tasks.txt", "w") as tasks_marked:

                                    #write the text variable to the tasks file with the list all rejoined as one string

                                    tasks_marked.write("".join(text))

                                    #close the tasks file that is in write mode

                                    tasks_marked.close()

                                #close the tasks file that is in read mode

                                task_to_mark.close()

                        #if the task is already marked as complete inform the user that it is

                        elif user_action == "e" and selection[5] == "Yes":

                            print("Task already complete")

                        #if the user selects edit and the task is not marked as complete

                        elif user_action == "e" and selection[5] == "No":

                            #enter an infinite while loop

                            while True:

                               #prompt the user for what kind of edit they would like to make

                               username_or_date = input("""Enter u to change the user who the task is assigned to, d to
change the due date, or -1 to go back: """)   

                                #if they select username
  
                               if username_or_date == "u":

                                    #prompt the user for the new username

                                    new_username = input("Please enter a new username for the task: ")

                                    #open the tasks file in read mode

                                    with open("tasks.txt", "r+") as task_to_change:

                                         #read the file

                                         text = task_to_change.readlines()

                                         #get the task line that they want to change and return as a list

                                         line_to_change = text[selection[6]].split(", ")

                                         #change the username by accesing the index of the list                      

                                         line_to_change[0] = new_username

                                         #rejoin the list as a string and put in the text list
                
                                         text[selection[6]] = ", ".join(line_to_change)

                                         #open the tasks file in write mode

                                         with open("tasks.txt", "w") as tasks_changed:

                                            #write the changed text to the file

                                            tasks_changed.write("".join(text))

                                            #close the tasks file that is in write mode

                                            tasks_changed.close()

                                         #close the tasks file that is in read mode

                                         task_to_change.close()

                                #if the user selects date

                               elif username_or_date == "d":
                                   
                                    #prompt the user for the new date

                                    new_date = input("Please enter a new due date for the task: ")

                                    #open the tasks file in read mode

                                    with open("tasks.txt", "r+") as task_to_change:

                                #selected_line = task_complete.readlines()[selection[6]]

                                         #read the file

                                         text = task_to_change.readlines()

                                         #get the task line that they want to change and return as a list

                                         line_to_change = text[selection[6]].split(", ")

                                         #change the date by accesing the index of the list 

                                         line_to_change[4] = new_date

                                         #rejoin the list as a string and put in the text list

                                         text[selection[6]] = ", ".join(line_to_change)

                                         #open the tasks file in write mode

                                         with open("tasks.txt", "w") as tasks_changed:

                                            #write the changed text to the file

                                            tasks_changed.write("".join(text))

                                            #close the tasks file that is in write mode

                                            tasks_changed.close()

                                         #close the tasks file that is in read mode

                                         task_to_change.close()

                                #if -1 is selected break the while loop and go back

                               elif username_or_date == "-1":

                                    break

                                #otherwise print the selection is invalid

                               else:

                                    print("Invalid selection")

                        #if -1 is selected break the while loop and go back

            
                        elif user_action == "-1":

                            break

                        #otherwise print the selection is invalid

                        else: 

                            print("Invalid selection")

                #if -1 is selected break the while loop and go back

                elif user_choice == -1:

                    break

                #otherwise print the selection is invalid

                else:

                    print("Invalid selection")


                

            #close the text file

            tasks.close()


def view_stats():

            #open the tasks text file in read mode

        with open('tasks.txt', 'r') as tasks:

            #read the tasks text file, split each line into an element of a list and then
            #count the elements of the list to know the number of tasks

            task_amount = len(tasks.read().splitlines()) 

            #close the text file

            tasks.close()

        #open the users text file in read mode    

        with open('user.txt', 'r') as users:

            #read the users text file, split each line into an element of a list and then
            #count the elements of the list to know the number of users

            user_amount = len(users.read().splitlines())  

            #close the text file

            tasks.close()

            #print the number of users and the nubmber of tasks to the screen

        print(f"""Number of users: {user_amount}
Number of tasks: {task_amount}""") 


#prompt user to enter their username

user_name = input("Please enter your username: ")

#prompt the user to enter their password

password = input("Please enter your password: ")

#open the user text file in read mode

with open('user.txt', 'r') as user_information:

    #read the lines for user creating a list

    users = user_information.read().splitlines()

    #while loop that continues to prompt user for their username and password while
    #they cannot be found together, by checking if a string consisting of the username
    #a comma with space and the password is present or not in the users list

    while (user_name + ", " + password) not in users:

        #if not found, print not found and prompt the user for username and password again

        print("not found")


        user_name = input("Please enter your username: ")

        password = input("Please your password: ")



    #define the user as the user_name so the program knows who is logged in
    
    user = user_name  

    #close the text file

    user_information.close()  

    

#forever while loop that is presented until the exit function is called by the user

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.

    #if the user is the admin

    if user == 'admin':

         #present a menu with all options available as input

         menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
vs - view stats
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

    else:

        #if the user is not the admin present a limited menu with view stats
        #and registering a user removed as these are reserved for the admin

        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()



    #if registering a user is selected and the admin is logged in

    if menu == 'r' and user == 'admin':


        reg_user()


    #if the user selects adding a task

    elif menu == 'a':

       add_task()


    #if view all tasks is selected

    elif menu == 'va':

        view_all()


    #if the view my tasks is selected

    elif menu == 'vm':

        view_mine()



    #if view stats is selected and the admin is the logged in user


    elif menu == 'vs' and user == 'admin':

        view_stats()

    #if the user selects generate reports and the logged in user is the admin


    elif menu == 'gr' and user == 'admin':

        #call the generate_task_overview() and generate_user_overview files

        generate_task_overview()

        generate_user_overview()

        print()

        print("Reports generated")

        print()

            

    #if the user selects generates stats and the logged in user is the admin

    elif menu == 'ds' and user == "admin":

        #check if tasks_overview exists, and if it does not, call the function to generate it

        if not exists("task_overview.txt"):

            generate_task_overview()

        #check if user_overview exists, and if it does not, call the function to generate it

        if not exists("user_overview.txt"):

            generate_user_overview()

        #open task_overview in read mode


        with open("task_overview.txt", "r") as task_overview:

            #print the text file to the screen after reading it

            print(task_overview.read())

            #close the text file

            task_overview.close()

            print()

        #open user_overview in read mode

        with open("user_overview.txt", "r") as user_overview:

            #get a list of each user task details

            users_and_tasks = user_overview.read().splitlines()

            #for user task details string

            for task in users_and_tasks:

                #split into a list

                users_tasks = task.split(", ")

                #print out each detail

                for detail in users_tasks:

                    print(detail)

                #print out a line for readability

                print()
            
            #close the file

            user_overview.close()


    #exit the program when the user selects to do so

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #if an invalid option is given prompt the user again, continuing the infinite while loop

    else:
        print("You have made a wrong choice, Please Try again")