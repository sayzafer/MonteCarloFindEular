from bc import *
import os
from threading import Thread

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 1000000
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
