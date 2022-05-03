import Newton_Cotes
import numpy as np
from sympy import *


def menu(funct):
    print("Wybierz metode całkowania numerycznego: ")
    print("1. Newtona-Cotesa opartą na trzech węzłach")
    print("2. Gaussa -Hermite'a")
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
        print()


def main():
    check = True
    while (check):
        print("Wybierz funkcje: ")
        print("0. Wyjście")
        print("1. sin(x)")
        print("2. cos(2x)")
        print("3. ")
        print("4. ")
        print("5. ")
        choice = input()
        if choice == "0":
            check = False
        elif choice == "1":
            funct = "np.sin(x)"
            menu(funct)
        elif choice == "2":
            funct = "np.cos(2*x)"
            menu(funct)

        elif choice == "3":
            funct = ""

        elif choice == "4":
            funct = ""
        else:
            print("Zły numer!")


if __name__ == '__main__':
    main()
