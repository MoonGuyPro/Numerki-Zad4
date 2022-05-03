import Newton_Cotes
import numpy as np
from sympy import *
import Gauss_Hermit


def menu(funct):
    print("Wybierz metode całkowania numerycznego: ")
    print("1. Newtona-Cotesa opartą na trzech węzłach")
    print("2. Gaussa-Hermite'a")
    method = input()
    if method == "1":
        print("Podaj przedział, od: ")
        interval_0 = input()
        print("do: ")
        interval_n = input()
        print("Podaj dokładność: ")
        epsilon = input()
        result = Newton_Cotes.Simpson_method(float(epsilon), float(interval_0), float(interval_n), funct)
        print("Całka wynosi: " + str(result))
        plus, minus = Newton_Cotes.function_limit(funct)
        print("Granica funkcji w -oo wynosi: " + str(minus) + ", a w +oo: " + str(plus))
    elif method == "2":
        print("Podaj ilość wezłów: [2,3,4,5]")
        n = input()
        result = Gauss_Hermit.Gaus_Hermit_method(funct, int(n))
        print("Całka dla " + str(n) + " węzłów wynosi: " + str(result))


def main():
    check = True
    while (check):
        print("Wybierz funkcje: ")
        print("0. Wyjście")
        print("1. Wybrana")
        print("2. cos(2x)")
        print("3. x**2+3")
        print("4. log(x+3) * 4")
        choice = input()
        if choice == "0":
            check = False
        elif choice == "1":
            print("Podaj funkcje: ")
            funct = input()
            menu(funct)
        elif choice == "2":
            funct = "np.cos(2*x)"
            menu(funct)
        elif choice == "3":
            funct = "x**2+3"
            menu(funct)
        elif choice == "4":
            funct = "np.log(x+3) * 4"
            menu(funct)
        else:
            print("Zły numer!")


if __name__ == '__main__':
    main()
