import numpy as np
from sympy import *


def f_x(x, function):
    f = eval(function)
    return f


def Simpson_method(epsilon, a, b, funct):
    result = 0.0
    # old_result = 0.0
    diff = 10
    iteration = 1
    n = 3

    while diff > epsilon:
        old_result = result
        h = (b - a) / (n - 1)
        x = np.linspace(a, b, n)
        f = f_x(x, funct)
        # f = np.sin(x)

        result = (h / 3) * (f[0] + 2 * sum(f[:n - 2:2]) + 4 * sum(f[1:n - 1:2]) + f[n - 1])
        n += 1
        iteration += 1
        diff = abs(result - old_result)
    print("Liczba iteracji: " + str(iteration))
    return result


def function_limit(funct):
    x = symbols('x')
    if funct[0:2] == "np":
        expr = funct[3:]
    else:
        expr = funct
    limit_funct_plus = limit(expr, x, oo, '+')
    limit_funct_minus = limit(expr, x, oo, '-')
    return limit_funct_plus, limit_funct_minus
