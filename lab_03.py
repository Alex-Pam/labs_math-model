# function  = y0 * math.tan(x0) - y0 * y0 * math.cos(x0) * math.cos(x0)
import math
import decimal
from lab_02 import euler




def main():
    print("Уточненный метод", euler_02())


def euler_02():
    starting_point = float(input("a: "))
    end_point = float(input("b: "))
    function_value_of_reference_point = float(input("s: "))
    accuracy = float(input("e: "))
    num_of_round = get_count_after_dot(accuracy)

    y_check = 0
    n = 0
    while (n != 10000):
        n += 1
        x0 = starting_point
        y0 = function_value_of_reference_point
        h = (end_point - starting_point) / n
        y1_2 = y0 + h / 2 * func(x0, y0)
        yi = y0 + h * func(x0 + h / 2, y1_2)
        xi = x0
        for i in range(n):
            dy = h * func(xi, yi)
            xi += h
            y = dy + yi
            yi = y
        if abs(y - y_check) < accuracy:
            break
        y_check = y
    if n != 10000:
        print("Numbers of iteration: " + str(n) + "\n")
    else:
        print("It was not possible to achieve the specified accuracy")
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
