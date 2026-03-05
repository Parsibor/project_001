class ValidationError(Exception):
    print('Ass')

def person_age(age):
    if age < 0:
        raise ValidationError('Возраст не может быть отрицательным')
    elif age > 120:
        raise ValidationError('Возраст не может быть больше 120')
    return True

try:
    person_age(150)
except ValidationError as e:
    print(e)