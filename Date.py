
# coding: utf-8

# Разработка класса данных
# Примеры:
# date = Date(2018, 11, 23)
# print(date) # 23.11.2018
# repr(date)  # Date(2018, 11, 23)

# date = Date(2018, 11, 31)

# date.date = '31.11.2018'
# print(date.date) # '31.11.2018'

# date.day   = 31 # Запрет
# date.month = 50 #
# date.month = 11 # 02 -> 01.03
# date.year       # на след. месяц


class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

    def __init__(self, *args):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @staticmethod
    def is_leap_year(year):
        return False  #

    @classmethod
    def get_max_day(cls, year, month):
        pass

    @property
    def date(self):
        pass

    @classmethod
    def __is_valid_date(cls, *args):
        pass

    @date.setter
    def date(self, value):
        pass

    @property
    def day(self):
        pass

    @property
    def month(self):
        pass

    @property
    def year(self):
        pass

    def add_day(self, day):
        pass

    def add_month(self, month):
        pass

    def add_year(self, year):
        pass

    @staticmethod
    def date2_date1(date2, date1):
        pass

