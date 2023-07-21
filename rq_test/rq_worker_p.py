import subprocess


def create_worker():
    # subprocess.Popen(['python', 'rq_worker.py'])
    subprocess.Popen(['python3', 'rq_worker.py'])


if __name__ == '__main__':
    for _ in range(3):
        create_worker()