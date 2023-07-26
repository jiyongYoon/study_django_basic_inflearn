import subprocess


## 현재 해당코드로 실행하면 종료 시 커넥션이 끊어지지 않는 중...
"""
poetry를 찾아보던 중, 해당 글에서 문제의 원인을 발견할 수 있었음.
https://spoqa.github.io/2019/08/09/brand-new-python-dependency-manager-poetry.html

Linux에서 어떤 프로그램을 Ctrl + c 로 종료시킬 때, SIGINT 시그널을 보내게 된다. (interrupt signal)

하지만 이 모듈에서 보면,
자식 프로세스를 만들고 나서 rq_worker_p.py를 Ctrl + c 로 종료하면 rq_worker_p.py는 종료가 되지만, subprocess들은 종료가 되지 않는다고 함.
즉, 부모 프로세스가 사라져 돌아다니는 '좀비 프로세스'가 되어버림...!
"""

def create_worker():
    # subprocess.Popen(['python', 'rq_worker.py'])
    subprocess.Popen(['python3', 'rq_worker.py'])


if __name__ == '__main__':
    for _ in range(3):
        create_worker()