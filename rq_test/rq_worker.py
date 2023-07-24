from redis_conf import getConn
from rq import Queue, Worker, Connection


def main():
    with Connection(connection=getConn()):
        # 작업자(worker) 생성 및 작업 처리
        worker = Worker([Queue()])
        worker.work()

    print("Worker process has been terminated.")


if __name__ == '__main__':
    main()
