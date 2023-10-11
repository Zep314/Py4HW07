import os


def group_rename(path, file_name, nnums, in_ext, out_ext, name_range):
    """
    Функция группового переименования файлов
    :param path: Путь к папке, в которой осуществляется переименование файлов
    :param file_name: желаемое конечное имя файла
    :param nnums: количество цифр в порядковом номере
    :param in_ext: расширение исходных файлов
    :param out_ext: расширение конечных файлов
    :param name_range: диапазон символов исходного файла, которые будут сохранены в конечном имени
    :return:

    Пример: group_rename('/path/to/directory', 'great', 3, ,'zzz', 'xxx', [3, 6])
    Исходное имя файла: qwerty.zzz
    Конечное имя файла: rtygreat001.xxx
    """
    files = list(os.walk(path))[-1][-1]  # список всех файлов в указанном каталоге
    files = [f for f in files if "." + in_ext in f]  # фильтруем список, чтобы остались файлы с нужным расширением

    # делаем список новых имен файлов
    new_files = [(files[i].split('.')[0][name_range[0]:name_range[1]] if range else '') +
                 file_name +
                 f"{i:0{nnums}}" +
                 "." + out_ext
                 for i in range(len(files))]

    try:  # Переименование файлов с обработкой ошибок
        list(map(lambda x, y: os.rename(f'{path}{os.sep}{x}', f'{path}{os.sep}{y}'), files, new_files))
    except (OSError, IOError):
        print("Ошибка при работе с файлами!")
