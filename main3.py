#факториал
def fak(a):
    start = 1
    for i in range(1,a):
        start *= i
    return start

print('ВВЕДИТЕ ВАШ ПРИМЕР:')
example = input()
list_num = []


if '!' in example:
    print('factorial')
    example.replace(' ', '')
    spl_ex = example[1:]
    num_ex = spl_ex
    result = fak(int(num_ex))
print(result)