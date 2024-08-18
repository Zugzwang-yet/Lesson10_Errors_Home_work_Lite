def convert_to_int(value: str):
    try:
        if not isinstance(value, (str, int, float)):
            raise TypeError("Аргумент должен быть строкой, целым или вещественным числом")
        
        value_int = int(value)
   
    except ValueError:
        print('Ошибка: невозможно преобразовать строку в число')
    except TypeError as e:
        print(f'Ошибка типа: {e}') 
    else:
        print(f'Результат преобразования: {value_int}', type(value_int))
    finally:
        print('Попытка преобразования завершена')

convert_to_int([1, 2, 3])
convert_to_int('123')
convert_to_int('abc')

