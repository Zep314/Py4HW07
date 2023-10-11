"""
Init-файл для пакета с моими модулями
"""
from my_file_utils.rename import group_rename
from my_file_utils.create_file import create_file
from my_file_utils.pseudo_names import pseudo_names

# Эти функции будем "экспортировать" для внешней работы
__all__ = ['group_rename', 'create_file', 'pseudo_names']
