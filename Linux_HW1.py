## Написать функцию которой передаются в качестве параметров команда и текст.
# функция должна возвращать True, если команда выполнена успешно и текст найден
# в ее выводе и False в обратном случае.
# Передаваться должна только одна строка, разбиение вывода не нужно.

import subprocess

def find_text_command(command, text):
    try:
        # Выполнение команды и получение вывода
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

        # Поиск текста в выводе команды
        if text in result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        # Обработка ошибки при выполнении команды
        return False

# Пример использования функции
# Запрос ввода текста от пользователя
text_to_find = input("Введите текст для поиска: ")

# Команда, которую нужно выполнить
command = "ls -l /"

# Вызов функции с командой и введенным текстом для поиска
result = find_text_command(command, text_to_find)

# Вывод
if result:
    print("True (Текст найден в выводе команды)")
else:
    print("False (Текст не найден в выводе команды или произошла ошибка)")