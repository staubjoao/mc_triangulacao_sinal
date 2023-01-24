# -*- coding: utf-8 -*-
# Sergio Alvarez RA115735

import numpy as np
from matplotlib import pyplot as plt
# Casos teste
# p1 p2 p3 p4 p5
# -48.4 -50.6 -32.2 -47.4 -46.3
# -46.9 -46.4 -41.2 -45.8 -48.7


def distanciaRadial(coordenadas, pk0, lk, pk):
    dk = []
    for i in range(len(coordenadas)):
        dk.append(10 ** ((pk0[i]-pk[i]) / (10 * lk[i])))

    return dk

# xR, yR, zR = posição receptor (valor conhecido)
# dk = distancia radial receptor (valor conhecido)
# x, y, z = posição emissor (valor desconhecido)
# Equação do circulo
# dk^2 = (x - xR)^2 + (y - yR)^2
# Expandindo a equação
# dk^2 = x^2 - 2xXR + xR^2 + y^2 - 2yyR + yR^2
# Subtraindo receptor2 - receptor1, receptor3 - receptor1 ...
# (+2x1 - 2x2)x + (+2y1 - 2y2)y = d2^2 - d1^2 - x2^2 + x1^2 - y2^2 + y1^2
# (+2x2 - 2x3)x + (+2y2 - 2y3)y = d3^2 - d1^2 - x3^2 + x1^2 - y3^2 + y1^2


def linearSolve(coordenadas, dk):
    x = [i[0] for i in coordenadas]
    y = [i[1] for i in coordenadas]

    matrixA = np.matrix([[2*x[0] - 2*x[1], 2*y[0] - 2*y[1]],  # -2x[1] -2x[1] - (-2x[0] -y[0] )
                        [2*x[0] - 2*x[2], 2*y[0] - 2*y[2]],
                        [2*x[0] - 2*x[3], 2*y[0] - 2*y[3]],
                        [2*x[0] - 2*x[4], 2*y[0] - 2*y[4]]])

    matrixB = np.matrix([[dk[1]**2 - dk[0]**2 + x[0]**2 - x[1]**2 + y[0]**2 - y[1]**2],  # (dk[1]**2 - (x[1]**2 + y[1]**2) - ((dk[0]**2 - (x[0]**2 + y[0]**2))
                        [dk[2]**2 - dk[0]**2 + x[0]**2 - \
                            x[2]**2 + y[0]**2 - y[2]**2],
                        [dk[3]**2 - dk[0]**2 + x[0]**2 - \
                            x[3]**2 + y[0]**2 - y[3]**2],
                        [dk[4]**2 - dk[0]**2 + x[0]**2 - x[4]**2 + y[0]**2 - y[4]**2]])
    """
for i in range(1, len(x)):
        A = np.append(A, [[-2*(x[i]-x[0]), -2*(y[i]-y[0])]], axis=0)
    #print(A)
        
    for i in range(1, len(x)):
        B = np.append(B, [[((dk[i]**2 - (x[i]**2 + y[i]**2)) - ((dk[0]**2 - (x[0]**2 + y[0]**2))))]])
    """
    return np.linalg.inv(matrixA.transpose() * matrixA) * matrixA.transpose() * matrixB


def dist(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.linalg.norm(a-b)


def plot(coordenadas, dk, resp):
    x = [i[0] for i in coordenadas]
    y = [i[1] for i in coordenadas]
    resp = [float(resp[0]), float(resp[1])]
    circle1 = plt.Circle((x[0], y[0]), dk[0], fill=False)
    circle2 = plt.Circle((x[1], y[1]), dk[1], fill=False)
    circle3 = plt.Circle((x[2], y[2]), dk[2], fill=False)
    circle4 = plt.Circle((x[3], y[3]), dk[3], fill=False)
    circle5 = plt.Circle((x[4], y[4]), dk[4], fill=False)
    fig, ax = plt.subplots()
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    ax.add_patch(circle4)
    ax.add_patch(circle5)
    # Receptores
    plt.scatter(x, y, c="red")
    # Emissor
    plt.scatter(float(resp[0]), resp[1], c="blue")
    plt.show()


def main():
    print("As coordenadas (x, y, z) dos receptores são: ")
    print("  x  |  y  |  z\n",
          "1.55 17.63 1.35\n"
          "-4.02 0.00  1.35\n"
          "-4.40 9.60  1.35\n"
          " 9.27 4.64  1.35\n"
          " 9.15 12.00 1.35")
    coordenadas = [[1.55, 17.63, 1.35], [-4.02, 0.00, 1.35],
                   [-4.40, 9.60, 1.35], [9.27, 4.64, 1.35], [9.15, 12.00, 1.35]]
    pk0 = [-26.0, -33.8, -29.8, -31.2, -33.0]
    lk = [2.1, 1.8, 1.3, 1.4, 1.5]
    pk = "-48.4 -50.6 -32.2 -47.4 -46.3"
    # pk = "-46.9 -46.4 -41.2 -45.8 -48.7"
    pk = pk.split(" ")
    pk = [float(i) for i in pk]
    dk = distanciaRadial(coordenadas, pk0, lk, pk)

    print(dk)

    # resp = linearSolve(coordenadas, dk)
    # print("X: ", float(resp[0]), " Y: ", float(resp[1]))
    # print("Distancia Euclidiana ", dist([3,3], [float(resp[0]), float(resp[1])]))
    # plot(coordenadas, dk, resp)


if __name__ == '__main__':
    main()
