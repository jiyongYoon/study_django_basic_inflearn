import subprocess


## 현재 해당코드로 실행하면 종료 시 커넥션이 끊어지지 않는 중...

def create_worker():
    # subprocess.Popen(['python', 'rq_worker.py'])
    subprocess.Popen(['python3', 'rq_worker.py'])


if __name__ == '__main__':
    for _ in range(3):
        create_worker()