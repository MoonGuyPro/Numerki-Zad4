from numpy.polynomial.hermite import hermgauss
import Newton_Cotes


def coefficients(n):
    A_i, x_i = hermgauss(n)
    return A_i, x_i


def Gaus_Hermit_method(funct, n):
    A_i, x_i = coefficients(n)
    result = 0.0
    for i in range(n):
        result += x_i[i] * Newton_Cotes.f_x(A_i[i], funct)
    return result
