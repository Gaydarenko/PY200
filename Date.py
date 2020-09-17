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
        self.__is_valid_date(*args)
        self._year, self._month, self._day = args

    def __str__(self) -> str:
        """
        Redetermine func __str__ for user
        :return: string format '23.11.2018'
        """
        return f'{self._day}.{self._month}.{self._year}'

    def __repr__(self) -> str:
        """
        Redetermine func __repr__ for programmers
        :return: string format 'Date(2018, 11, 23)'
        """
        return f'Date({self._year}, {self._month}, {self._day})'

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Verification leap year
        :param year:year of interesting for check leap
        :return: True or False
        """
        return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

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
        # return self._date
        return f'{self._day}, {self._month}, {self._year}'

    @classmethod
    def __is_valid_date(cls, *args: int) -> None:
        """
        Verification day
        :param args: [year, month, day]
        :return: None
        """
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
        if args[2] not in range(1, days_in_months[args[1] - 1] + 1):
            raise ValueError(f'Value day must be in range from 1 to {days_in_months[args[1] - 1]}')

    @date.setter
    def date(self, value):
        try:
            args = value.split('.')
            if len(args) == 3:
                self._year, self._month, self._day = list(map(int, args))
            else:
                raise ValueError
        except TypeError:
            print('Value date must be string')
        except ValueError:
            print('Value date must be string in next format: "year.month.day"')

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self.__is_valid_date(self._year, self._month, value)
        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self.__is_valid_date(self._year, value, self._day)
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self.__is_valid_date(value, self._month, self._day)
        self._year = value

    def add_day(self, days):
        try:
            self._day += days
        except ValueError:
            days -= self.DAY_OF_MONTH[self.is_leap_year(self._year)][self._month - 1] - self._day + 1
            self._day = 1
            self.add_month(1)
            while days >= self.DAY_OF_MONTH[self.is_leap_year(self._year)][self._month - 1]:
                days -= self.DAY_OF_MONTH[self.is_leap_year(self._year)][self._month - 1]
                self.add_month(1)
            self._day += days

    def add_month(self, month: int) -> None:
        """
        Function add some years to self.year
        :param month: adding year
        :return: None
        """
        remain = 12 - self._month
        if month <= remain:
            self._month += month
        else:
            remain = month - remain
            self.year += 1 + remain // 12
            self.month = remain % 12
            try:
                self.__is_valid_date(self._year, self._month, self._day)
            except ValueError:
                self._day = self.DAY_OF_MONTH[self.is_leap_year(self._year)][self._month - 1]   # присвоение последнего
                                                                                                # дня этого месяца

    def add_year(self, year: int) -> None:
        """
        Function add some years to self.year
        :param year: adding year
        :return: None
        """
        self._year += year
        try:
            self.__is_valid_date(self._year, self._month, self._day)
        except ValueError:
            self._day = self.DAY_OF_MONTH[self.is_leap_year(self._year)][self._month - 1]

    @staticmethod
    def date2_date1(date2, date1):
        # date2 = date2.split('.')
        # if len(date2) == 3:
        #     self.year, self.month, self.day = list(map(int, date2))
        # else:
        #     raise ValueError('Value date must be string in next format: "year.month.day"')

        pass    # не могу разобраться как вызвать тот же self.year, ...


if __name__ == "__main__":
    d1 = Date(2019, 9, 11)
    print(d1)
    print(repr(d1))
    d2 = Date(2020, 2, 29)
    print(d2)
    # d3 = Date(2019, 2, 29)
    # print(d3)
    d2.add_year(2)
    print(f'+2 year = {d2}')

    # d2.add_month(2)
    # print(f'+2 month = {d2}')
    # d2.add_month(10)
    # print(f'+10 month = {d2}')
    d2.add_month(11)
    print(f'+11 month = {d2}')
    # d2.add_month(12)
    # print(f'+12 month = {d2}')
    d2.date = '2020.9.11'
    print(f'd2.date={d2.date}')

    print(d2.is_leap_year(2020))

    d2.add_month(10)
    print(d2)
    d2.add_day(33)
    print(d2)

    d3 = Date(2019, 10, 10)
    d3.add_day(30)
    print(d3)

    d3.date2_date1('2222.9.11', '2111.9.11')
