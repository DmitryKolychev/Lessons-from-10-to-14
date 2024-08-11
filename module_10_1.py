import os
from time import sleep
from datetime import datetime
from threading import Thread

def check_and_delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)
    #     print(f"Файл '{file_name}' успешно удален.")
    # else:
    #     print(f"Файл '{file_name}' не найден.")

def write_words(word_count, file_name):
    time_start = datetime.now()
    word = "Какое-то слово № "
    for i in range(word_count):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'{word}{i+1} \n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    time_end = datetime.now()
    # print(f'Работа функции {time_end - time_start}')

time_start = datetime.now()
f1 = (10, 'example1.txt')
check_and_delete_file(f1[1])
write_words(f1[0], f1[1])
# with open(f1[1], 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

f2 = (30, 'example2.txt')
check_and_delete_file(f2[1])
write_words(f2[0], f2[1])
# with open(f2[1], 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

f3 = (200, 'example3.txt')
check_and_delete_file(f3[1])
write_words(f3[0], f3[1])
# with open(f3[1], 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

f4 = (100, 'example4.txt')
check_and_delete_file(f4[1])
write_words(f4[0], f4[1])
# with open(f4[1], 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

time_end = datetime.now()
print(f'\nОбщее время работы функций {time_end - time_start}\n')

f5 = (10, 'example5.txt')
f6 = (30, 'example6.txt')
f7 = (200, 'example7.txt')
f8 = (100, 'example8.txt')

time_start = datetime.now()
f5_flow = Thread(target=write_words, args=f5)
f6_flow = Thread(target=write_words, args=f6)
f7_flow = Thread(target=write_words, args=f7)
f8_flow = Thread(target=write_words, args=f8)

f5_flow.start()
f6_flow.start()
f7_flow.start()
f8_flow.start()

f5_flow.join()
f6_flow.join()
f7_flow.join()
f8_flow.join()

time_end = datetime.now()
print(f'\nРабота потоков {time_end - time_start}\n')