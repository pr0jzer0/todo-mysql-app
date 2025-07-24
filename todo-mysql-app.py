import mysql.connector

db = mysql.connector.connect(
    user= "root",
    password= "",
    database= "to_do_list",
)

dbcursor = db.cursor()


# Insert a new task into the 'newtasklist' table


while(True):

# Main menu for the To-Do List App

    print("Welcome to the To-Do List App")
    print("Please enter your your option from below:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    option = input("Enter your option: ")


# Check the user's option and perform the corresponding action
    # Add a task to the 'newtasklist' table
    if option == "1":
        print("You have selected to add a task.")
        A_task = input("Enter a task: ")
        sql = "INSERT INTO newtasklist (Task) VALUES (%s)"
        val = (A_task,)
        dbcursor.execute(sql, val)
        db.commit()
        print(dbcursor.rowcount, "record inserted.")


    # Print the task that was added
    elif option == "2":
        print("You have selected to view tasks.")
        dbcursor.execute("SELECT * FROM newtasklist")
        tasks = dbcursor.fetchall()
        if tasks:
            for task in tasks:
                print(f"Task ID: {task[0]}, Task: {task[1]}")
        else:
            print("No tasks found.")
    
    
    # Delete a task from the 'newtasklist' table
    elif option == "3":
        print("You have selected to delete a task.")
        task_id = input("Enter the task ID to delete: ")
        dbcursor.execute("SELECT COUNT(*) FROM newtasklist")
        count = dbcursor.fetchone()[0]
        if count == 0:
            print("No tasks available to delete.")
            continue
        dbcursor.execute("DELETE FROM newtasklist WHERE id = %s", (task_id,))
        sql = "UPDATE newtasklist SET id = %s-1 WHERE id = %s"

        dbcursor.execute(sql, (id, task_id))
        db.commit()
        print(dbcursor.rowcount, "record(s) deleted.")

    
    # Exit the application
    elif option == "4":
        print("Exiting the To-Do List App. Goodbye!")
        break
    
    # Handle invalid options
    else:
        print("You have selected an invalid option. Please try again.")
        continue
