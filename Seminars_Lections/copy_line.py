# Дополнить справочник возможностью копирования данных
# из одного файла в другой. Пользователь вводит номер строки,
# которую необходимо перенести из одного файла в другой.

from return_data_file import print_file

def copy_line(source_file, destination_file, line_number):
    try:
        with open(source_file, 'r') as source:
            lines = source.readlines()
            if 1 <= line_number <= len(lines):
                line_to_copy = lines[line_number - 1]

                with open(destination_file, 'a') as destination:
                    destination.write(line_to_copy)

                print(f"Строка {line_number} успешно скопирована из {source_file} в {destination_file}.")
            else:
                print(f"Недопустимый номер строки. В файле {source_file} всего {len(lines)} строк.")
    except FileNotFoundError:
        print("Ни один из файлов не найден.")

# Пример использования:
source_file_path = 'исходный_файл.txt'
destination_file_path = 'целевой_файл.txt'

user_line_number = int(input("Введите номер строки для копирования: "))

copy_line(source_file_path, destination_file_path, user_line_number)
