import random
import time


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
        for _ in range(n):
            self.count += 1
            sum = 0
            while True:
                sum = sum + random.random()
                self.index += 1
                if sum >= 1:
                    break

    def value_of_e(self):
        return self.index / self.count
