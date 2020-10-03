"""
Автор: Гайдаренко Евгений Григорьевич
Задача:
Дан каталог книг.
Реализуйте библиотеку для хранения данных книг и поиску по каталогу.
Каталог должен поддерживать возможность добавления и удаления книг, редактирования информации о книге,
а также обладать персистентностью (т.е. сохранять библиотеку в внешнем файле и подгружать обратно).
Также необходимо оформить точку входа, поддерживать поиск по различным параметрам
и обеспечить интерфейс взаимодействия пользователя с библиотекой.
"""
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
import os.path
import Drivers
import linkedlist
from node import Node


SIZE_X = 400
SIZE_Y = 150


class OldLib:
    def __init__(self):
        self.num = 1
        self.result_dict = {}
        self.len_res = 0
        self.result_book_number = None
        self.result_title = None
        self.result_author = None
        self.result_genre = None
        self.current_book = None

    def create_window(self):
        """
        Функция создаёт головное окно с полями ввода данных и кнопкой поиска в каталоге по введенным данным.
        :return: None
        """
        # Создание головного окна по центру экрана.
        window1 = tk.Tk()
        window1.title('Каталог библиотеки им.Гайдаренко Е.Г.')
        w = window1.winfo_screenwidth()  # Переменная создана для удобства чтения кода
        h = window1.winfo_screenheight()  # Переменная создана для удобства чтения кода
        window1.geometry(f'{SIZE_X}x{SIZE_Y}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2}')
        window1.resizable(False, False)  # Запрет изменения размера окна

        # Отрисовка текста в окне и размещение полей ввода данных
        tk.Label(text='Название книги:').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(text='Автор:').grid(row=1, column=0, padx=10)
        tk.Label(text='Жанр:').grid(row=2, column=0, padx=10, pady=10)
        entry_title = tk.Entry(width=45)
        entry_title.grid(row=0, column=1, sticky=tk.W)
        entry_author = tk.Entry(width=45)
        entry_author.grid(row=1, column=1, sticky=tk.W)
        entry_genre = tk.Entry(width=45)
        entry_genre.grid(row=2, column=1, sticky=tk.W)

        # Создание кнопок поиска и добавления книги, а также привязка к ним функций
        button_search = tk.Button(window1, text='Поиск')
        button_search.bind('<Button-1>',
                           lambda x: self.search_window(entry_title.get(), entry_author.get(), entry_genre.get()))
        button_search.grid(row=4, column=1, sticky=tk.W, pady=10)
        button_add = tk.Button(window1, text='Добавить')
        button_add.bind('<Button-1>', lambda x: self.add_book(entry_title.get(), entry_author.get(), entry_genre.get()))
        button_add.grid(row=4, column=1, sticky=tk.E, pady=10)
        window1.mainloop()

    def search(self, title: str, author: str, genre: str) -> None:
        """
        Функция выполняет поиск в каталоге (linkedlist) по переданным данным.
        :param title: Строка с названием книги
        :param author: Строка с фамилией (возможно с инициалами) автора книги
        :param genre: Строка с жанром книги
        :return: None
        """
        number = 0
        self.result_dict = {}
        self.num = 1
        for node_val in self.l_from_file:
            if not title or title == node_val["title"]:
                if not author or author == node_val["author"]:
                    if not genre or genre == node_val["genre"]:
                        number += 1
                        self.result_dict[number] = {"title": node_val["title"],
                                                    "author": node_val["author"],
                                                    "genre": node_val["genre"]}

    def search_window(self, title: str, author: str, genre: str) -> None:
        """
        Функция создаёт окно, которое появляется ровно над головным, тем самым скрывая его.
        И выдает информацию по текущей книге. Переключение между книгами осуществляется с помощью кнопок.
        :param title: Строка с названием книги
        :param author: Строка с фамилией (возможно с инициалами) автора книги
        :param genre: Строка с жанром книги
        :return: None
        """
        self.search(title, author, genre)     # словарь с результатами
        if not self.result_dict:
            return mb.showinfo('Упс!!!', 'Такой книги нет в базе')
        self.len_res = len(self.result_dict)
        # self.num = 1

        # Создание нового окна поверх всех окон
        window2 = tk.Tk()
        window2.title(f'Найдено книг: {self.len_res}')
        w = window2.winfo_screenwidth()
        h = window2.winfo_screenheight()
        window2.geometry(f'{SIZE_X}x{SIZE_Y + 50}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2}')
        # window2.grab_set()
        window2.focus_set()

        # Создание кнопок редактирования, удаления и переключения результатов
        button_edit = tk.Button(window2, text='Изменить')
        button_edit.bind('<Button-1>', self.edit_window)
        button_edit.grid(row=5, column=1, sticky=tk.W, pady=20)
        button_del = tk.Button(window2, text='Удалить')
        button_del.bind('<Button-1>', lambda x: self.del_book())
        button_del.grid(row=5, column=1, sticky=tk.E, pady=20)
        button_save_as = tk.Button(window2, text='Сохранить как...')
        button_save_as.bind('<Button-1>', self.save_as_window)
        button_save_as.grid(row=5, column=1, sticky=tk.S, pady=20)
        button_scroll_r = tk.Button(window2, text='>>')
        button_scroll_r.bind('<Button-1>', self.scroll_right)
        button_scroll_r.grid(row=5, column=2, padx=20, pady=20)
        button_scroll_l = tk.Button(window2, text='<<')
        button_scroll_l.bind('<Button-1>', self.scroll_left)
        button_scroll_l.grid(row=5, column=0, pady=20)

        # Отрисовка текста в окне
        label_space = tk.Label(window2)
        label_space.grid(row=0)
        label_book_number = tk.Label(window2, text=f'Номер книги:')
        label_book_number.grid(row=1, column=0, ipady=5)
        label_title = tk.Label(window2, text='Название книги:')
        label_title.grid(row=2, column=0, padx=5)
        label_author = tk.Label(window2, text='Автор:')
        label_author.grid(row=3, column=0, pady=5)
        label_genre = tk.Label(window2, text='Жанр:')
        label_genre.grid(row=4, column=0)

        # Размещение полей для ответов
        self.result_book_number = tk.Entry(window2, width=38)
        self.result_book_number.grid(row=1, column=1)
        self.result_title = tk.Entry(window2, width=38)
        self.result_title.grid(row=2, column=1)
        self.result_author = tk.Entry(window2, width=38)
        self.result_author.grid(row=3, column=1)
        self.result_genre = tk.Entry(window2, width=38)
        self.result_genre.grid(row=4, column=1)

        self.current_book = self.result_dict[self.num]
        self.insert()
        window2.mainloop()

    def insert(self) -> None:
        """
        Функция вставляет данные в поля окна результатов поиска
        :return: None
        """
        self.result_book_number.configure(state="normal")
        self.result_book_number.delete(0, tk.END)
        self.result_book_number.insert(0, f'{self.num} из {len(self.result_dict)}')
        self.result_book_number.configure(state="disabled")
        self.result_title.configure(state="normal")
        self.result_title.delete(0, tk.END)
        self.result_title.insert(0, self.current_book["title"])
        self.result_title.configure(state="disabled")
        self.result_author.configure(state="normal")
        self.result_author.delete(0, tk.END)
        self.result_author.insert(0, self.current_book["author"])
        self.result_author.configure(state="disabled")
        self.result_genre.configure(state="normal")
        self.result_genre.delete(0, tk.END)
        self.result_genre.insert(0, self.current_book["genre"])
        self.result_genre.configure(state="disabled")

    def scroll_left(self, *args) -> None:
        """
        Функция выполняющая вызов функции insert() с предыдущим значением резульата поиска
        :return: None
        """
        if self.num > 1:
            self.num -= 1
            self.current_book = self.result_dict[self.num]
            self.insert()

    def scroll_right(self, *args) -> None:
        """
        Функция выполняющая вызов функции insert() со следующим значением резульата поиска
        :return: None
        """
        if self.num <= len(self.result_dict) - 1:
            self.num += 1
            self.current_book = self.result_dict[self.num]
            self.insert()

    def edit_window(self, *args) -> None:
        """
        Функция создает окно редактирования книги и заполняет поля ввода по умолчанию.
        :return: None
        """
        # Создание нового окна поверх всех окон
        window3 = tk.Tk()
        window3.title(f'Редактирование книги {self.current_book["title"]}')
        w = window3.winfo_screenwidth()
        h = window3.winfo_screenheight()
        window3.geometry(f'{SIZE_X}x{SIZE_Y + 150}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2}')
        window3.focus_set()

        # Отрисовка текста в окне
        tk.Label(window3, text='Если поле будет не заполнено, то будут пустые строки').grid(row=0, column=0,
                                                                                            columnspan=2, pady=10)
        tk.Label(window3, text='Название книги:', font=10).grid(row=1, column=0)
        tk.Label(window3, text='Сейчас:').grid(row=2, column=0, sticky=tk.E)
        tk.Label(window3, text='Новое:').grid(row=3, column=0, sticky=tk.E)
        tk.Label(window3, text='Автор:', font=10).grid(row=4, column=0)
        tk.Label(window3, text='Сейчас:').grid(row=5, column=0, sticky=tk.E)
        tk.Label(window3, text=f'{self.current_book["author"]}').grid(row=5, column=1, sticky=tk.W)
        tk.Label(window3, text='Новое:').grid(row=6, column=0, sticky=tk.E)
        tk.Label(window3, text='Жанр:', font=10).grid(row=7, column=0)
        tk.Label(window3, text='Сейчас:').grid(row=8, column=0, sticky=tk.E)
        tk.Label(window3, text=f'{self.current_book["genre"]}').grid(row=8, column=1, sticky=tk.W)
        tk.Label(window3, text='Новое:').grid(row=9, column=0, sticky=tk.E)

        # Размещение полей ввода данных напротив отрисованного ранее текста
        entry_title_old = tk.Entry(window3, width=40)
        entry_title_old.grid(row=2, column=1)
        entry_title_old.insert(0, f'{self.current_book["title"]}')
        entry_title_old.configure(state="disabled")
        entry_title_new = tk.Entry(window3, width=40)
        entry_title_new.grid(row=3, column=1)
        entry_title_new.insert(0, f'{self.current_book["title"]}')
        entry_author_old = tk.Entry(window3, width=40)
        entry_author_old.grid(row=5, column=1)
        entry_author_old.insert(0, f'{self.current_book["author"]}')
        entry_author_old.configure(state="disabled")
        entry_author_new = tk.Entry(window3, width=40)
        entry_author_new.grid(row=6, column=1)
        entry_author_new.insert(0, f'{self.current_book["author"]}')
        entry_genre_old = tk.Entry(window3, width=40)
        entry_genre_old.grid(row=8, column=1)
        entry_genre_old.insert(0, f'{self.current_book["genre"]}')
        entry_genre_old.configure(state="disabled")
        entry_genre_new = tk.Entry(window3, width=40)
        entry_genre_new.grid(row=9, column=1)
        entry_genre_new.insert(0, f'{self.current_book["genre"]}')

        # Создание кнопок редактирования, удаления и переключения результатов
        button_edit = tk.Button(window3, text='Применить изменения')
        button_edit.bind('<Button-1>',
                         lambda x: self.edit_book(entry_title_new.get(), entry_author_new.get(), entry_genre_new.get()))
        button_edit.grid(row=10, column=1)
        window3.mainloop()

    def add_book(self, title: str, author: str, genre: str) -> None:
        """
        Добавление новой книги в каталог.
        Достаточно указать только наименование (например, утеряна обложка и неизвестен автор)
        :param title: Строка с названием книги
        :param author: Строка с фамилией (возможно с инициалами) автора книги
        :param genre: Строка с жанром книги
        :return None
        """
        self.l_from_file.append({"title": title, "author": author, "genre": genre})
        self.l_from_file.save()
        if self.flag:
            mb.showinfo(f"Книга добавлена в базу.", f"Название книги: {title}\nАвтор: {author}\nЖанр: {genre}")
        self.flag = True

    def del_book(self) -> None:
        """
        Функция производит удаление книги путем выгрузки в память содержимого файла и перезаписи этого файла.
        :return: None
        """
        self.l_from_file.remove(Node(self.current_book))
        self.l_from_file.save()
        self.result_dict.pop(self.num)
        self.len_res = len(self.result_dict)
        self.restructure_result_dict()
        mb.showinfo('Готово!', 'Книга удалена.')

    def edit_book(self, new_title: str, new_author: str, new_genre: str) -> None:
        """
        Функция производит редактирование инфоормации о книге.
        :param new_title: Строка с исправленным названием книги
        :param new_author: Строка с исправленной фамилией (возможно с инициалами) автора книги
        :param new_genre: Строка с исправленным жанром книги
        :return: None
        """
        if new_title:
            self.del_book()
            self.add_book(new_title, new_author, new_genre)
            mb.showinfo('Готово!', 'Книга изменена.')
        else:
            mb.showinfo("Ошибка", "Обязательно должно быть название книги!!!")

    def restructure_result_dict(self) -> None:
        """
        Обновляет словарь с результатами после внесения изменений - обеспечивает непрерывный порядок ключей
        :return: None
        """
        roster = sorted(self.result_dict.items())
        self.result_dict = {}
        for i in range(len(roster)):
            self.result_dict[i+1] = roster[i][1]

    def save_as_window(self, *args) -> None:
        """
        Функция создает новое окно, в котором можно указать файл и выбрать расширение для файла,
        в который нужно записать результаты поиска.
        :return: None
        """
        window4 = tk.Tk()
        window4.title(f'Сохранение каталога книг в новом файле')
        w = window4.winfo_screenwidth()
        h = window4.winfo_screenheight()
        window4.geometry(f'{SIZE_X}x{SIZE_Y + 150}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2}')
        window4.focus_set()

        # list(self.base_drivers.keys())

        # Отрисовка текста в окне и размещение полей ввода данных
        tk.Label(window4, text='Имя файла').grid(row=0, column=0, padx=10, pady=10)
        entry_title = tk.Entry(window4, width=35)
        entry_title.grid(row=0, column=1, sticky=tk.W)
        combobox = ttk.Combobox(window4, values=list(self.base_drivers.keys()), width=10)
        combobox.current(0)
        combobox.grid(row=0, column=3, padx=10, pady=10)

        # Создание кнопки
        button_edit = tk.Button(window4, text='Сохранить')
        button_edit.bind('<Button-1>', lambda x: self.save_as(entry_title.get(), combobox.get()))
        button_edit.grid(row=10, column=1)
        window4.focus_set()
        window4.mainloop()

    def save_as(self, filename: str, extension: str) -> None:
        """
        Функция сохраняет результаты поиска в файл с заданным именем и выбранным расширением
        :param filename: имя файла
        :param extension: расширение файла
        :return:
        """
        driver_name = self.base_drivers[extension]
        builder = Drivers.SDFabric().get_sd_driver(driver_name)
        sd = builder.build(f"{filename}.{extension}")

        l_for_save = linkedlist.LinkedList()
        for i in range(1, len(self.result_dict) + 1):
            l_for_save.append(self.result_dict[i])

        l_for_save.set_structure_driver(sd)
        l_for_save.save()
        l_for_save.clear()

    def choose_library(self) -> None:
        """
        Выбор каталога с книгами. Исходя из расширения файла, автоматически выбирается драйвер.
        :return: None
        """
        # создание окна
        window0 = tk.Tk()
        window0.title('Каталог библиотеки им.Гайдаренко Е.Г.')
        w = window0.winfo_screenwidth()  # Переменная создана для удобства чтения кода
        h = window0.winfo_screenheight()  # Переменная создана для удобства чтения кода
        window0.geometry(f'{SIZE_X}x{SIZE_Y}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2}')
        window0.resizable(False, False)

        # расположение текста
        tk.Label(text=f"Какую библиотеку Вы бы хотели открыть?\n"
                      f"Укажите название файла с расширением.").grid(row=0, column=0, padx=10, pady=10)
        entry_title = tk.Entry(width=21)
        entry_title.grid(row=0, column=1, sticky=tk.W)

        # создание кнопки
        button_search = tk.Button(window0, text='Поиск')
        button_search.bind('<Button-1>', lambda x: self.finish(entry_title.get(), window0))
        button_search.grid(row=4, column=1, sticky=tk.W, pady=10)

        window0.mainloop()

    def finish(self, filename: str, window0) -> None:
        """
        Automatically detects driver based on file extension.
        :param filename: filename with extension
        :return: None
        """
        self.base_drivers = Drivers.SDFabric.get_driver_base()
        if os.path.isfile(filename):
            driver_name = self.base_drivers[filename.split('.')[1]]
            builder = Drivers.SDFabric().get_sd_driver(driver_name)
            sd = builder.build(filename)
            self.l_from_file = linkedlist.LinkedList()
            self.l_from_file.set_structure_driver(sd)
            self.l_from_file.load()  # закачка линкедлиста из файла
            window0.destroy()
            self.create_window()


if __name__ == '__main__':
    t1 = OldLib()
    t1.choose_library()
