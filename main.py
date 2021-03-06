import sqlalchemy as sqa
import tkinter as tk
from tkinter import ttk
from const import COLORS

class Main(tk.Frame): #конструктор класса
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = fin_db
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
            self.db.insert_rec(description, costs)
            self.view_records()
            self.view_state()

    def delete_record(self, search): #удаление данных о тратах с главного окна
        self.db.delete_rec(search)
        self.stats_field.delete("all")
        self.view_records()
        self.view_state()


    def view_state(self): # отображение статей расходов
        state_mass = self.db.select_descrip_recs()
        text_x0 = 300
        text_y0 = 20
        for i, m in enumerate(state_mass):
            self.stats_field.create_text(text_x0, text_y0, text = self.delete_symbols(m), fill = COLORS[i])
            if text_y0 < 300:
                text_y0 += 50
            else:
                text_x0+=100
                text_y0=20

    def view_records(self):   #отрисовка диаграмммы
        summ = self.db.sel_sum()
        money_mass = self.db.select_cost_recs()
        end = 0
        if len(money_mass) == 1:
            self.stats_field.create_oval(20, 20, 200, 200, fill=COLORS[0])
        else:
            for i, m in enumerate(money_mass):
                ext = 360 * m[0] / summ
                self.stats_field.create_arc(20, 20, 200, 200,start=end, extent=ext, fill=COLORS[i])
                end += ext

    def delete_symbols(self, row): #очистка отобрадаемых данных от лишних символом
        row = str(row).replace(str(row)[-2], '')
        row = str(row).replace(str(row)[1], '')
        row = str(row).replace("(", '')
        row = str(row).replace(")", '')
        row = str(row).replace(',', '')
        return str(row)


    def open_dialog(self): #открыть окно добавление расходов
        Recount()

    def open_destroy(self): #открыть окно удаление расходов
        Destroy()

    def open_account(self): #открыть окно счетов
        Account()

class Destroy(tk.Toplevel): #око удаления
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

        btn_exit = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_exit.place(x=300, y=170)

        self.grab_set()
        self.focus_set()


class Recount(tk.Toplevel): #окно добавления
    def __init__(self): #конструктор
        super().__init__(root)
        self.acc_db = acc_db
        self.init_child()
        self.view = app

    def init_child(self): #главная функция
        self.title('Добавить доходы\расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Наименование:')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='выберите счет')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Сумма:')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        sel = self.acc_db.select_name()
        self.choose_acc_box = ttk.Combobox(self, values=sel)
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

    def recount(self, name_state, money, name_acc): #отрисовка измененных данных наглавном окне и измененеие счета
        self.view.records(name_state, money)
        self.acc_db.update_rec(name_acc,money)




class Account(tk.Toplevel): #окно счетов
    def __init__(self): #конструктор
        super().__init__(root)
        self.init_account()
        self.acc_db = acc_db
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
            self.acc_db.insert_rec(name, money)
            self.view_acc_data()

    def view_acc_data(self):  # отрисовка счетов

        sel = self.acc_db.acc_table.select()
        [self.tree.delete(i) for i in self.tree.get_children()]
        for row in self.acc_db.conn.execute(sel):
            self.tree.insert('', 'end', values=self.__delete_symbols(row))

    def delete_account(self):  # удалить счет из бд
        for selection_item in self.tree.selection():
            delt = sqa.delete(self.acc_db.acc_table).where(self.acc_db.acc_table.c.id.like(self.tree.set(selection_item, '#1')))
            self.acc_db.conn.execute(delt)
        self.view_acc_data()

    def __delete_symbols(self, row): #очистка выводимых значений от ненужных символов
        start = str(row).find(',')
        end = str(row).rfind(',')
        row = str(row).replace(str(row)[start + 2], '')
        row = str(row).replace(str(row)[end - 1], '')
        row = str(row).replace("(", '')
        row = str(row).replace(")", '')
        row = str(row).replace(',', '')
        return str(row)


class ACC_DB(): #класс для работы с БД счетов
    def __init__(self): #конструктор
        self.engine = sqa.create_engine('sqlite:///acc.db')
        self.conn = self.engine.connect()
        self.data = sqa.MetaData(self.engine)
        self.acc_table = sqa.Table('acc', self.data,
                    sqa.Column('id', sqa.Integer(), primary_key=True),
                    sqa.Column('name', sqa.String()),
                    sqa.Column('money', sqa.Integer())
                    )
        self.data.create_all(self.engine)

    def insert_rec(self, name_value, money_value): #добавить значение
        ins = self.acc_table.insert().values(
            name = name_value,
            money = money_value
        )
        self.conn.execute(ins)

    def select_name(self): #выбор названий всех счетов
        rtrn_mass = []
        sel = sqa.select([self.acc_table.c.name])
        select_mass = self.conn.execute(sel).fetchall()
        for item in select_mass:
            rtrn_mass.append(item[0])
        return rtrn_mass

    def update_rec(self, name_value, money_value): #изменение баланса счет name_value на -new_walue едениц
        upd = sqa.update(self.acc_table).where(self.acc_table.c.name == name_value).values(money=self.acc_table.c.money
                                                                                                 -money_value)
        self.conn.execute(upd)

class FIN_DB(): #класс для работы с БД статей расходов
    def __init__(self): #конструктор
        self.engine = sqa.create_engine('sqlite:///fin.db')
        self.conn = self.engine.connect()
        self.data = sqa.MetaData(self.engine)
        self.fin_table = sqa.Table('fin', self.data,
                    sqa.Column('id', sqa.Integer, primary_key=True),
                    sqa.Column('description', sqa.String()),
                    sqa.Column('cost', sqa.Integer())
                    )
        self.data.create_all(self.engine)

    def insert_rec(self, descrip_value, cost_value): #добавить значение
        ins = self.fin_table.insert().values(
            description=descrip_value,
            cost=cost_value
        )
        self.conn.execute(ins)

    def delete_rec(self, value): #удалить запись
        delt = sqa.delete(self.fin_table).where(self.fin_table.c.description.like(value))
        self.conn.execute(delt)


    def select_descrip_recs(self): #выбор описаний всех статей расходов
        sel = sqa.select([self.fin_table.c.description])
        return self.conn.execute(sel).fetchall()

    def select_cost_recs(self): #выбор всех стоимостей статей расходов
        sel = sqa.select([self.fin_table.c.cost])
        return self.conn.execute(sel).fetchall()

    def sel_sum(self):#выбрать сумму стоимостей всех статей расходов
        summ = 0
        sel = sqa.select([self.fin_table.c.cost])
        summ_mass = self.conn.execute(sel).fetchall()
        for i in summ_mass:
            summ+=i[0]
        return summ


if __name__ == "__main__":
    root = tk.Tk()
    acc_db = ACC_DB()
    fin_db =FIN_DB()
    app = Main(root)
    app.pack()
    root.title("Household finance")
    root.geometry("650x340+300+200")
    root.resizable(False, False)
    root.mainloop()