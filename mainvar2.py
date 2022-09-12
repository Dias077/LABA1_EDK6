def main():
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        x = int(input('Введите X: '))

        if x > 6:
            y = (6 * (x * x)) - (a * b) / 2 * (x * x)
        else:
            y = 4 * (x + (a * a) + (b * b))

        print("y = %.1f" % y)
    except ValueError:
        print("Ошибка! Не верные данные")
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль")

if __name__ == '__main__':
    main()
