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
import json

SIZE_X = 400
SIZE_Y = 150

global num


def create_window():
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
    button_search.bind('<Button-1>', lambda x: search_window(entry_title.get(), entry_author.get(), entry_genre.get()))
    button_search.grid(row=4, column=1, sticky=tk.W, pady=10)
    button_add = tk.Button(window1, text='Добавить')
    button_add.bind('<Button-1>', lambda x: add_book(entry_title.get(), entry_author.get(), entry_genre.get()))
    button_add.grid(row=4, column=1, sticky=tk.E, pady=10)
    window1.mainloop()


def search(title: str, author: str, genre: str):
    """
    Функция выполняет поиск в каталоге по переданным данным.
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return roster: Список книг (с данными), удовлетворяющих параметрам поиска либо None
    """

    roster = []

    with open('catalog.lib', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = list(map(lambda x: x.capitalize(), json.loads(line)))
        target = list(map(lambda x: x.capitalize(), [title, author, genre]))
        if title == '':
            target[0] = line[0]
        if author == '':
            target[1] = line[1]
        if genre == '':
            target[2] = line[2]

        if line == target:
            roster.append(line)
    if not roster:
        return None
    return roster


def search_window(title: str, author: str, genre: str):
    """
    Функция создаёт окно, которое появляется ровно над головным, тем самым скрывая его.
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return: None
    """

    def insert(book: list):
        """
        Функция вставляет данные в поля окна результатов поиска
        :param book: Список данных книги
        :return: None
        """
        result_book_number.configure(state="normal")
        result_book_number.delete(0, tk.END)
        result_book_number.insert(0, f'{num + 1} из {len_res}')
        result_book_number.configure(state="disabled")
        result_title.configure(state="normal")
        result_title.delete(0, tk.END)
        result_title.insert(0, book[0])
        result_title.configure(state="disabled")
        result_author.configure(state="normal")
        result_author.delete(0, tk.END)
        result_author.insert(0, book[1])
        result_author.configure(state="disabled")
        result_genre.configure(state="normal")
        result_genre.delete(0, tk.END)
        result_genre.insert(0, book[2])
        result_genre.configure(state="disabled")

    def scroll_right():
        """
        Функция выполняющая вызов функции insert() с следующим значением резульата поиска
        :return: None
        """
        global num
        if num + 1 < len(results):
            num += 1
            insert(results[num])

    def scroll_left():
        """
        Функция выполняющая вызов функции insert() с предыдущим значением резульата поиска
        :return: None
        """
        global num
        if num - 1 >= 0:
            num -= 1
            insert(results[num])

    global num
    num = 0

    if [title, author, genre] == ['', '', '']:
        return None

    results = search(title, author, genre)
    if not results:
        return mb.showinfo('Упс!!!', 'Такой книги нет в базе')
    len_res = len(results)

    # Создание нового окна поверх всех окон
    window2 = tk.Tk()
    window2.title(f'Найдено книг: {len_res}')
    w = window2.winfo_screenwidth()
    h = window2.winfo_screenheight()
    window2.geometry(f'{SIZE_X}x{SIZE_Y + 50}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2}')
    window2.grab_set()
    window2.focus_set()

    # Создание кнопок редактирования, удаления и переключения результатов
    button_edit = tk.Button(window2, text='Изменить')
    button_edit.bind('<Button-1>', lambda x: edit_window(results[num][0], results[num][1], results[num][2]))
    button_edit.grid(row=5, column=1, sticky=tk.W, pady=20)
    button_del = tk.Button(window2, text='Удалить')
    button_del.bind('<Button-1>', lambda x: del_book(results[num][0], results[num][1], results[num][2]))
    button_del.grid(row=5, column=1, sticky=tk.E, pady=20)
    button_scroll_r = tk.Button(window2, text='>>')
    button_scroll_r.bind('<Button-1>', lambda x: scroll_right())
    button_scroll_r.grid(row=5, column=2, padx=20, pady=20)
    button_scroll_l = tk.Button(window2, text='<<')
    button_scroll_l.bind('<Button-1>', lambda x: scroll_left())
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
    result_book_number = tk.Entry(window2, width=38)
    result_book_number.grid(row=1, column=1)
    result_book_number.insert(0, f'{num + 1} из {len_res}')
    result_book_number.configure(state="disabled")
    result_title = tk.Entry(window2, width=38)
    result_title.grid(row=2, column=1)
    result_title.insert(0, results[num][0])
    result_title.configure(state="disabled")
    result_author = tk.Entry(window2, width=38)
    result_author.grid(row=3, column=1)
    result_author.insert(0, results[num][1])
    result_author.configure(state="disabled")
    result_genre = tk.Entry(window2, width=38)
    result_genre.grid(row=4, column=1)
    result_genre.insert(0, results[num][2])
    result_genre.configure(state="disabled")

    window2.mainloop()


def edit_window(title, author, genre):
    """
    Функция создает окно редактирования книги и заполняет поля ввода по умолчанию (для удобства).
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return: None
    """

    # Создание нового окна поверх всех окон
    window3 = tk.Tk()
    window3.title(f'Редактирование книги {title}')
    w = window3.winfo_screenwidth()
    h = window3.winfo_screenheight()
    window3.geometry(f'{SIZE_X}x{SIZE_Y + 150}+{w // 2 - SIZE_X // 2}+{h // 2 - SIZE_Y // 2}')
    window3.grab_set()
    window3.focus_set()

    # Отрисовка текста в окне
    tk.Label(window3, text='Если поле будет не заполнено, то будут пустые строки').grid(row=0, column=0,
                                                                                        columnspan=2, pady=10)
    tk.Label(window3, text='Название книги:', font=10).grid(row=1, column=0)
    tk.Label(window3, text='Сейчас:').grid(row=2, column=0, sticky=tk.E)
    tk.Label(window3, text='Новое:').grid(row=3, column=0, sticky=tk.E)
    tk.Label(window3, text='Автор:', font=10).grid(row=4, column=0)
    tk.Label(window3, text='Сейчас:').grid(row=5, column=0, sticky=tk.E)
    tk.Label(window3, text=f'{author}').grid(row=5, column=1, sticky=tk.W)
    tk.Label(window3, text='Новое:').grid(row=6, column=0, sticky=tk.E)
    tk.Label(window3, text='Жанр:', font=10).grid(row=7, column=0)
    tk.Label(window3, text='Сейчас:').grid(row=8, column=0, sticky=tk.E)
    tk.Label(window3, text=f'{genre}').grid(row=8, column=1, sticky=tk.W)
    tk.Label(window3, text='Новое:').grid(row=9, column=0, sticky=tk.E)

    # Размещение полей ввода данных напротив отрисованного ранее текста
    entry_title_old = tk.Entry(window3, width=40)
    entry_title_old.grid(row=2, column=1)
    entry_title_old.insert(0, f'{title}')
    entry_title_old.configure(state="disabled")
    entry_title_new = tk.Entry(window3, width=40)
    entry_title_new.grid(row=3, column=1)
    entry_title_new.insert(0, f'{title}')
    entry_author_old = tk.Entry(window3, width=40)
    entry_author_old.grid(row=5, column=1)
    entry_author_old.insert(0, f'{author}')
    entry_author_old.configure(state="disabled")
    entry_author_new = tk.Entry(window3, width=40)
    entry_author_new.grid(row=6, column=1)
    entry_author_new.insert(0, f'{author}')
    entry_genre_old = tk.Entry(window3, width=40)
    entry_genre_old.grid(row=8, column=1)
    entry_genre_old.insert(0, f'{genre}')
    entry_genre_old.configure(state="disabled")
    entry_genre_new = tk.Entry(window3, width=40)
    entry_genre_new.grid(row=9, column=1)
    entry_genre_new.insert(0, f'{genre}')

    # Создание кнопок редактирования, удаления и переключения результатов
    button_edit = tk.Button(window3, text='Применить изменения')
    button_edit.bind('<Button-1>', lambda x: edit_book(title, author, genre, entry_title_new.get(),
                                                       entry_author_new.get(), entry_genre_new.get()))
    button_edit.grid(row=10, column=1)
    window3.mainloop()


def add_book(title: str, author: str, genre: str):
    """
    Добавление новой книги в каталог.
    Достаточно указать только наименование (например, утеряна обложка и неизвестен автор)
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return None
    """
    target = list(map(lambda x: x.capitalize(), [title, author, genre]))
    if len(title):
        with open('catalog.lib', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                line = list(map(lambda x: x.capitalize(), json.loads(line)))
                if line == target:
                    return mb.showinfo('Упс!!!', 'Такая книга уже существует')
        with open('catalog.lib', 'a', encoding='utf-8') as file:
            json.dump(target, file, ensure_ascii=False)
            file.write(f'\n')
        mb.showinfo(f"Книга добавлена в базу.", f"Название книги: {target[0]}\nАвтор: {target[1]}\nЖанр: {target[2]}")


def del_book(title: str, author: str, genre: str):
    """
    Функция производит удаление книги путем выгрузки в память содержимого файла и перезаписи этого файла.
    Также производится подсчет количества удаленных книг.
    :param title: Строка с названием книги
    :param author: Строка с фамилией (возможно с инициалами) автора книги
    :param genre: Строка с годом выпуска книги
    :return: None
    """
    count = 0
    if len(title):
        with open('catalog.lib', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        file = open('catalog.lib', 'w')  # очиска файла
        file.close  # очиска файла

        with open('catalog.lib', 'a', encoding='utf-8') as file:
            for line in lines:
                line = list(map(lambda x: x.capitalize(), json.loads(line)))
                if line != [title, author, genre]:
                    json.dump(line, file, ensure_ascii=False)
                    file.write(f'\n')
                else:
                    count = 1
    if count:
        mb.showinfo('Готово!', 'Книга удалена.')
    else:
        mb.showinfo('Упс!!!', 'Что-то пошло не так')


def edit_book(title: str, author: str, genre: str, new_title: str, new_author: str, new_genre: str):
    """
    Функция производит редактирование инфоормации о книге.
    :param title: Строка с неисправленным названием книги
    :param author: Строка с неисправленной фамилией (возможно с инициалами) автора книги
    :param genre: Строка с неисправленным годом выпуска книги
    :param new_title: Строка с исправленным названием книги
    :param new_author: Строка с исправленной фамилией (возможно с инициалами) автора книги
    :param new_genre: Строка с исправленным годом выпуска книги
    :return: None
    """
    count = 0
    if len(new_title):
        with open('catalog.lib', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        file = open('catalog.lib', 'w')  # очиска файла
        file.close  # очиска файла

        target = list(map(lambda x: x.capitalize(), [new_title, new_author, new_genre]))
        with open('catalog.lib', 'a', encoding='utf-8') as file:
            for line in lines:
                line = list(map(lambda x: x.capitalize(), json.loads(line)))
                if line == [title, author, genre]:
                    json.dump(target, file, ensure_ascii=False)
                    file.write(f'\n')
                elif line == target:
                    count += 1
                    continue
                else:
                    json.dump(line, file, ensure_ascii=False)
                    file.write(f'\n')
        if count:
            mb.showinfo('Готово!', f'Такая книга уже существует.\nЗаписи были объединены.')
        else:
            mb.showinfo('Готово!', 'Изменения данных о книге успешно применены.')
    else:
        mb.showinfo('Внимание', 'Необходимо указать название книги!')


if __name__ == '__main__':
    # a = [["Унесенные ветром", "Евген у.К.", "наука"],
    #      ["Физика", "Евген", "наука"],
    #      ["Алгебра", "Евген", "наука"],
    #      ["Химия", "Евген", "наука"],
    #      ["Ботаника", "Елена", "наука"],
    #      ["Физ-ра", "Евген", "спорт"],
    #      ["1", "2", "3"]]

    # Проверка функции добавления книг
    # for i in a:
    #     title = i[0]
    #     author = i[1]
    #     genre = i[2]
    #     add_book(title, author, genre)

    # Проверка функции удаления книг
    # del_book("Химия", "Евген", "наука")

    create_window()
