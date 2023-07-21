import django_rq

from rq_task import test_fib
from redis_conf import getConn

# 장고 모듈을 장고에서 사용하지 않고 파이썬 모듈만 실행하는 경우 이렇게 등록해줘야 한다고 함
""" 에러 StackTrace
raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Requested setting RQ_SHOW_ADMIN_LINK, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_django.settings")

redis_conn = getConn()

print(redis_conn)

job_list = []

for _ in range(30, 40):
    enqueue = django_rq.enqueue(test_fib, _)
    print(f'enqueue한 job ID: {enqueue.id}')
    job_list.append(enqueue)

print(job_list.__sizeof__())

for _ in range(30, 40):
    queue = django_rq.get_queue(connection=getConn())
    job = job_list.pop()
    fetch_job = queue.fetch_job(job.id)
    print(f'pop한 job ID: {fetch_job.id}')

