def infinity_sequence(start=1):
    while True:
        yield start
        start += 1


numbers = infinity_sequence()

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print('#' * 10)

#-----------------------------------------------------------------------------

def f():
    print('Initial...')
    yield 'one'
    print('Continue...')
    yield 'two'
    print('Final...')
    # yield 'three'

i = f()
print(next(i))
print(next(i))
print(next(i, 'А всё, генерация закончилась!'))

#-----------------------------------------------------------------------------

def iterate(x0, m):
    x = x0
    while True:
        yield x
        x *= m

for n in iterate(1, 1.2):
    print(n)
    if n > 3:
        break

if __name__ == '__main__':
    # тестируем на коленке генератор
    i = iterate(1, 1.2)
    print('Тут ASSERRTы начинаются')
    assert next(i) == 1
    assert next(i) == 1.2
    assert next(i) == 1.44
    assert next(i) == 1.728
    print('Тут ASSERRTы заканчиваются')
