import sqlite3
import datetime

db = sqlite3.connect('To_Do_List_Db.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS ToDoList (
          title text,
          description text,
          date text,
          state text
)""")
user_title = None
user_description = None
user_date = None
user_state = None
user_state_choice = None



def add_task():
    user_title = input("enter title of your task: ")
    user_description = input("enter description of your task: ")
    user_date = datetime.date.today().strftime("%d.%m.%Y")
    c.execute("INSERT INTO ToDoList VALUES (?, ?, ?, ?)", (user_title, user_description, user_date, 'not done'))
    db.commit()

def see_all_tasks():
    c.execute("SELECT rowid, * FROM ToDoList")
    items = c.fetchall()
    for elementy in items:
        print(f"\n{elementy[0]}. {elementy[1]}\n{elementy[2]}\ndate: {elementy[3]}\nstate: {elementy[4]}")
    

def change_task_state():
    try:
        user_state_choice = int(input("enter number of your task: "))
        user_state = input("enter new state: ")
        c.execute("UPDATE ToDoList SET state = ? WHERE rowid = ?", (user_state, user_state_choice))
        db.commit()
    except ValueError:
        print("please enter correct number!")

def delete_task():
    try:
        task_num = int(input("enter number of your task: "))
        c.execute("DELETE FROM ToDoList WHERE rowid = " + str(task_num))
        db.commit()
    except ValueError:
        print("please enter correct number!")

while True:
    print("\n--- To Do List ---")
    print("add task - 1")
    print("see all tasks - 2")
    print("change task state - 3")
    print("delete task - 4")
    print("exit - 5")

    try:
        choice = int(input("please enter number: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            see_all_tasks()
        elif choice == 3:
            change_task_state()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            db.commit()
            break
        else:
            print("please enter correct number!")
    except ValueError:
        print("please enter correct number!")


db.commit()
db.close()
