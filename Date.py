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
        # self.__is_valid_date(self._year, value, self._day)
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
            self.day += days
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
        if month < 0:
            raise ValueError('Month value must be only positive')

        remain = 12 - self._month
        if month <= remain:
            self._month += month
        else:
            remain = month - remain
            rem_of_div = remain % 12
            self.year += 1 + remain // 12 - (1 if not rem_of_div else 0)
            self.month = 12 if not rem_of_div else rem_of_div
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
        if year < 0:
            raise ValueError('Month year must be only positive')
        self._year += year
        try:
            self.__is_valid_date(self._year, self._month, self._day)
        except ValueError:
            self._day = self.DAY_OF_MONTH[self.is_leap_year(self._year)][self._month - 1]

    @classmethod
    def date_from_string(cls, value):
        date = value.split('.')
        if len(date) == 3:
            try:
                year, month, day = list(map(int, date))
                cls.__is_valid_date(year, month, day)
            except TypeError:
                return 'Value year, month, day must be integer"'
        else:
            raise ValueError('Value date must be string in next format: "year.month.day"')
        return year, month, day

    @staticmethod
    def date2_date1(date2: str, date1: str) -> str:
        """
        The function counts amount of days between two dates.
        :param date2: date value 2
        :param date1: date value 1
        :return: string with amount of days
        """
        # date2_ = date2.split('.')
        # date1_ = date1.split('.')
        # if len(date2_) == 3 and len(date1_) == 3:
        #     try:
        #         year2, month2, day2 = list(map(int, date2_))
        #         year1, month1, day1 = list(map(int, date1_))
        #         Date.__is_valid_date(year2, month2, day2)
        #         Date.__is_valid_date(year1, month1, day1)
        #     except TypeError:
        #         return 'Value year, month, day must be integer"'
        # else:
        #     raise ValueError('Value date must be string in next format: "year.month.day"')
        year2, month2, day2 = Date.date_from_string(date2)
        year1, month1, day1 = Date.date_from_string(date1)

        if year2 < year1 or year2 == year1 and (month2 < month1 or month2 == month1 and day2 < day1):
            raise ValueError('date2 value must be more then date1 value')

        if year1 == year2 and month1 == month2:
            day_res = day2 - day1
        elif year1 == year2:
            day_res = sum(Date.DAY_OF_MONTH[Date.is_leap_year(year1)][month1 - 1:month2 - 1]) - day1 + day2
        else:
            days_in_year1 = sum(Date.DAY_OF_MONTH[Date.is_leap_year(year1)][month1-1:]) - day1
            days_in_years = sum(list(map(lambda x: sum(Date.DAY_OF_MONTH[Date.is_leap_year(x)]), range(year1 + 1, year2))))
            days_in_year2 = sum(Date.DAY_OF_MONTH[Date.is_leap_year(year2)][:month2 - 1]) + day2

            day_res = days_in_year1 + days_in_years + days_in_year2

        return f'{day_res} days between {date2} and {date1}'


if __name__ == "__main__":
    # Сюда смотреть не надо - это промежуточные тесты для быстрой отладки в процессе написания кода.
    # Все тесты  реализованы в tests_date.py

    # d1 = Date(2019, 9, 11)
    # print(d1)
    # print(repr(d1))
    # d2 = Date(2020, 2, 29)
    # print(d2)
    # # d3 = Date(2019, 2, 29)
    # # print(d3)
    # d2.add_year(2)
    # print(f'+2 year = {d2}')
    #
    # # d2.add_month(2)
    # # print(f'+2 month = {d2}')
    # # d2.add_month(10)
    # # print(f'+10 month = {d2}')
    # d2.add_month(11)
    # print(f'+11 month = {d2}')
    # # d2.add_month(12)
    # # print(f'+12 month = {d2}')
    # d2.date = '2020.9.11'
    # print(f'd2.date={d2.date}')
    #
    # print(d2.is_leap_year(2020))
    #
    # d2.add_month(10)
    # print(d2)
    # d2.add_day(33)
    # print(d2)
    #
    # d3 = Date(2019, 10, 10)
    # d3.add_day(30)
    # print(d3)
    #
    # d3.date2_date1('2222.9.11', '2111.9.11')

    # ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))
    # year1, month1, day1 = 2019, 8, 10
    # delta1 = sum(Date.DAY_OF_MONTH[Date.is_leap_year(year1)][month1-1:]) - day1
    # print(delta1)   # must be 143
    # year2, month2, day2 = 2020, 9, 20
    # delta2 = sum(Date.DAY_OF_MONTH[Date.is_leap_year(year2)][:month2-1]) + day2
    # print(delta2)   # must be 264
    # delta = sum(list(map(lambda x: sum(Date.DAY_OF_MONTH[Date.is_leap_year(x)]), range(year1+1, year2))))
    # print(delta)
    # print(delta2 + delta1 + delta)

    # d1 = Date(838, 3, 31)
    # d1.add_month(11)
    # print(d1)


    for i in range(1,100):
        d1 = Date(838, 3, 31)
        d1.add_month(i)
        print(d1)

