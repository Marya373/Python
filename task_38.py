# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска о
#    определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# ДЗ
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных


import os
from time import sleep


def main():
    FILENAME = '/Users/maryafaivisovich/Desktop/Python/Python_практика/Python/Python-2/data.txt'
    while True:
        os.system('clear')
        print('ТЕЛЕФОННЫЙ СПРАВОЧНИК \n'
              ' "1" для выведения всех записей \n'
              ' "2" для добавления нового контакта \n'
              ' "3" для поиска информации по контакту \n'
              ' "4" для изменения информации по контакту \n'
              ' "5" для удаления информации по контакту \n'
              ' "0" для выхода')
        try:
            mode = int(input('Выберите режим: '))
            if mode == 1:
                show_data(FILENAME)
                sleep(3)
            elif mode == 2:
                new_data(FILENAME)
                sleep(1)
            elif mode == 3:
                search_data(FILENAME)
                sleep(3)
            elif mode == 4:
                edit_data(FILENAME)
                sleep(2)
            elif mode == 5:
                delete_data(FILENAME)
                sleep(2)
            elif mode == 0:
                print('Заново')
                break
        except ValueError:
            print('Такого пункта нет!')
            sleep(1)


if __name__ == '__main__':
    main()

def show_data(FILENAME):
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('Файл не найден')


def new_data(FILENAME):
    with open(FILENAME, 'a+', encoding='utf-8') as file:
        fio = input('Введите ФИО: ')
        phone = input('Введите телефон: ')
        file.write(f'{fio} | {phone}\n')
        print('Контакт добавлен')


def rewrited(strings, data, FILENAME):
    fio = input('Введите изменения в ФИО: ')
    phone = input('Введите изменения в телефон: ')
    with open(FILENAME, 'w', encoding='utf-8') as f2:
        [f2.write(f'{fio} | {phone}\n') if line == strings else f2.write(
            f'{data[line]}\n') for line in range(len(data)-1)]
        print('Данные изменены')


def deleted(strings, data, FILENAME):
    with open(FILENAME, 'w', encoding='utf-8') as f2:
        [f2.write(f'{data[line]}\n') if line !=
         strings else '' for line in range(len(data)-1)]
        print('Данные удалены')


def search_data(FILENAME):
    with open(FILENAME, 'r', encoding='utf-8') as f1:
        search = input('Введите ФИО или номер телефона для поиска: ')
        text = f1.read().split('\n')
        result = [(text.index(book), book)
                  for book in text if search.lower() in book.lower()]
        if len(result) >= 1:
            print('Найдено: ')
            [print(f'{result.index(book)+1}) {str(book[1])}')
             for book in result]
            return ([line[0] for line in result], text)
        else:
            print('Не найдено')
            return ([], text)


def edit_data(FILENAME):
    data = search_data(FILENAME)
    if len(data[0]) == 1:
        rewrited(data[0][0], data[1], FILENAME)
    elif len(data[0]) > 1:
        change = int(
            input('Номер желаемой для изменения записи: '))
        while change not in [i for i in range(1, len(data[0])+1)]:
            print('Номер отсутствует')
            change = int(
                input('Номер желаемой для изменения записи: '))
        rewrited(int(data[0][change-1]), data[1], FILENAME)


def delete_data(FILENAME):
    data = search_data(FILENAME)
    if len(data[0]) == 1:
        deleted(data[0][0], data[1], FILENAME)
    elif len(data[0]) > 1:
        change = int(
            input('Номер записи для удаления: '))
        while change not in [i for i in range(1, len(data[0])+1)]:
            print('Номер отсутствует')
            change = int(
                input('Номер для удаления записи: '))
        deleted(int(data[0][change-1]), data[1], FILENAME)

    
