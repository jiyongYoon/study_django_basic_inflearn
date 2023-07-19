from redis_conf import getConn
from rq import Queue, Worker, Connection
import threading
from multiprocessing import Pool


def main():
    # redis_conn = Redis()
    redis_conn = getConn()

    # with Connection(connection=getConn()):
    with Connection(connection=redis_conn):
        # 작업자(worker) 생성 및 작업 처리
        worker = Worker([Queue()])
        worker.work()
        # q = Queue()
        # Worker(q).work()


if __name__ == '__main__':
    # 작업자 개수
    num_workers = 3

    # # 작업자 스레드 시작
    # threads = []
    # for _ in range(num_workers):
    #     thread = threading.Thread(target=main)
    #     thread.start()
    #     threads.append(thread)
    #
    # # 모든 스레드 종료 대기
    # for thread in threads:
    #     thread.join()
    #

    # 작업자 프로세스 시작
    processes = []
    for _ in range(num_workers):
        process = multiprocessing.Process(target=main)
        process.start()
        processes.append(process)

    # 모든 프로세스 종료 대기
    for process in processes:
        process.join()