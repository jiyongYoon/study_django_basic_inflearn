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

        ret1 = p.apply_async(func, (1,))
        ret2 = p.apply_async(func, (2,))
        ret3 = p.apply_async(func, (3,))
        ret4 = p.apply_async(func, (4,))
        ret5 = p.apply_async(func, (5,))
        print(ret1.get(), ret2.get(), ret3.get(), ret4.get(), ret5.get())

        delta_t = time.time() - start
        print("Time :", delta_t)
