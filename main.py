
import my_file_utils as mfu

if __name__ == '__main__':

    # Задание №2 - генерировать случайные имена файлов
    with open('rnd_names.txt', 'w') as f:
        for _ in range(10):
            f.write(mfu.pseudo_names()+'\n')

    # Задание 4 - 6 - Функции создания файлов
    mfu.create_file('/home/user/Work/Python/dz3/Py3HW07/test_create1', {'qqq': 5,
                                                                        'www': 10,
                                                                        'eee': 7,
                                                                        'rrr': 12,
                                                                        })
    # Домашнее задание - функция переименования файлов
    mfu.group_rename('/home/user/Work/Python/dz3/Py3HW07/ttest', 'ffile', 3, 'zzz', 'xxx', [3, 6])
