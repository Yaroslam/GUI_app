
import tkinter as tk
from tkinter import ttk
from const import *


# главгое окно
class Main:

    def __init__(self, root):
        self.root = root
        self.root.title('something')
        self.root.geometry('650x400')

        self.stats_field = tk.Canvas(self.root, bg="red", width=650)
        self.stats_field.pack()

        self.top_block = tk.Frame(self.root, bg="black", bd=2)
        self.top_block.pack(side=tk.TOP, fill=tk.X)

        self.btn_recount = tk.Button(self.root, text="add", command=self.create_statement_and_sector, compound=tk.TOP,
                                     bd=0)  # button is open recount window
        self.btn_recount.pack(side=tk.LEFT)

        self.btn_goal = tk.Button(self.root, text="goals", command=self.open_goal,
                                  compound=tk.TOP)  # button is open goals window
        self.btn_goal.pack(side=tk.LEFT)

        self.btn_account = tk.Button(self.root, text="account", command=self.open_account, compound=tk.TOP, bd=0)
        self.btn_account.pack(side=tk.LEFT) # button is open account window
 
        self.root.mainloop()

    def create_statement_and_sector(self): #create small circle with text below
        self.get_state = Recount(self.root)
        self.statement = self.get_state.enter_text('')
        self.moneys = self.get_state.enter_money()
        if self.statement:
            fill = 'black'
            self.stats_field.create_oval(mass_for_circle[0], mass_for_circle[1], mass_for_circle[2], mass_for_circle[3],
                                         fill=fill)
            self.stats_field.create_text(mass_of_text_for_circle[0], mass_of_text_for_circle[1], text=self.statement)
            

    def open_goal(self):
        Goal(self.root)

    def open_account(self):
        Account(self.root)


# окно ввода денег
class Recount:

    def __init__(self, root):
        self.child_root = tk.Toplevel(root)
        self.child_root.geometry("400x220")
        self.child_root.title("окно номер 2")
        self.child_root.resizable(False, False)

        self.money = ttk.Entry(self.child_root)  # add money
        self.money.place(x=200, y=50)

        self.state_of_recount = ttk.Entry(self.child_root)  # add state of earninig or spending
        self.state_of_recount.place(x=200, y=110)

        self.select_box = ttk.Combobox(self.child_root,
                                       values=['spending', 'earning'])  # selestion of spending or earning
        self.select_box.current(1)
        self.select_box.place(x=200, y=80)

        self.describ_money = ttk.Label(self.child_root, text="money")  # describtion for  self.money
        self.describ_money.place(x=150, y=50)

        self.describ_state = ttk.Label(self.child_root, text="state")  # description for  self.state_of_recount
        self.describ_state.place(x=150, y=110)

        self.describ_box = ttk.Label(self.child_root, text="earning/spending")  # description for box
        self.describ_box.place(x=100, y=80)

        self.btn_exit = tk.Button(self.child_root, text="exit", command=self.child_root.destroy) #exit button
        self.btn_exit.place(x=300, y=170)

        self.btn_add = tk.Button(self.child_root, text="apply", command=self.set_text) #button for sending information about state and money
        self.btn_add.place(x=220, y=170)

        self.child_root.grab_set()
        self.child_root.focus_set()

    def enter_money(self): 
        self.money.insert('0', tk.END)
        self.money_count = 0
        self.child_root.wait_window()
        return self.money_count

    def set_money(self):
        self.money_count = self.money.get()

    def enter_text(self, texted=''):
        self.state_of_recount.insert('0', texted)
        self.state = None
        self.child_root.wait_window()
        return self.state

    def set_text(self):
        self.state = self.state_of_recount.get()
        self.child_root.destroy()


class Goal:
    def __init__(self, root):
        self.child_root = tk.Toplevel(root)
        self.child_root.geometry("400x220")
        self.child_root.title("окно номер 2")
        self.child_root.resizable(False, False)

        self.add_goal_btn = tk.Button(self.child_root, text="add goal", )
        self.delete_goal_btn = tk.Button(self.child_root, text="delete goal")

        self.add_goal_btn.pack()
        self.delete_goal_btn.pack()


class Account:
    def __init__(self, root):
        self.child_root = tk.Toplevel(root)
        self.child_root.geometry("400x220")
        self.child_root.title("окно номер 2")
        self.child_root.resizable(False, False)

        self.add_account_btn = tk.Button(self.child_root, text="add account", )
        self.delete_account_btn = tk.Button(self.child_root, text="delete account", )

        self.add_account_btn.pack()
        self.delete_account_btn.pack()


root = tk.Tk()

Main(root)

