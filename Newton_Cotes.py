import numpy as np


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
        print(iteration)
        iteration += 1
        print(result)
        diff = abs(result - old_result)

    return result
