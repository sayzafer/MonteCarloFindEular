from bc_numba import *
from threading import Thread
import os

if __name__ == '__main__':
    for _ in range(3):

        tt = TicToc()
        tt.tic()
        n = 10000000/8
        find_es = []
        threads = []

        for i in range(os.cpu_count()):
            find_es.append(FindE())
            threads.append(Thread(target=find_es[i].find_euler, args=(n,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        n = 0
        count = 0
        for find_e in find_es:
            n += find_e.index
            count += find_e.count

        print("e = ", n / count)
        print("TIME = ", tt.toc())
