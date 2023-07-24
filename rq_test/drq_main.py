import django_rq

from rq_test.rq_task import test_fib
from rq_test.redis_conf import getConn

# 장고 모듈을 장고에서 사용하지 않고 파이썬 모듈만 실행하는 경우 이렇게 등록해줘야 한다고 함
""" 에러 StackTrace
raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Requested setting RQ_SHOW_ADMIN_LINK, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_django.settings")


def main():
    redis_conn = getConn()

    print(redis_conn)

    default_job_list = []
    high_job_list = []

    for _ in range(30, 40):
        enqueue = django_rq.enqueue(test_fib, _)
        default_job_list.append(enqueue.id)

        djangoQ = django_rq.get_queue('high')
        django_q_enqueue = djangoQ.enqueue(test_fib, _)
        high_job_list.append(django_q_enqueue.id)

    for i, default_job in enumerate(default_job_list):
        print(f'default 에 enqueue한 job {i} / ID: {default_job}')

    for i, high_job in enumerate(high_job_list):
        print(f'high 에 enqueue한 job {i} / ID: {high_job}')

    ######## 작업 적재 끝 ########

    queue = django_rq.get_queue('default')
    print(f'[defaultQ] job ID: {queue.job_ids}')
    # queue.empty()
    print(queue.count)

    # job = job_list.pop()
    # fetch_job = queue.fetch_job(job.id)
    # print(f'[defaultQ] pop한 job ID: {fetch_job.id}')

    djangoQQ = django_rq.get_queue('high')
    print(f'[djangoQ] job ID: {djangoQQ.job_ids}')
    # djangoQQ.empty()
    print(djangoQQ.count)

    # fetch_job = djangoQQ.fetch_job(job.id)
    # print(f'[djangoQ] pop한 job ID: {fetch_job.id}')

