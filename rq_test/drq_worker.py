import django_rq

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_django.settings")


def main():
    default_worker = django_rq.get_worker('default')
    default_worker.work()

    high_worker = django_rq.get_worker('high')
    high_worker.work()

    print("Worker process has been terminated.")


if __name__ == '__main__':
    main()