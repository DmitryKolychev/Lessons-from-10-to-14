from threading import Thread
from time import sleep
class Knight:

    def __init__(self, name, power):
        self.name = name
        self.power = power
        # super().__init__()


    def run(self):
        print(f'{self.name}, на нас напали!')
        warriors = 100
        day = 0
        while warriors > 0:
            sleep(1)
            day += 1
            warriors = (warriors - self.power if (warriors - self.power) >= 0 else 0)
            print(f'{self.name} сражается {day} дней, осталось {warriors} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
third_knight = Knight("Sir Robin Good", 15)

first_knight_flow = Thread(target=first_knight.run)
second_knight_flow = Thread(target=second_knight.run)
third_knight_flow = Thread(target=third_knight.run)

first_knight_flow.start()
second_knight_flow.start()
third_knight_flow.start()

first_knight_flow.join()
second_knight_flow.join()
third_knight_flow.join()
print('Все битвы закончились!')