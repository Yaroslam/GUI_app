
import tkinter as tk
from tkinter import ttk
import sqlite3
from const import COLORS

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()
        self.view_state()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        btn_open_destroy = tk.Button(toolbar, text = 'удалить позицию', command=self.open_destroy, bd=0, compound=tk.TOP)
        btn_open_destroy.pack(side=tk.LEFT)

        self.stats_field = tk.Canvas(bg = COLORS[43],width=650)
        self.stats_field.pack()

    def records(self, description, costs):
        self.db.insert_data(description, costs)
        self.view_records()
        self.view_state()


    def delete_record(self, search):
        self.db.delete_data(search)
        self.stats_field.delete("all")
        self.view_records()
        self.view_state()

    def view_state(self):
        state_mass = self.db.c.execute('''SELECT description FROM finance''').fetchall()
        text_x0 = 100
        text_y0 = 100
        for i, m in enumerate(state_mass):
            self.stats_field.create_text(text_x0, text_y0, text = m, fill = COLORS[i])
            text_x0 += 100

    def view_records(self):   #отображение расходов
        summ = self.db.c.execute('''SELECT SUM(costs) FROM finance''').fetchone()
        money_mass = self.db.c.execute('''SELECT costs FROM finance''').fetchall()
        end = 0
        for i, m in enumerate(money_mass):
            ext = 360 * m[0] / summ[0]
            self.stats_field.create_arc(20, 20, 200, 200,start=end, extent=ext, fill=COLORS[i])
            end += ext


    def open_dialog(self):
        Recount()

    def open_destroy(self):
        Destroy()


class Destroy(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_destroy()
        self.view = app

    def init_destroy(self):
        self.title('Добавить доходы\расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.enter_destroy_position = ttk.Entry(self)
        self.enter_destroy_position.place(x=200, y=50)

        destroy_position_description = tk.Label(self, text='Что надо удалить')
        destroy_position_description.place(x=50, y=50)

        btn_delete = tk.Button(self, text='Удалить')
        btn_delete.place(x=220, y=170)
        btn_delete.bind('<Button-1>', lambda event: self.view.delete_record(self.enter_destroy_position.get()))

        btn_exit = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_exit.place(x=300, y=170)

        self.grab_set()
        self.focus_set()


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
        btn_ok.bind('<Button-1>', lambda event: self.view.records(
                                                                  self.entry_description.get(),
                                                                  self.entry_money.get()
                                                                    ))

        self.grab_set()
        self.focus_set()






class DB:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs integer)''') #создание бд
        self.conn.commit()

    def insert_data(self, description, costs):
        self.c.execute('''INSERT INTO finance(description, costs) VALUES (?, ?)''', #добалвние данных в бд
                       (description, costs))
        self.conn.commit()

    def delete_data(self, search):
        self.c.execute('DELETE FROM finance WHERE description = ?',(search,))
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
