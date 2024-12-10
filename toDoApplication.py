#Function for the adding of tasks
def add_Task(task_List):
    
    try:
        add = input("Enter the Task to add to the list: ")

        if not add:
            return "Invalid input. Task cannot be empty."
        
        if add in task_List:
            return f"{add} is already in the list."
    
        #Adds user input to the To Do List
        task_List.append(add)
        return f"'{add}' has been added to your To Do List."
    
    except Exception as e:
        return f"An error occurred while adding the task: {e}"



#Function for the removing of tasks
def remove_Task(task_List):

    try:
        remove = input("Enter the Task to delete from the list: ")

        if not remove:
            return "Invalid input. Task to remove cannot be emtpy."

        #If the input is in the list remove it
        if remove in task_List:
            task_List.remove(remove)
            return f"'{remove}' has been removed from your To Do List."
        else:
            return f"{remove} was not in the To Do List."
        
    except Exception as e:
        return f"An error occurred while removing the task: {e}"


#Function for the viewing of tasks
def view_Task(task_List):

    try:
    
        if not task_List:
            return "Your To Do List is empty."
           
    
        #Adds to variable "msg" with a string of the task from the user in a  formatted way so "msg" can be returned and viewed as the To Do List
        msg = "\nTo Do List:\n" + ("---" * 12) + "\n"
        for task in task_List:
            msg += f"Task: {task}\n\n" 
        return msg
    
    except Exception as e:
        return f"An error occurred while viewing the tasks: {e}"
    

#Main interface for To Do List Application
def interface():
    
    task_List = []

    while True:
        try:

            #Uses user input to turn the string into an integer from 1-4 to access features through a menu

            print("To Do List Management Menu:")
            print("1. Add a Task")
            print("2. Remove a Task")
            print("3. View Tasks")
            print("4. Quit")

            choice = input("Please enter your choice (1-4): ").strip()

            if not choice.isdigit():
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

            choice = int(choice)

            if choice == 1:
                result = add_Task(task_List)
                print(result)
            elif choice == 2:
                result = remove_Task(task_List)
                print(result)
            elif choice == 3:
                result = view_Task(task_List)
                print(result)
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except Exception as e:
            return f"An error occurred while viewing the tasks: {e}"


if __name__ == "__main__":
    interface()