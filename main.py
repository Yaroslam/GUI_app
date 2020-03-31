import sqlalchemy as sqa
from sqlalchemy.orm import Session
import tkinter as tk
from tkinter import ttk
import sqlite3
from const import COLORS

class Main(tk.Frame): #конструктор класса
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()
        self.view_state()

    def init_main(self): #главная функция
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add_img.PNG')
        self.acc_img = tk.PhotoImage(file='account_img.PNG')
        self.delete_img = tk.PhotoImage(file='delete_img.PNG')

        btn_open_dialog = tk.Button(toolbar, image=self.add_img, command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.place(x=100)

        btn_open_destroy = tk.Button(toolbar, image=self.delete_img, command=self.open_destroy, bd=0, compound=tk.TOP, bg='#d7d8e0')
        btn_open_destroy.pack()

        btn_open_account = tk.Button(toolbar, command=self.open_account, bd=0, compound=tk.TOP, image=self.acc_img, bg='#d7d8e0')
        btn_open_account.place(x=500)

        self.stats_field = tk.Canvas(bg='#d7d8e0',width=650)
        self.stats_field.pack()

    def records(self, description, costs):  # ввод и отображение данных о тратах на главном окне
        if description == '' or description == " ":
            pass
        else:
            self.db.insert_data(description, costs)
            self.view_records()
            self.view_state()

    def delete_record(self, search): #удаление данных о тратах с главного окна
        self.db.delete_data(search)
        self.stats_field.delete("all")
        self.view_records()
        self.view_state()

    def delete_all_records(self): #удаление всех данных о расходах
        self.db.delete_all()
        self.stats_field.delete("all")

    def view_state(self): # отображение статей расходов
        state_mass = self.db.c.execute('''SELECT description FROM finance''').fetchall()
        text_x0 = 300
        text_y0 = 20
        for i, m in enumerate(state_mass):
            self.stats_field.create_text(text_x0, text_y0, text = m, fill = COLORS[i])
            if text_y0 < 300:
                text_y0 += 50
            else:
                text_x0+=100
                text_y0=20

    def view_records(self):   #отрисовка диаграмммы
        summ = self.db.c.execute('''SELECT SUM(costs) FROM finance''').fetchone()
        money_mass = self.db.c.execute('''SELECT costs FROM finance''').fetchall()
        end = 0
        if len(money_mass) == 1:
            self.stats_field.create_oval(20, 20, 200, 200, fill=COLORS[0])
        else:
            for i, m in enumerate(money_mass):
                ext = 360 * m[0] / summ[0]
                self.stats_field.create_arc(20, 20, 200, 200,start=end, extent=ext, fill=COLORS[i])
                end += ext


    def open_dialog(self): #открыть окно добавление расходов
        Recount()

    def open_destroy(self): #открыть окно удаление расходов
        Destroy()

    def open_account(self):
        Account()

class Destroy(tk.Toplevel):
    def __init__(self): #конструктор
        super().__init__(root)
        self.init_destroy()
        self.view = app

    def init_destroy(self): #главная функция
        self.title('Добавить доходы\расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.enter_destroy_position = ttk.Entry(self)
        self.enter_destroy_position.place(x=200, y=50)

        destroy_position_description = tk.Label(self, text='Какую позицию удалить')
        destroy_position_description.place(x=50, y=50)

        btn_delete = ttk.Button(self, text='Удалить')
        btn_delete.place(x=220, y=170)
        btn_delete.bind('<Button-1>', lambda event: self.view.delete_record(self.enter_destroy_position.get()))

        btn_delete_all = ttk.Button(self, text='Удалить все')
        btn_delete_all.place(x=140, y=170)
        btn_delete_all.bind('<Button-1>', lambda event: self.view.delete_all_records())

        btn_exit = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_exit.place(x=300, y=170)

        self.grab_set()
        self.focus_set()


class Recount(tk.Toplevel):
    def __init__(self): #конструктор
        super().__init__(root)
        self.db = db
        self.init_child()
        self.view = app

    def init_child(self): #главная функция
        self.title('Добавить доходы\расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Наименование:')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Статья дохода\расхода:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Сумма:')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.choose_acc_box = ttk.Combobox(self, values=self.db.a.execute('''SELECT name FROM account''').fetchall())
        self.choose_acc_box.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.recount(self.entry_description.get(),
                                                             self.entry_money.get(),
                                                             self.choose_acc_box.get()
                                                             ))

        self.grab_set()
        self.focus_set()

    def recount(self, name_state, money, name_acc):
        self.view.records(name_state, money)
        self.db.minus_money_on_acc(money,name_acc)




class Account(tk.Toplevel):
    def __init__(self): #конструктор
        super().__init__(root)
        self.init_account()
        self.db = db
        self.view_acc_data()

    def init_account(self): #главная функция
        self.title('Добавить доходы\расходы')
        self.geometry('650x450+400+300')
        self.resizable(False, False)

        self.tree = ttk.Treeview(self, columns=('ID', 'name', 'balance'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('name', width=365, anchor=tk.CENTER)
        self.tree.column('balance', width=150, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('name', text='счет')
        self.tree.heading('balance', text='баланс')

        self.tree.pack()

        self.name_acc = tk.Entry(self)
        self.name_acc.place(x=263,y=330)

        self.acc_balance = tk.Entry(self)
        self.acc_balance.place(x=263,y=350)

        self.acc_balance_descrip = tk.Label(self, text='баланс счета')
        self.acc_balance_descrip.place(x=150,y=350)

        self.name_acc_descrip = tk.Label(self, text='название счета')
        self.name_acc_descrip.place(x=150,y=330)

        btn_add_acc = ttk.Button(self, text='добавить')
        btn_add_acc.bind('<Button-1>', lambda event: self.acc(self.name_acc.get(),
                                                              self.acc_balance.get()
                                                                  ))
        btn_add_acc.place(x=445,y=420)

        btn_delete_acc = ttk.Button(self, text='удалить')
        btn_delete_acc.bind('<Button-1>', lambda event: self.delete_account())
        btn_delete_acc.place(x=525, y=420)

    def acc(self, name, money):  # добавить счет в бд
        if name == '' or name == " ":
            pass
        else:
            self.db.insert_account(name, money)
            self.view_acc_data()

    def view_acc_data(self):  # отрисовка счетов
        self.db.a.execute('''SELECT * FROM account''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.a.fetchall()]

    def delete_account(self):  # удалить счет из бд
        for selection_item in self.tree.selection():
            self.db.a.execute('''DELETE FROM account WHERE id=?''', (self.tree.set(selection_item, '#1')))
        self.db.conn.commit()
        self.view_acc_data()

# class DB:
#     def __init__(self):  # создание бд
#         self.account = sqlite3.connect('account.db')
#         self.conn = sqlite3.connect('finance.db')
#         self.a = self.account.cursor()
#         self.c = self.conn.cursor()
#         self.c.execute(
#             '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs integer)''')
#         self.a.execute(
#             '''CREATE TABLE IF NOT EXISTS account(id integer primary key, name text, money integer)''')
#         self.conn.commit()
#         self.account.commit()
#
#     def insert_data(self, description, costs): #добалвние данных в бд
#         self.c.execute('''INSERT INTO finance(description, costs) VALUES (?, ?)''',
#                        (description, costs))
#         self.conn.commit()
#
#     def delete_data(self, search): #удаление данных по вводимому значению
#         self.c.execute('DELETE FROM finance WHERE description = ?',(search,))
#         self.conn.commit()
#
#     def delete_all(self): #удаление бд
#         self.c.execute('''DROP TABLE finance''')
#         self.a.execute('''DROP TABLE account''')
#
#     def insert_account(self, name, money): #добавление данных
#         self.a.execute('''INSERT INTO account(name, money) VALUES (?, ?)''',
#                        (name, money))
#         self.account.commit()
#
#     def minus_money_on_acc(self, summ, account_name): #редактирование счета
#         self.a.execute('''UPDATE account SET money = money - ? WHERE name = ?''', (summ, account_name))
#         self.account.commit()

class acc_db():
    def __init__(self):
        self.metadata = sqa.MetaData()
        self.engine = sqa.create_engine() #не работает
        self.acc_table = sqa.Table(
            'acc_db', self.metadata,
            sqa.Column('id', sqa.Integer(), primary_key=True),
            sqa.Column('name', sqa.String()),
            sqa.Column('money', sqa.Integer()),
            )
        self.metadata.create_all(self.engine)
        self.conn = self.engine.connect()
        self.insert = sqa.insert(self.acc_table)


    def insert(self, get_name, get_money):
        self.conn.execute(self.insert,
                          name=get_name,
                          money=get_money
                        )












if __name__ == "__main__":
    root = tk.Tk()
    db = acc_db()
    app = Main(root)
    app.pack()
    root.title("Household finance")
    root.geometry("650x340+300+200")
    root.resizable(False, False)
    root.mainloop()
