import os
import time

directory = "/path/to/directory"

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file},'
              f' Путь: {filepath},'
              f' Размер: {filesize} байт,'
              f' Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')


# Не забудьте заменить "/path/to/directory" на путь к каталогу, который вы хотите обойти.
# Этот код позволит вывести информацию о файлах в указанной директории и всех её поддиректориях.
