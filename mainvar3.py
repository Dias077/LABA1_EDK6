import math
try:
    a = float(input("Введите A="))
    b = float(input("Введите B="))
    x = float(input("Введите X="))
    try:
        if x > 6:
            y = (6 * (x * x)) - (a * b) / 2 * (x * x)
        else:
            y = 4 * (x + (a * a) + (b * b))
        print("y = %.1f" % y)
    except:
        print("Нет решения!")
except:
    print("Неверные входные данные!")
input("Нажмите Enter для выхода")