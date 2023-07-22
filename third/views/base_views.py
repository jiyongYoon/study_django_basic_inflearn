from django.core.paginator import Paginator
from django.db.models import Count, Avg
from django.shortcuts import render

from third.models import Restaurant


def list(request):
    # restaurants = Restaurant.objects.all()
    restaurants = Restaurant.objects.all()\
        .annotate(reviews_count=Count('review'))\
        .annotate(average_point=Avg('review__point'))
        # reviews_count 라는 이름으로 Count('review') 값에 접근할 수 있게 됨.
        # review 모델 안에 속성에 접근할때는 __ (언더바 2개)로 접근할 수 있음.
    paginator = Paginator(restaurants, 5)

    page = request.GET.get('page') ## third/list?page=1
    items = paginator.get_page(page)

    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)