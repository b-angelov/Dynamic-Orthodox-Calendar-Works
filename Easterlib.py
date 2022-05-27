class EasterCalculus:

    def __init__(self, year=2022, mode="JulianInGregorian",
                 adoption={"adoptionYear": 1582, "adoption": "exclusive", "gregPriorAdoption": False}):
        self.year = year
        self.leap = self.isLeap(year, mode)
        self.adoptionYear = adoption["adoptionYear"]
        self.adoption = adoption["adoption"]
        self.gregPriorAdoption = adoption["gregPriorAdoption"]
        self.mode = mode.lower()
        self.month = None
        self.day = None
        self.date = None
        self.set(year)

    def set(self, year=None, mode=None):
        date = []
        if not year:
            year = self.year
        if not mode:
            mode = self.mode
        mode = mode.lower()
        if mode == "Julian".lower():
            self.date = self.JulianCal(year)
            self.leap = self.isLeap(year, "Julian")
        elif mode == "JulianInGregorian".lower():
            date = self.JulianCal(year)
            self.date = self.JulianInGregorian(date[0], date[1], year)
        elif mode == "GaussGregorian".lower():
            self.date = self.GaussAlgorithm(year, "Gregorian")
        elif mode == "GaussJulian".lower() or self.gregPriorAdoption is False:
            self.date = self.GaussAlgorithm(year)
            self.leap = self.isLeap(year, "Julian")
        elif mode == "GaussJulianInGregorian".lower():
            date = self.GaussAlgorithm(year)
            self.date = self.JulianInGregorian(date[0], date[1], year)
        elif mode == "AnonymousGregorian".lower():
            self.date = self.AnonymousGregorian(year, "original")
        elif mode == "AnonymousGregorianOptimized".lower():
            self.date = self.AnonymousGregorian(year)

        self.month = self.date[0]
        self.day = self.date[1]
        self.year = year
        return date

    def JulianCal(self, year):
        a = year % 4
        b = year % 7
        c = year % 19
        d = (19 * c + 15) % 30
        e = (2 * a + 4 * b - d + 34) % 7
        month = (d + e + 114) // 31
        day = ((d + e + 114) % 31) + 1
        return [month, day]

    def JulianInGregorian(self, month, day, year=None):
        if not year:
            year = self.year
        increase = 0
        adoptionYear = self.__adoption_year()

        if year > adoptionYear or self.gregPriorAdoption:
            increase = year // 100 - year // 400 - 2
        day += increase
        month_length = self.__month_length(month, year)
        if day > month_length:
            day = day % month_length
            if month + 1 <= 12:
                month += 1
            else:
                month = 1
                year += 1
        return [month, day, year]

    def __adoption_year(self):
        adoptionYear = self.adoptionYear
        if self.adoption != "exclusive":
            adoptionYear -= 1
        return adoptionYear

    def __month_length(self, month, year=None, calendar="Gregorian"):
        month_length = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year and self.isLeap(year, calendar):
            month_length[2] = 29
        return month_length[month]

    def isLeap(self, year, mode="Gregorian"):
        mode = mode.lower()
        if (year % 4 == 0 and (mode == "Julian".lower() or mode == "JulianGauss".lower())) or (
                year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True

        return False

    def GaussAlgorithm(self, year, mode="Julian"):
        if self.gregPriorAdoption is False and self.__adoption_year() >= year:
            mode = "Julian"
        mode = mode.lower()
        a = year % 19
        b = year % 4
        c = year % 7
        M = 15
        N = 6
        if mode == "Gregorian".lower():
            k = year // 100
            p = (13 + 8 * k) // 25
            q = k // 4
            M = (15 - p + k - q) % 30
            N = (4 + k - q) % 30
        d = (19 * a + M) % 30
        e = (2 * b + 4 * c + 6 * d + N) % 7
        if 22 + d + e <= 31:
            month = 3
            day = 22 + d + e
        else:
            month = 4
            day = d + e - 9

        if d == 28 and e == 6 and (11 * M - 11) % 30 < 19 and day == 25:
            day = 18
        elif d == 29 and e == 6 and day == 26:
            day = 19
        return [month, day]

    def AnonymousGregorian(self, year, mode="optimized"):
        if self.gregPriorAdoption is False and self.__adoption_year() >= year:
            return self.GaussAlgorithm(year)
        mode = mode.lower()
        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        if mode == "optimized":
            g = (8 * b + 13) // 25
        else:
            f = (b + 8) // 25
            g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        if mode == "optimized":
            m = (a + 11 * h + 19 * l) // 433
            n = (h + l - 7 * m + 90) // 25
            p = (h + l - 7 * m + 33 * n + 19) % 32
        else:
            m = (a + 11 * h + 22 * l) // 451
            n = (h + l - 7 * m + 114) // 31
            o = (h + l - 7 * m + 114) % 31
            p = o + 1
        month = n
        day = p
        return [month, day]


class EasterRelated:

    from datetime import date

    def __init__(self, year, month, day, mode="Julian"):
        self.mode = mode
        self.year = year
        self.month = month
        self.day = day
        self.EC = EasterCalculus(year)

    def datestamp(self, year, month, day):
        return f"{year}-{month}-{day}"

    def weekday(self, year, month, day, mode=None):
        if mode == "Julian" or (mode is None and self.mode == "Julian"):
            date = self.EC.JulianInGregorian(month, day, year)
            month = date[0]
            day = date[1]
            if date[2] is not None:
                year = date[2]
        return self.date(int(year), int(month), int(day)).isoweekday()
