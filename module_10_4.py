from threading import Thread
import queue
from random import randint
import time


class Table:

    def __init__(self, number):
        self.guest = None
        self.number = number


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        new_guest = self.queue.get()
                        table.guest = new_guest
                        new_guest.start()
                        print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
