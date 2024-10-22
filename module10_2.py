from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super(). __init__()
        self.name = name
        self.power = power

    def run(self):
        emenies = 100
        days = 0
        print(f"{self.name} на нас напали!")
        for i in range (emenies):
            if emenies > 0:
                emenies -= self.power
                days += 1
                sleep(1)
                print(f"{self.name} сражается  {days}  осталось {emenies} воинов.")
                if emenies <= 0:
                    print (f"{self.name} одержал победу спустя {days} дней(дня)!")

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

# Вывод строки об окончании сражения
first_knight.join()
second_knight.join()

print("Battles are over")








