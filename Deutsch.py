import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()


    def init_main(self):
        toolbar = tk.Frame(bg="#8DCFFF", bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        #self.add_img = tk.PhotoImage(file='lizardman.jpg')
        button_open_dialogue = tk.Button(toolbar, text='Text', command=self.opendialog, bg="#8DCFFF", bd = 0, compound=tk.TOP) #image=self.add_img)

        button_open_dialogue.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns = ('ID', 'Description', 'Cost', 'Total'), height=15, show='headings')
        self.tree.column('ID', width=150, anchor=tk.CENTER)
        self.tree.column('Description', width=150, anchor=tk.CENTER)
        self.tree.column('Cost', width=150, anchor=tk.CENTER)
        self.tree.column('Total', width=150, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('Description', text='Наименование')
        self.tree.heading('Cost', text='Доход/Расход')
        self.tree.heading('Total', text='Сумма')

        self.tree.pack()


    def opendialog(self):
        Child()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Добавить')
        self.geometry('400x400+400+300')
        self.resizable(False,False)

        label_description = tk.Label(self, text="Наименование")
        label_description.place(x=50, y=50)

        label_select = tk.Label(self, text="Доход/расход")
        label_select.place(x=50, y=80)

        label_sum = tk.Label(self, text="Сумма")
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        self.grab_set()
        self.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Deutsch Words Remembering")
    root.geometry("660x400+100+200")
    root.resizable(True, True)
    root.mainloop()