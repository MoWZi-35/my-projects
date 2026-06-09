from tkinter import *
import sqlite3

db = sqlite3.connect('bank.db')
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Bank(
          login text UNIQUE,
          password text,
          money integer
)""")

window = Tk()
window.title('Bank')
window.geometry('1280x720')
window.resizable(width=False, height=False)
window.config(bg='#103e72')

page1 = Frame(window, bg='#103e72')
page2 = Frame(window, bg='#103e72')
page3 = Frame(window, bg='#103e72')

def show_page(page):
    page1.pack_forget()
    page2.pack_forget()
    page3.pack_forget()
    page.pack()

login = None
password = None
deposit = None
withdraw = None
current_user = None

def create_account():
    login = LC.get()
    password = LC1.get()
    c.execute("SELECT * FROM Bank WHERE login = ?", (login,))
    if c.fetchall():
        lab1.configure(text='An account with the same login already exists.', fg='red')
    else:
        c.execute("INSERT OR IGNORE INTO Bank VALUES (?, ?, ?)", (login, password, 0))
        db.commit()
        lab1.configure(text='account has been created', fg='green')

def log_in():
    global current_user 
    login = L.get()
    password = L1.get()
    c.execute("SELECT * FROM Bank WHERE login = ? AND password = ?", (login, password))
    if c.fetchall():
        show_page(page3)
        current_user = login
        c.execute("SELECT money FROM Bank WHERE login = ?", (current_user,))
        new_balance = c.fetchone()[0]
        balance.configure(text=f'{new_balance}$')
    else:
        lab.configure(text="incorect login or password", fg='red')

def deposit_money():
    global current_user
    deposit = int(deposit_e.get())
    c.execute("UPDATE Bank SET money = money + ? WHERE login = ?", (deposit, current_user))
    db.commit()
    c.execute("SELECT money FROM Bank WHERE login = ?", (current_user,))
    new_balance = c.fetchone()[0]
    balance.configure(text=f'{new_balance}$')

def withdraw_money():
    global current_user
    withdraw = int(withdraw_e.get())
    c.execute("UPDATE Bank SET money = money - ? WHERE login = ?", (withdraw, current_user))
    db.commit()
    c.execute("SELECT money FROM Bank WHERE login = ?", (current_user,))
    new_balance = c.fetchone()[0]
    balance.configure(text=f'{new_balance}$')


# --- Page 1 (log in) ---
Label(page1,
    text='Bank',
    font=("Arial", 60, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

Label(page1,
    text='Log in',
    font=("Arial", 30, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

Label(page1,
    text='Login: ',
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack(pady=(150,0))

L = Entry(page1) 
L.pack()

Label(page1,
    text='password: ',
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

L1 = Entry(page1, show='*') 
L1.pack()

login_btn = Button(page1,
                   text='login',
                   command=log_in,
                   font=("Arial", 20, "bold"),
                   fg='#103e72',
                   bg='white',
                   activebackground="#0E2E54",
                   activeforeground='white',

                   )
login_btn.pack(pady=10)

lab= Label(page1,
    text=" ",
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    )
lab.pack()

Label(page1,
    text="you don't have an account?",
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

create_account_btn = Button(page1,
                   text='create account',
                   command=lambda: show_page(page2),
                   font=("Arial", 10, "bold"),
                   fg='#103e72',
                   bg='white',
                   activebackground="#0E2E54",
                   activeforeground='white',

                   )
create_account_btn.pack(pady=10)

#--- Page 2 (create account) ---
Label(page2,
    text='Bank',
    font=("Arial", 60, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

Label(page2,
    text='Create account',
    font=("Arial", 30, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

Label(page2,
    text='Login: ',
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack(pady=(150,0))

LC = Entry(page2) 
LC.pack()

Label(page2,
    text='password: ',
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

LC1 = Entry(page2, show='*') 
LC1.pack()

create_account_btn1 = Button(page2,
                   text='Create account',
                   command=create_account,
                   font=("Arial", 20, "bold"),
                   fg='#103e72',
                   bg='white',
                   activebackground="#0E2E54",
                   activeforeground='white',

                   )
create_account_btn1.pack(pady=10)

lab1= Label(page2,
    text=" ",
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    )
lab1.pack()

Label(page2,
    text="you already have an account?",
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

login_btn1 = Button(page2,
                   text='log in',
                   command=lambda: show_page(page1),
                   font=("Arial", 10, "bold"),
                   fg='#103e72',
                   bg='white',
                   activebackground="#0E2E54",
                   activeforeground='white',

                   )
login_btn1.pack(pady=10)

#--- Page 3 (account balance) ---
Label(page3,
    text='Bank',
    font=("Arial", 60, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

Label(page3,
    text='Balance',
    font=("Arial", 30, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

Label(page3,
    text='Your Balance:',
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack(pady=(100,0))

balance=Label(page3,
    text='0$',
    font=("Arial", 30, "bold"),
    bg='#103e72',
    fg='white'
    )
balance.pack()

Label(page3,
    text='deposit money: ',
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack(pady=(50,0))

deposit_e = Entry(page3) 
deposit_e.pack()

deposit = Button(page3,
                   text='OK',
                   command=deposit_money,
                   font=("Arial", 10, "bold"),
                   fg='#103e72',
                   bg='white',
                   activebackground="#0E2E54",
                   activeforeground='white',

                   )
deposit.pack(pady=10)

Label(page3,
    text='withdraw money: ',
    font=("Arial", 10, "bold"),
    bg='#103e72',
    fg='white'
    ).pack()

withdraw_e = Entry(page3) 
withdraw_e.pack()

withdraw = Button(page3,
                   text='OK',
                   command=withdraw_money,
                   font=("Arial", 10, "bold"),
                   fg='#103e72',
                   bg='white',
                   activebackground="#0E2E54",
                   activeforeground='white',

                   )
withdraw.pack(pady=10)


logout_btn = Button(page3,
                   text='log out',
                   command=lambda: show_page(page1),
                   font=("Arial", 10, "bold"),
                   fg='#103e72',
                   bg='white',
                   activebackground="#0E2E54",
                   activeforeground='white',

                   )
logout_btn.pack(pady=10)

show_page(page1)
window.mainloop()
db.commit()
db.close()
