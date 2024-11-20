import inspect


def introspection_info(obj):
    data = {}

    data['Тип объекта'] = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    data['Атрибуты объекта'] = attributes

    methods = [method for method in dir(obj) if
               callable(getattr(obj, method)) and not method.startswith("__")]
    data['Методы объекта'] = methods

    module = inspect.getmodule(obj)
    data['Модуль'] = module.__name__ if module else "Объект встроенный или не принадлежит модулю"

    data['Документация объекта'] = obj.__doc__ if hasattr(obj, '__doc__') else "Документация отсутствует"

    return data


number_info = introspection_info(42)
print(number_info)
