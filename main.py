#module - выполняет функцию сложения числа на себя
#module1 -  выполняет функцию добовления слова в список 
#module2 -  выполняет функцию (колличество букв в слове)

import new_file.module as m1
import module1 as m2
import module2 as m3
import calcul as cal

def main():
    user_choise = int(input("CHOISE 1 if you want adding a number on yourself \n CHOISE 2 if you want adding a word to the list \n CHOISE 3 if you want find out the number of letters in a word \n CHOISE 4 if you want use a calculator"))
    if user_choise == 1:
        m1.main()
    elif user_choise == 2:
        m2.main()
    elif user_choise == 3:
        m3.main()
    elif user_choise == 4:
        cal.main()
    else:
        print("!!!!ВЫ ВВЕЛИ НЕВЕРНОЕ ЧИСЛО!!!!")
        main()


if __name__ == "__main__":
    main()