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
        self.year = args[0]
        self.month = args[1]
        self.day = args[2]

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Verification leap year
        :param year:year of interesting for check leap
        :return: True or False
        """
        return True if year % 4 == 0 and year % 100 != 0 else False

    @classmethod
    def get_max_day(cls, year: int, month: int) -> int:
        """
        Determines the number of days in the month of interest, taking into account the (no)leap year
        :param year: year of interesting
        :param month: month of interesting
        :return: return max day in month of inter
        """
        if month == 2:
            return cls.DAY_OF_MONTH[cls.is_leap_year(year)][1]
        else:
            return cls.DAY_OF_MONTH[0][month - 1]

    @property
    def date(self):
        pass

    @classmethod
    def __is_valid_date(cls, *args):
        if not isinstance(args[0], int):
            raise ValueError('Value year must be int')
        if args[0] < 1:
            raise ValueError('Value year must be only positive')

        if not isinstance(args[1], int):
            raise ValueError('Value month must be int')
        if args[1] not in range(1, 13):
            raise ValueError('Value month must be in range from 1 to 12')

        days_in_months = cls.DAY_OF_MONTH[cls.is_leap_year(args[0])]
        if not isinstance(args[2], int):
            raise ValueError('Value day must be int')
        if args[2] not in range(1, days_in_months[args[1] + 1]):
            raise ValueError(f'Value day must be in range from 1 to {days_in_months[args[1]]}')

    @date.setter
    def date(self, value):
        pass

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self.__is_valid_date(self.year, self.month, value)
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self.__is_valid_date(self.year, value, self.day)
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self.__is_valid_date(value, self.month, self.day)
        self._year = value

    def add_day(self, day):
        pass

    def add_month(self, month):
        pass

    def add_year(self, year):
        pass

    @staticmethod
    def date2_date1(date2, date1):
        pass
