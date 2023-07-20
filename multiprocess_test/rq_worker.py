from redis_conf import getConn
from rq import Queue, Worker


def main():
    with getConn():
        # 작업자(worker) 생성 및 작업 처리
        worker = Worker([Queue()])
        worker.work()


if __name__ == '__main__':
    main()
