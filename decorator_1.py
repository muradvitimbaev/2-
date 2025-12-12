# Декоратор логирования
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула: {result}")
        return result

    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def divide(a, b):
    return "Ошибка! Деление на 0" if b == 0 else a / b


@logger
def greet(name):
    return f'Здравствуйте {name}!'

print(add(2, 3))
print(divide(4, 1))
print(greet('Мурад'))
