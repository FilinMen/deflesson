

#СЛОЖЕНИЕ
def add(a):
    for i in range(1, len(a)):
        a[0] += a[i]
    return  a[0]
#УМНОЖЕНИЕ
def mul(a):
    for i in range(1, len(a)):
        a[0] *= a[i]
    return a[0]
#РАЗНОСТЬ 
def sub(a):
    for i in range(1, len(a)):
        a[0] -= a[i]
    return a[0] 
#ДЕЛЕНИЕ
def div(a):
    for i in range(1, len(a)):
        a[0] /= a[i]
    return a[0]
#СТЕПЕНЬ
def deg(a):
    for i in range(1, len(a)):
        a[0] **= a[i]
    return a[0]
#ФАКТОРИАЛ
def fak(a):
    start = 1
    for i in range(1,a):
        start *= i
    return start
#УСЛОВИЯ
def main():
    print('ВВЕДИТЕ ВАШ ПРИМЕР:')
    example = input()
    a = []


    #СЛОЖЕНИЕ
    if '+' in example:
            print('addition')
            example.replace(' ', '') #УДАЛЕНИЕ ПРОБЕЛОВ
            spl_ex = example.split('+')# РАЗДЕЛЕНИЕ ПО ЗНАКУ
            list_ex = spl_ex
            for i in range(len(list_ex)):
                a.append(float(list_ex[i]))
            result = add(a)
    #УМНОЖИТЬ
    elif '*' in example and '**' not in example:
            print('multiply')
            example.replace(' ', '')
            spl_ex = example.split('*')
            list_ex = spl_ex
            for i in range(len(list_ex)):
                a.append(float(list_ex[i]))
            result = mul(a)
    #РАЗНОСТЬ
    elif '-' in example:
            print('subtract')
            example.replace(' ', '')
            spl_ex = example.split('-')
            list_ex = spl_ex
            for i in range(len(list_ex)):
                a.append(float(list_ex[i]))
            print(a[1])
            result = sub(a)
    #ДЕЛИТЬ
    elif '/' in example:
            print('subtract')
            example.replace(' ', '')
            spl_ex = example.split('/')
            list_ex = spl_ex
            for i in range(len(list_ex)):
                a.append(float(list_ex[i]))
            result = div(a)
    #СТЕПЕНЬ
    elif '**' in example or '^' in example:
            print('degree')
            example.replace(' ', '')
            if "**" in example:
                spl_ex = example.split('**')
            else:
                spl_ex = example.split('^')
            list_ex = spl_ex
            for i in range(len(list_ex)):
                a.append(float(list_ex[i]))
            result = deg(a)
    #ФАКТОРИАЛ
    elif '!' in example:
            print('factorial')
            example.replace(' ', '')
            spl_ex = example[1:]
            num_ex = spl_ex
            result = fak(int(num_ex))
    print(result)


if __name__ == '__main__':
    main()