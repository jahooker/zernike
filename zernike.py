from matplotlib import pyplot as plt
import math
import numpy as np

class R:

    def __init__(self, n: int, m: int):
        assert 0 <= m <= n
        self.m = m
        self.n = n

    def __call__(self, rho: float):
        m = self.m
        n = self.n
        if ((n - m) % 2 == 1):
            return 0
        return sum(
            (-1) ** k * math.factorial(n - k) * math.pow(rho, (n - 2 * k)) /
            (math.factorial(k) * math.factorial((n + m) // 2 - k) * math.factorial((n - m) // 2 - k))
            for k in range(0, (n - m) // 2 + 1)
        )

rhos = np.linspace(0, 1, 100)

'''
for n in range(20):
    for m in range(n):
        rmn = R(n, m)
        plt.plot(rhos, [rmn(rho) for rho in rhos])
    plt.show()
'''

class Z:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m

    def __call__(self, rho: float, phi: float):
         m = self.m
         n = self.n
         if m >= 0:
             # Even
             return R(n, +m)(rho) * math.cos(+m * phi)
         else:
             # Odd
             return R(n, -m)(rho) * math.sin(-m * phi)


for n in range(10):
    for m in range(-n, n + 1):

        if ((n - m) % 2 == 1): continue

        sr = 200  # Sampling rate (how many pixels for the diameter of the disk)

        pad = 0.1
        side = int(sr * (1 + 2 * pad))
        arr = np.zeros((side, side))
        for i in range(side):
            for j in range(side):
                x, y = (i - side/2) / (sr/2), (j - side/2) / (sr/2)
                rho = math.hypot(x, y)
                if rho > 1: continue
                phi = math.atan2(y, x)
                arr[i][j] = Z(n, m)(rho, phi)

        plt.imshow(arr, interpolation='nearest')
        plt.title(f'Z{(n, m)}')
        plt.show()

