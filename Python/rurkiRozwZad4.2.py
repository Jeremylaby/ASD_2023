import numpy as np
import matplotlib.pyplot as pyp
from scipy.integrate import quad


def e_function(i, x, dx):
    if x <= i*dx and x > (i-1)*dx:
        return x/dx-(i-1)
    elif (x > i*dx and x < (i+1)*dx):
        return 1-x/dx+i
    else:
        return 0


def e_function_derective(i, x, dx):
    if x <= (i - 1) * dx or x >= (i + 1) * dx:
        return 0
    elif x <= i * dx:
        return 1 / dx
    else:
        return -1 / dx


def B_function(w, v, dx):
    # w(2)v(2)+Cw'v'-Cwv=Csin(x)v
    if abs(w-v) > 1:
        return 0
    if w-v == 0:
        # Ogólnie ograniczyłem przedziały bo dla większej ilości przedziałów wywalało błąd a itak dla reszty mamy 0
        integral_A = quad(lambda x: e_function_derective(
            w, x, dx) * e_function_derective(v, x, dx), max(0, (w-1)*dx), min(2, (w+1)*dx))[0]
        integral_B = quad(lambda x: e_function(w, x, dx) *
                          e_function(v, x, dx), max(0, (w-1)*dx), min(2, (w+1)*dx))[0]
        return integral_A - integral_B + e_function(v, 2, dx) * e_function(w, 2, dx)
    else:
        integral_A = quad(lambda x: e_function_derective(
            w, x, dx) * e_function_derective(v, x, dx), min(w, v)*dx, max(w, v)*dx)[0]
        integral_B = quad(lambda x: e_function(w, x, dx) *
                          e_function(v, x, dx), max(0, (w-1)*dx), min(2, (w+1)*dx))[0]
        return integral_A - integral_B + e_function(v, 2, dx) * e_function(w, 2, dx)


def L_function(i):
    # B(u,v)=L(v)
    # B(w+u~,v)=L(v)
    # B(w,v)=L(v)-B(u~,v)
    # B(w,v)=L(v)-B(2u0,v)
    # B(w,v)=L(v)-2B(u0,v)
    Lei = quad(lambda x: 5*np.sin(np.pi*2*x) * e_function(i, x, dx),
               max(0, (i-1)*dx), min(2, (i+1)*dx))[0]
    Buei = B_function(0, i, dx)
    return Lei - Buei


if __name__ == '__main__':
    n = int(input("Podaj liczbę przedziałów: "))
    dx = 2 / n
    # tworzenie macierzy
    B_Matrix = np.zeros((n, n))
    L_Matrix = np.zeros(n)

    # Obliczenia macierzy B i macierzy L
    for i in range(n):
        for j in range(n):
            B_Matrix[i, j] = B_function(
                j+1, i+1, dx)
        L_Matrix[i] = L_function(
            i+1)
    # Wyliczmy u1 u2 itd a raczej samo sie wylicza:)
    Ui_Matrix = np.linalg.solve(B_Matrix, L_Matrix)
    # w(0)=2
    Ui_Matrix = np.concatenate(([1], Ui_Matrix))
    pyp.plot(np.linspace(0, 2, n + 1), Ui_Matrix)
    pyp.show()
