from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from third.forms import ReviewForm
from third.models import Restaurant, Review


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', id=restaurant_id)
    else:
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = ReviewForm(initial={'restaurant': item}) # 미리 데이터를 채워서 form을 던짐
        return render(request, 'third/review_create.html', {'form': form, 'item': item})


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('restaurant-detail', id=restaurant_id)


def review_list(request):
    # reviews = Review.objects.all().order_by('-created_at')
    reviews = Review.objects.all().select_related().order_by('-created_at') # 연관관계 매핑된 객체까지 함께 불러옴
    paginator = Paginator(reviews, 10)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'reviews': items
    }
    return render(request, 'third/review_list.html', context)