class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):

        total_second = self.__second + other.__second
        total_minute = self.__minute + other.__minute + total_second // 60
        total_hour = self.__hour + other.__hour + total_minute // 60

        total_second %= 60
        total_minute %= 60
        total_hour %= 24  

        return Time(total_hour, total_minute, total_second)

    def display(self):
        print(f"{self.__hour:}:{self.__minute:}:{self.__second:}")


t1 = Time(7, 23, 1)
t2 = Time(2, 59, 10)
t3 = t1 + t2  
t3.display()



