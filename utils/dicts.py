def get_val(collection, key, default='git'):
    """
    Извлекает из словаря значение по ключу, если ключ существует.
    Если ключа не существует, возвращает значение default.
    :param collection: исходный словарь.
    :param key: ключ.
    :param default: значение по-умолчанию.
    :return: значение ключа или значение по-умолчанию
    """

    if key in collection:
        return collection[key]
    return default
