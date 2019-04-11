# Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
# В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке,
# из которой запущен данный код. Затем создайте вторую функцию, удаляющую эти папки.
# Проверьте работу функций в этом же модуле.


import os


def create_folder():
    for folder in range(1, 10):
        path_folder = os.path.join(os.getcwd(), '{}_{}'.format('dir', folder))
        os.mkdir(path_folder)
    print('Создали каталоги')

create_folder()


def del_folder():
    for folder in range(1, 10):
        path_folder = os.path.join(os.getcwd(), '{}_{}'.format('dir', folder))
        os.rmdir(path_folder)
    print('Удалили каталоги')

del_folder()