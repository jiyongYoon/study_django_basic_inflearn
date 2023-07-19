import time
import os

from redis_conf import getConn
from redis import Redis
from rq import Queue, Connection

from rq_task import test_fib

# REDIS_HOST = 'redis'
# REDIS_PORT = 6379
# REDIS_DB = 0
#
# redis_conn = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def main():
    # Redis 연결
    redis_conn = getConn()
    # redis_conn = Redis()

    # 작업 큐 생성
    q = Queue(connection=redis_conn)

    fib_range = range(30, 40)

    # 작업 큐에 작업 추가
    # joblist = []
    # for x in fib_range:
    #     job = q.enqueue(test_fib, x) # 작업 함수와 파라미터 함께 큐에 추가
    #     print(f'Job Register, ID: {job.id} , num: {x}') # 각 작업별로 고유 id가 있음
    #     joblist.append(job)

    async_results = [q.enqueue(test_fib, x) for x in fib_range]

    start_time = time.time()
    # 종료 flag
    done = False

    while not done:
        os.system('clear')
        # 시작 시간
        print('Asynchronously: (now = %.2f)' % (time.time() - start_time,))
        done = True
        # for i, x in enumerate(joblist):
        for i, x in enumerate(async_results):
            # 결과 반환
            result = x.return_value
            if result is None:
                done = False
                result = '(calculating)'
            # 결과 콘솔 출력
            print('fib(%d) = %s' % (i, result))
        print('')
        # CLI에서 실행 추천
        print('To start the actual in the background, run a worker: ')
        print('      python examples/run_worker.py')
        # 잠시 대기
        time.sleep(0.2)

    print('Done')


if __name__ == '__main__':
    with Connection(connection=getConn()):
    # with Connection(connection=Redis()):
        main()