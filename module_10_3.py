import threading
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            dep = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += dep
            print(f'Пополнение {i + 1}: {dep}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            cash = randint(50, 500)
            print(f'Запрос на {cash}')
            if self.balance >= cash:
                self.balance -= cash
                print(f'Снятие {i + 1}: {cash}. Баланс: {self.balance}')
                sleep(0.001)

            else:
                print(f'Запрос отклонён, недостаточно средств.')
                self.lock.acquire()



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
