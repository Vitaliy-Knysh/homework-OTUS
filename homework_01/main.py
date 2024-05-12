"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [*map(lambda x: x ** 2, numbers)]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"  # простое число


def is_prime(number):
    if number % 1 == 0 and number > 1:
        for i in range(2, number - 1):
            if number % i == 0:
                return False
        return True
    else: return False


def filter_numbers(numbers, fltr):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if fltr == ODD:
        return [*filter(lambda x: x % 2 == 1, numbers)]
    elif fltr == EVEN:
        return [*filter(lambda x: x % 2 == 0, numbers)]
    elif fltr == PRIME:
        return [*filter(is_prime, numbers)]
