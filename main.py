
import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage()
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.stats_field = tk.Canvas(self, bg="red", width=650)
        self.stats_field.pack()


    def records(self, description, costs):
        self.db.insert_data(description, costs)
        self.view_records()

    def view_records(self):
        summ = self.db.c.execute('''SELECT SUM(costs) FROM finance''')
        money_mass = self.db.c.execute('''SELECT costs FROM finance''')
        money_mass.fetchall()
        end = 0
        for i in money_mass:
            self.stats_field.create_arc(start=end, extend=3.6*(i//summ * 100), fill = "black")
            end += 3.6*(i//summ * 100)



    def open_dialog(self):
        Recount()


class Recount(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
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

        self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                  self.entry_money.get()))

        self.grab_set()
        self.focus_set()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs integer)''')
        self.conn.commit()

    def insert_data(self, description, costs):
        self.c.execute('''INSERT INTO finance(description, costs) VALUES (?, ?)''',
                       (description, costs))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Household finance")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
