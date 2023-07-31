class CustomException(Exception):
    pass


class LevelError(CustomException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'В доступе отказано. Ваш уровень ниже {self.value}'


class AccessError(CustomException):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f'Пользователя с id: {self.user_id} и с именем: {self.name} в базе не найдено'

