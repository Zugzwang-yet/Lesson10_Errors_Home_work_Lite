class NegativeNumberError(Exception):
    def __init__(self, number: int|float, message='Отрицательное число'):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.number}"

def check_positive_number(number: int|float):
        if number < 0:
            raise NegativeNumberError(number)
    
        

check_positive_number(10)
check_positive_number(-10)