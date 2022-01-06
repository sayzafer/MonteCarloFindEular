import random
import time
from numba import jit


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindE:
    def __init__(self):
        self.count = 0
        self.index = 0

    def find_euler(self, n):
        (self.count, self.index) = self.find_euler_static(n)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def find_euler_static(n):
        count = 0
        index = 0
        for _ in range(n):
            count += 1
            sum = 0
            while True:
                sum = sum + random.random()
                index += 1
                if sum >= 1:
                    break
        return count, index

    def value_of_e(self):
        return self.index / self.count
