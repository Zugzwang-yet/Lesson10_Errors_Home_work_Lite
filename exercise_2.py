class KeyNotFoundError(Exception):
    pass

class UserInputError(Exception):
    pass

def validate_user_input(data):
    try:   
        if not isinstance(data, dict):
            raise UserInputError('Введенные данные должны быть словарем')

        if 'name' not in data:
            raise KeyNotFoundError('Отсутствует обязательный ключ: name')
            
        if not isinstance(data['name'], str):
            raise TypeError('Неподходящий тип данных для значения ключа "name", ожидался str, получен: ', type(data['name']))
        
        if 'age' not in data:
            raise KeyNotFoundError('Отсутствует обязательный ключ: age')
        
        if not isinstance(data['age'], int):
            raise TypeError('Неподходящий тип данных для значения ключа "age", ожидался int, получен: ', type(data['age']))
                
        if not 0 < data['age'] <= 120:
            raise ValueError('Указан некорректный возраст')
                
    except (UserInputError, KeyNotFoundError, ValueError, ) as e:
        print(f'Ошибка типа: {e}')

    except TypeError as t:
        raise ValueError('Ошибка ввода данных') from t
    
    else:
        print(f'Входные данные пользователя являются корректными: {data}')

data1 = {"name": "Alice", "age": 30}
data2 = {"age": 30}
data3 = {"name": "Alice", "age": 130}
data4 = 'Hello, world!'

validate_user_input(data1)
validate_user_input(data2)
validate_user_input(data3)
validate_user_input(data4)





