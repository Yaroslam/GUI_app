mass_for_circle = [10,10,30,30]
mass_of_text_for_circle = [30,40]
list_of_spend = {}

# self.main_tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), height = 15, show='headings')
        #
        # self.main_tree.column('ID', width=30, anchor=tk.CENTER)
        # self.main_tree.column('description', width=365, anchor=tk.CENTER)
        # self.main_tree.column('costs', width=150, anchor=tk.CENTER)
        # self.main_tree.column('total', width=100, anchor=tk.CENTER)
        #
        # self.main_tree.heading('ID', text= 'ID')
        # self.main_tree.heading('description', text='description')
        # self.main_tree.heading('costs', text='costs')
        # self.main_tree.heading('total', text='total')
        #
        # self.main_tree.pack()

# import tkinter as tk
# from tkinter import ttk
# from const import *
#
# # главгое окно
# class Main:
#
#     def __init__(self, root):
#         self.root = root
#         self.root.title('something')
#         self.root.geometry('650x400')
#
#         self.stats_field = tk.Canvas(self.root,bg="red", width=650)
#         self.stats_field.pack()
#
#         self.top_block = tk.Frame(self.root,bg = "black", bd = 2)
#         self.top_block.pack(side=tk.TOP, fill=tk.X)
#
#         self.btn_recount = tk.Button(self.root, self.top_block, text="add", command=self.open_recount, compound=tk.TOP,bd=0)  # button is open recount window
#         self.btn_recount.pack(side=tk.LEFT)
#
#         self.btn_goal = tk.Button(self.root, self.top_block, text="goals", command=self.open_goal, compound=tk.TOP)  # button is open goals window
#         self.btn_goal.pack(side=tk.LEFT)
#
#         self.btn_account = tk.Button(self.root, self.top_block, text="account", command=self.open_account, compound=tk.TOP, bd=0)
#         self.btn_account.pack(side=tk.LEFT)
#
#         self.root.mainloop()
#
#
#     def open_recount(self):
#         Recount()
#
#     def open_goal(self):
#         Goal()
#
#     def open_account(self):
#         Account()
#
# # окно ввода денег
# class Recount:
#
#     def __init__(self, root):
#         self.geometry("400x220")
#         self.title("окно номер 2")
#         self.resizable(False, False)
#
#         self.money = ttk.Entry(self)  # add money
#         self.money.place(x=200, y=50)
#
#         self.state_of_recount = ttk.Entry(self)  # add state of earninig or spending
#         self.state_of_recount.place(x=200, y=110)
#
#         self.select_box = ttk.Combobox(self, values=['spending', 'earning'])  # selestion of spending or earning
#         self.select_box.current(1)
#         self.select_box.place(x=200, y=80)
#
#         self.describ_money = ttk.Label(self, text="money")  # describtion for  self.money
#         self.describ_money.place(x=150, y=50)
#
#         self.describ_state = ttk.Label(self, text="state")  # description for  self.state_of_recoun
#         self.describ_state.place(x=150, y=110)
#
#         self.describ_box = ttk.Label(self, text="earning/spending")  # description for box
#         self.describ_box.place(x=100, y=80)
#
#         self.btn_exit = tk.Button(self, text="exit", command=self.destroy)
#         self.btn_exit.place(x=300, y=170)
#
#         self.btn_add = tk.Button(self, text="apply")
#         self.btn_add.place(x=220, y=170)
#
#         self.grab_set()
#         self.focus_set()
#
#
#
#
#
# class Goal(tk.Toplevel):
#     def __init__(self):
#         self.add_goal_btn = tk.Button(self, text="add goal", )
#         self.delete_goal_btn = tk.Button(self, text="delete goal")
#
#         self.add_goal_btn.pack()
#         self.delete_goal_btn.pack()
#
#         self.geometry("300x300")
#         self.title("окно номер 3")
#         self.grab_set()
#         self.focus_set()
#
# class Account(tk.Toplevel):
#     def __init__(self):
#         self.add_account_btn = tk.Button(self, text="add account", )
#         self.delete_account_btn = tk.Button(self, text="delete account", )
#
#         self.add_account_btn.pack()
#         self.delete_account_btn.pack()
#
#         self.geometry("300x300")
#         self.title("окно номер 4")
#         self.grab_set()
#         self.focus_set()
#
#
# root = tk.Tk()
#
# Main(root)


