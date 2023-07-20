import time

from redis_conf import getConn
from rq import Queue
from rq_task import test_fib


def main():
    redis_conn = getConn()

    q = Queue(connection=redis_conn)

    fib_range = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30]

    async_results = [q.enqueue(test_fib, x) for x in fib_range]

    start_time = time.time()
    done = False

    while not done:

        print('Asynchronously: (now = %.2f)' % (time.time() - start_time,))
        done = True
        for i, x in enumerate(async_results):
            result = x.return_value
            if result is None:
                done = False
                result = '(calculating)'
            print('fib(%d) = %s' % (i, result))
        time.sleep(0.2)

    print('Done')


if __name__ == '__main__':
    with getConn():
        main()
