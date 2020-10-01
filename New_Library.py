import tkinter as tk


class Library(tk.Frame):
    def __init__(self, win1):
        super().__init__(win1)
        self.init_gui()

    def init_gui(self):
        # tb = tk.Frame(bg="#d7d8e0", bd=5)
        # tb.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="old_library/3.png")
        # button_search = tk.Button(tb, text="Поиск", command=self.open_dialog, bg="#d7d8e0", bd=0,
        #                           compound=tk.TOP, image=self.add_img)
        # button_search.pack(side=tk.LEFT)

        self.search_button()
        self.add_button()

    def search_button(self) -> None:
        """
        Add button "Поиск" in lower left corner for open new search book window.
        :return: None
        """
        button_search = tk.Button(window1, text='Поиск')
        button_search.bind('<Button-1>', self.open_dialog)
        button_search.grid(row=4, column=1, sticky=tk.W, pady=10)

    def add_button(self) -> None:
        """
        Add button "Добавить" in lower right corner for open new add book window.
        :return: None
        """
        button_add = tk.Button(window1, text='Добавить')
        button_add.bind('<Button-1>', self.open_dialog)     # need self.add_book_window
        button_add.grid(row=4, column=2, sticky=tk.E, pady=10)

    def open_dialog(self, *args):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(window1)
        self.init_child()

    def init_child(self):
        self.title("Some text1")
        self.geometry("400x200+400+300")
        self.resizable(False, False)

        self.grab_set()     # Перехват всех событий
        self.focus_set()    # Удержание фокуса окна


if __name__ == "__main__":
    window1 = tk.Tk()
    app = Library(window1)
    # app.pack()
    window1.title("My Library")
    SIZE_X = 400
    SIZE_Y = 150
    w = window1.winfo_screenwidth()
    h = window1.winfo_screenheight()
    window1.geometry(f'{SIZE_X}x{SIZE_Y}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2 - 100}')
    window1.resizable(False, False)
    window1.mainloop()
