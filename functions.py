def show_data(FILENAME):
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('Файл справочника не существует')


def new_data(FILENAME):
    with open(FILENAME, 'a+', encoding='utf-8') as file:
        fio = input('Введите ФИО: ')
        phone = input('Введите телефон: ')
        file.write(f'{fio} | {phone}\n')
        print('Контакт успешно добавлен в справочник')


def rewrited(strings, data, FILENAME):
    fio = input('Введите изменения в ФИО: ')
    phone = input('Введите измененный телефон: ')
    with open(FILENAME, 'w', encoding='utf-8') as f2:
        [f2.write(f'{fio} | {phone}\n') if line == strings else f2.write(
            f'{data[line]}\n') for line in range(len(data)-1)]
        print('Данные успешно изменены')


def deleted(strings, data, FILENAME):
    with open(FILENAME, 'w', encoding='utf-8') as f2:
        [f2.write(f'{data[line]}\n') if line !=
         strings else '' for line in range(len(data)-1)]
        print('Данные успешно удалены')


def search_data(FILENAME):
    with open(FILENAME, 'r', encoding='utf-8') as f1:
        search = input('Введите ФИО или номер телефона для выбора: ')
        text = f1.read().split('\n')
        result = [(text.index(book), book)
                  for book in text if search.lower() in book.lower()]
        if len(result) >= 1:
            print('Найдены записи: ')
            [print(f'{result.index(book)+1}) {str(book[1])}')
             for book in result]
            return ([line[0] for line in result], text)
        else:
            print('Значение в справочнике не найдено')
            return ([], text)


def edit_data(FILENAME):
    data = search_data(FILENAME)
    if len(data[0]) == 1:
        rewrited(data[0][0], data[1], FILENAME)
    elif len(data[0]) > 1:
        change = int(
            input('Введите порядковый номер желаемой для изменения записи: '))
        while change not in [i for i in range(1, len(data[0])+1)]:
            print('Введеный номер отсутствует в списке вариантов')
            change = int(
                input('Введите порядковый номер желаемой для изменения записи: '))
        rewrited(int(data[0][change-1]), data[1], FILENAME)


def delete_data(FILENAME):
    data = search_data(FILENAME)
    if len(data[0]) == 1:
        deleted(data[0][0], data[1], FILENAME)
    elif len(data[0]) > 1:
        change = int(
            input('Введите порядковый номер желаемой для удаления записи: '))
        while change not in [i for i in range(1, len(data[0])+1)]:
            print('Введеный номер отсутствует в списке вариантов')
            change = int(
                input('Введите порядковый номер желаемой для удаления записи: '))
        deleted(int(data[0][change-1]), data[1], FILENAME)
