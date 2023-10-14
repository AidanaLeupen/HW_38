
from os.path import exists
from csv import DictReader, DictWriter
def get_info():
    info = []
    first_name = 'Ivan'
    last_name = 'Ivanov'
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = 12345678901  # int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info
def create_file():
    with open('phone.csv', 'w', encoding='utf-8') as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()

def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8') as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(res)

def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book

def record_info():
    lst = get_info()
    write_file(lst)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            print(*read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
            else:
                phone_book = read_file('phone.csv')
                print(*phone_book)
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 'e':
            last_name = input('Введите фамилию для изменения: ')
            new_phone_number = input('Введите новый номер: ')
            if edit_record(res, last_name, new_phone_number):
                print('Данные успешно изменены.')
                with open('phone.csv', 'w', encoding='utf-8') as f_n:
                    f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
                    f_n_writer.writeheader()
                    f_n_writer.writerows(res)
            else:
                print('Контакт не найден.')

        elif command == 'd':
            last_name = input('Введите фамилию для удаления: ')
            if delete_record(res, last_name):
                print('Контакт успешно удален.')
                with open('phone.csv', 'w', encoding='utf-8') as f_n:
                    f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
                    f_n_writer.writeheader()
                    f_n_writer.writerows(res)
            else:
                print('Контакт не найден.')