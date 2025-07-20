class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
    
    def __add__(self, other):
        return Date(self.day + other, self.month, self.year)
    


if __name__ == "__main__":
    d1 = Date(6, 7, 24)
    d2 = Date(4, 3, 6)
    print(d1)
    print(d2)
    print(d1+10)
