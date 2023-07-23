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


# CBV(Class-Based Views)
from django.views import View


class BaseView(View):
    def get(self, request):
        # restaurants = Restaurant.objects.all()
        restaurants = Restaurant.objects.all() \
            .annotate(reviews_count=Count('review')) \
            .annotate(average_point=Avg('review__point'))
        # reviews_count 라는 이름으로 Count('review') 값에 접근할 수 있게 됨.
        # review 모델 안에 속성에 접근할때는 __ (언더바 2개)로 접근할 수 있음.
        paginator = Paginator(restaurants, 5)

        page = request.GET.get('page')  ## third/list?page=1
        items = paginator.get_page(page)

        context = {
            'restaurants': items
        }
        return render(request, 'third/list.html', context)


from django.views.generic import ListView


class ListBaseView(ListView):
    # 어떤 모델의 데이터를 가져올 것인지
    model = Restaurant
    # 기본적으로 app/모델명_list.html 형태로 매핑해줌. 다른 이름이면 특정해주면 됨.
    # template_name = 'third/restaurant_list.html'
    # context에 담을 이름
    context_object_name = 'restaurants'
    # 페이징 처리 가능
    paginate_by = 5

    # 모델리스트를 가져올 때 사용할 쿼리도 커스텀 해줄 수 있음.
    def get_queryset(self):
        return Restaurant.objects.all() \
            .annotate(reviews_count=Count('review')) \
            .annotate(average_point=Avg('review__point'))