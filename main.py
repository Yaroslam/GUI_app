import tkinter as tk


# главгое окно
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self): #fubction for built main window
        left_footer = tk.Frame(bg = "black", bd = 2)
        left_footer.pack(side = tk.LEFT, fill = tk.Y)

        btn_recount = tk.Button(left_footer,text = "add", command = self.open_child)  #button is open recount window
        btn_recount.pack()


    def open_child(self):
        Recount()


# окно ввода денег
class Recount(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self): #function for built recount window
        self.money = tk.Entry(self) #add money
        self.state_of_recount = tk.Entry(self) #add state of earninig or spending

        self.describ_money = tk.Label(self, text = "money")
        self.describ_state = tk.Label(self, text="state")

        self.describ_money.pack()
        self.describ_state.pack()
        self.money.pack()
        self.state_of_recount.pack()


        self.geometry("300x300")
        self.title("окно номер 2")
        self.grab_set()
        self.focus_set()




if __name__ == "__main__":
        root = tk.Tk()
        app = Main(root)
        app.pack()
        root.title("придумаю еще")
        root.geometry("650x450+300+200")
        root.resizable(False, False)
        root.mainloop()
