# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randrange
from re import findall

MIN_LETTERS = 4  # Минимальное количество букв в имени
MAX_LETTERS = 7  # Максимальное количество букв в имени
ALL_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'  # Алфавит
VOWEL_ALPHABET = 'aeiou'  # Только гласные буквы


def pseudo_names(n_min=MIN_LETTERS, n_max=MAX_LETTERS, ext='rnd'):
    """
    Генерируем псевдо-имя для файла
    :return: имя файла
    """
    ret = []
    while len(findall(f'[{VOWEL_ALPHABET}]', ''.join(ret))) < 1:  # До тех пор, пока не будет хотя бы одна гласная
        ret = [ALL_ALPHABET[randrange(len(ALL_ALPHABET))] for _ in range(randrange(n_min, n_max + 1))]
    return "".join(["".join(ret).capitalize(), '.', ext])
