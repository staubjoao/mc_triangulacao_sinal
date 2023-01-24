class Receptor:
    def __init__(self, x, y, z, pk0, lk):
        self.x = x
        self.y = y
        self.z = z
        self.pk0 = pk0
        self.lk = lk

    def distanciaRadial(self, pk):
        return 10 ** ((self.pk0-pk) / (10 * self.lk))


def main():
    r1 = Receptor(1.55, 17.63, 1.35, -26.0, 2.1)
    r2 = Receptor(-4.02, 0.00, 1.35, -33.8, 1.8)
    r3 = Receptor(-4.40, 9.60, 1.35, -29.8, 1.3)
    r4 = Receptor(9.27, 4.64, 1.35, -31.2, 1.4)
    r5 = Receptor(9.15, 12.00, 1.35, -33.0, 1.5)
    receptores = [r1, r2, r3, r4, r5]

    dk = []
    pk = [-48.4, -50.6, -32.2, -47.4, -46.3]
    # pk = "-46.9 -46.4 -41.2 -45.8 -48.7"

    for i in range(len(receptores)):
        dk.append(receptores[i].distanciaRadial(pk[i]))

    print(dk)

    # pk = "-46.9 -46.4 -41.2 -45.8 -48.7"


if __name__ == '__main__':
    main()
