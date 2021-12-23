# function  = y0 * math.tan(x0) - y0 * y0 * math.cos(x0) * math.cos(x0)
import math
import decimal


def main():
    print("Метода Рунге-Кутта", foo())


def foo():
    starting_point = float(input("a: "))
    end_point = float(input("b: "))
    function_value_of_reference_point = float(input("s: "))
    accuracy = float(input("e: "))
    num_of_round = get_count_after_dot(accuracy)

    n = 1
    h = (end_point - starting_point) / n
    x = starting_point
    y = function_value_of_reference_point
    while (pow(h, 4) >= accuracy):
        n += 1
        h = (end_point - starting_point) / n
        for i in range(n):
            k1 = h * func(x, y)
            k2 = h * func(x + h / 2, y + k1 / 2)
            k3 = h * func(x + h, y + k2 / 2)
            k4 = h * func(x + h, y + k3)
            dy = (k1 + 2 * k2 + 2 * k3 + k4) / 6
            y += dy
            x += h
        print("Numbers of iteration: " + str(n) + "\n")
    return round(y, num_of_round)


def func(x, y):
    return y * math.tan(y) - y ** 2 * math.cos(x)


def get_count_after_dot(num):
    s = str(num)
    if '.' in s:
        return abs(decimal.Decimal(s.rstrip('0')).as_tuple().exponent)
    else:
        return 0


main()
