# Создайте модуль. В нем создайте функцию, которая принимает список и
# возвращает из него случайный элемент. Если список пустой, функция
# должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную.
#     Или возьмите этот: [1, 2, 3, 4]

import random


def random_list(number_list, default=None):
    if number_list:
        for item in number_list:
            return random.choice(number_list)
    else:
        return default



list = [1, 2, 3, 4]
print(random_list(list))

list2 = []
print(random_list(list2))