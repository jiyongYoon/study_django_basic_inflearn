from django.shortcuts import render

from rq_test import drq_worker
from rq_test import drq_main


# Create your views here.
def run_worker(request):
    drq_worker.main()


def run_main(request):
    drq_main.main()
