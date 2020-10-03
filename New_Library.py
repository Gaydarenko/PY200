import tkinter as tk
import linkedlist


class Main(tk.Frame):
    def __init__(self, win1):
        super().__init__(win1)
        self.SIZE_X = 400
        self.SIZE_Y = 150
        self.w = window1.winfo_screenwidth()
        self.h = window1.winfo_screenheight()
        self.start()
        # self.main_window()

    def start(self):
        window1.title('Каталог библиотеки им.Гайдаренко Е.Г.')
        window1.geometry(
            f'{self.SIZE_X}x{self.SIZE_Y}+{self.w // 2 - self.SIZE_X // 2}+{self.h // 2 - self.SIZE_Y // 2 - 100}')
        window1.resizable(False, False)
        tk.Label(text='Имя библиотеки').grid(row=0, column=0, padx=10, pady=10)
        entry_title = tk.Entry(width=45)
        entry_title.grid(row=0, column=1, sticky=tk.W)
        button_search = tk.Button(window1, text='Open')
        button_search.bind('<Button-1>', self.finish)
        button_search.grid(row=4, column=1, sticky=tk.W, pady=10)


    def finish(self, *args):
        self.destroy()
        self.main_window()


    def main_window(self):
        # tb = tk.Frame(bg="#d7d8e0", bd=5)
        # tb.pack(side=tk.TOP, fill=tk.X)

        # self.add_img = tk.PhotoImage(file="old_library/3.png")
        # button_search = tk.Button(tb, text="Поиск", command=self.open_dialog, bg="#d7d8e0", bd=0,
        #                           compound=tk.TOP, image=self.add_img)
        # button_search.pack(side=tk.LEFT)

        window1.title('Каталог библиотеки им.Гайдаренко Е.Г.')
        window1.geometry(f'{self.SIZE_X}x{self.SIZE_Y}+{self.w // 2 - self.SIZE_X // 2}+{self.h // 2 - self.SIZE_Y // 2 - 100}')
        window1.resizable(False, False)

        self.main_window_text()
        self.search_button()
        self.add_button()

    def main_window_text(self) -> None:
        """
        Rendering text in a window and placing data entry fields.
        :return: None
        """
        tk.Label(text='Название книги:').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(text='Автор:').grid(row=1, column=0, padx=10)
        tk.Label(text='Жанр:').grid(row=2, column=0, padx=10, pady=10)
        entry_title = tk.Entry(width=45)
        entry_title.grid(row=0, column=1, sticky=tk.W)
        entry_author = tk.Entry(width=45)
        entry_author.grid(row=1, column=1, sticky=tk.W)
        entry_genre = tk.Entry(width=45)
        entry_genre.grid(row=2, column=1, sticky=tk.W)

    def search_button(self) -> None:
        """
        Add button "Поиск" in lower left corner for open new search book window.
        :return: None
        """
        button_search = tk.Button(window1, text='Поиск')
        button_search.bind('<Button-1>', self.open_search_window)
        button_search.grid(row=4, column=1, sticky=tk.W, pady=10)

    def add_button(self) -> None:
        """
        Add button "Добавить" in lower right corner for open new add book window.
        :return: None
        """
        button_add = tk.Button(window1, text='Добавить')
        button_add.bind('<Button-1>', self.add_book)     # need self.add_book_window
        button_add.grid(row=4, column=1, sticky=tk.E, pady=10)

    def open_search_window(self, *args):
        l_list = linkedlist.LinkedList()
        l_list.load()
        # print(type(l_list))     # for check
        SearchResult()

    def add_book(self, *args):
        pass


class SearchResult(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.SIZE_X = 400
        self.SIZE_Y = 150
        self.w = window1.winfo_screenwidth()
        self.h = window1.winfo_screenheight()
        self.search_window()
        self.roster = []

    def search_window(self):
        self.title("Результаты поиска")
        self.geometry(f'{self.SIZE_X}x{self.SIZE_Y + 50}+{self.w // 2 - self.SIZE_X // 2}+{self.h // 2 - self.SIZE_Y // 2 - 100}')
        self.resizable(False, False)

        self.text()
        self.answers()
        self.scroll_left_button()
        self.scroll_right_button()

        self.grab_set()     # Перехват всех событий
        self.focus_set()    # Удержание фокуса окна

    def text(self) -> None:
        """
        Rendering text in a window.
        :return: None
        """
        label_space = tk.Label(self)
        label_space.grid(row=0)
        label_book_number = tk.Label(self, text=f'Номер книги:')
        label_book_number.grid(row=1, column=0, ipady=5)
        label_title = tk.Label(self, text='Название книги:')
        label_title.grid(row=2, column=0, padx=5)
        label_author = tk.Label(self, text='Автор:')
        label_author.grid(row=3, column=0, pady=5)
        label_genre = tk.Label(self, text='Жанр:')
        label_genre.grid(row=4, column=0)

    def answers(self):
        num = 0
        len_res = 0
        results = {0: ('-', '-', '-')}
        result_book_number = tk.Entry(self, width=38)
        result_book_number.grid(row=1, column=1)
        result_book_number.insert(0, f'{num + 1} из {len_res}')
        result_book_number.configure(state="disabled")
        result_title = tk.Entry(self, width=38)
        result_title.grid(row=2, column=1)
        result_title.insert(0, results[num][0])
        result_title.configure(state="disabled")
        result_author = tk.Entry(self, width=38)
        result_author.grid(row=3, column=1)
        result_author.insert(0, results[num][1])
        result_author.configure(state="disabled")
        result_genre = tk.Entry(self, width=38)
        result_genre.grid(row=4, column=1)
        result_genre.insert(0, results[num][2])
        result_genre.configure(state="disabled")


    def scroll_right_button(self) -> None:
        """
        Add button ">>" in lower right corner for open next search result.
        :return: None
        """
        button_scroll_r = tk.Button(self, text='>>')
        button_scroll_r.bind('<Button-1>', self.tmp)
        button_scroll_r.grid(row=5, column=2, padx=20, pady=20)

    def scroll_left_button(self) -> None:
        """
        Add button "<<" in lower right corner for open next search result
        :return: None
        """
        button_scroll_l = tk.Button(self, text='<<')
        button_scroll_l.bind('<Button-1>', self.tmp)
        button_scroll_l.grid(row=5, column=0, pady=20)

    def tmp(self):
        pass



if __name__ == "__main__":
    window1 = tk.Tk()
    app = Main(window1)
    # app.pack()
    # window1.title('Каталог библиотеки им.Гайдаренко Е.Г.')
    # SIZE_X = 400
    # SIZE_Y = 150
    # w = window1.winfo_screenwidth()
    # h = window1.winfo_screenheight()
    # window1.geometry(f'{SIZE_X}x{SIZE_Y}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2 - 100}')
    # window1.resizable(False, False)
    window1.mainloop()
