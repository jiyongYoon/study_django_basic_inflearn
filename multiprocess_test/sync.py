from multiprocessing import Pool
import multiprocessing as mp
import time


def func(num):
    c_proc = mp.current_process()
    print("Running on Process", c_proc.name, "PID", c_proc.pid)
    time.sleep(1)
    print("Ended", num, "Process", c_proc.name)
    return num


if __name__ == '__main__':
    with Pool(4) as p:
        start = time.time()

        ret = p.apply(func, (1,))
        print(ret)
        ret = p.apply(func, (2,))
        print(ret)
        ret = p.apply(func, (3,))
        print(ret)
        ret = p.apply(func, (4,))
        print(ret)
        ret = p.apply(func, (5,))
        print(ret)

        delta_t = time.time() - start
        print("Time :", delta_t)
