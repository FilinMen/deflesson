def sum(x):
    return x + x

def main():
    num = int(input("введите число"))
    num_sum = sum(num)
    print("сумма числа на себя же", num_sum)

if __name__ == '__main__':
    main()
