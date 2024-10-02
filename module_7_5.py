import os
import time
os.chdir(r'C:\Users\synesis1\PycharmProjects\pythonProject1\.venv\module_5_hard')
directoty = os.getcwd()

for root, dirs, files in os.walk(directoty):
  for file in files:
    filepath = os.getcwd()
    filetime = os.stat(file).st_atime

    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.stat(file).st_size
    parent_dir = os.path.dirname(directoty)

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')