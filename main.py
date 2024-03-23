def main(stroke):

    word_size = len(stroke)
    try:
        if word_size < 3:
            raise ValueError
    except ValueError:
        print("Строка не является математической операцией, пожалуйста повторите попытку, для ввода используйте два целых числа и один из математических операторов: '/' - деление, '*' - умножение, '+' - сложение, '-' - вычитание!")
        quit()

    if "+" in stroke:
        symb = stroke[stroke.find("+")]
        try:
            if stroke.count("+") > 1:
                raise ValueError
        except:
            print("Строка не является математической операцией, пожалуйста повторите попытку, для ввода используйте два целых числа и один из математических операторов: '/' - деление, '*' - умножение, '+' - сложение, '-' - вычитание!")
            quit()
        stroke = stroke.split(symb, 1)

    elif "-" in stroke:
        symb = stroke[stroke.find("-")]
        try:
            if stroke.count("-") > 1:
                raise ValueError
        except:
            print("Строка не является математической операцией, пожалуйста повторите попытку, для ввода используйте два целых числа и один из математических операторов: '/' - деление, '*' - умножение, '+' - сложение, '-' - вычитание!")
            quit()
        stroke = stroke.split(symb, 1)

    elif "/" in stroke:
        symb= stroke[stroke.find("/")]
        try:
            if stroke.count("/") > 1:
                raise ValueError
        except:
            print("Строка не является математической операцией, пожалуйста повторите попытку, для ввода используйте два целых числа и один из математических операторов: '/' - деление, '*' - умножение, '+' - сложение, '-' - вычитание!")
            quit()
        stroke = stroke.split(symb, 1)

    elif "*" in stroke:
        symb= stroke[stroke.find("*")]
        try:
            if stroke.count("*") > 1:
                raise ValueError
        except:
            print("Строка не является математической операцией, пожалуйста повторите попытку, для ввода используйте два целых числа и один из математических операторов: '/' - деление, '*' - умножение, '+' - сложение, '-' - вычитание!")
            quit()
        stroke = stroke.split(symb, 1)

    try:
        a = int(stroke[0])
        b = int(stroke[1])
    except ValueError:
        print("Строка не является математической операцией, пожалуйста повторите попытку, для ввода используйте два целых числа и один из математических операторов: '/' - деление, '*' - умножение, '+' - сложение, '-' - вычитание!")
        quit()


    try:
        if "+" == symb and 1 <= a <= 10 and 1 <= b <= 10:
            return a + b

        elif "-" == symb and 1 <= a <= 10 and 1 <= b <= 10:
            return a - b

        elif "/" in symb and 1 <= a <= 10 and 1 <= b <= 10:
            return a // b

        elif "*" in symb and 1 <= a <= 10 and 1 <= b <= 10:
            return a * b
        else:
            raise ValueError
    except ValueError:
        print("Для ввода используйте, пожалуйста, числа от 1 до 10!")
        quit()




stroke = input("Введите математическую операцию: ")
print(main(stroke))