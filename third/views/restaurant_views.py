from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from third.models import Restaurant, Review
from third.forms import RestaurantForm, ReviewForm, UpdateRestaurantForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from third.forms import RestaurantForm
from third.models import Restaurant, Review


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/list/')
    else:
        form = RestaurantForm()
        return render(request, 'third/create.html', {'form': form})

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
    elif request.method == 'GET':
        id = request.GET.get('id')

    item = get_object_or_404(Restaurant, pk=id)

    if request.method == 'POST' and 'id' in request.POST: # 두번째 조건문은 업데이트를 하러 들어왔는데 id값이 없다면 업데이트 요청이 아니기 때문
        # item = get_object_or_404(Restaurant, pk=request.POST.get('id')) # 이렇게 가져오면 해당 레코드가 없는 경우 기본 404 리다이렉트 페이지 사용됨
        # item = Restaurant.objects.get(pk=request.POST.get('id')) # 이러면 쌩 에러 stacktrace까지 나옴
        password = request.POST.get('password', '') # '' 빈 str은 디폴트값
        # form = RestaurantForm(request.POST, instance=item) # 초기화 할 대상 instance를 item으로 지칭해줌. 만약 없다면 create가 되어버림
        form = UpdateRestaurantForm(request.POST, instance=item) # 초기화 할 대상 instance를 item으로 지칭해줌. 만약 없다면 create가 되어버림
        if form.is_valid() and password == item.password:
            item = form.save()
            # return HttpResponseRedirect('third/')
    elif request.method == 'GET':
        # item = Restaurant.objects.get(pk=request.GET.get('id')) # third/update?id=2 이런식으로 요청이 온다고 가정할때
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})

    return HttpResponseRedirect('/third/list/')


def detail(request, id):
    # if 'id' in request.GET:
    if 'id' is not None:
        # item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/list/')


def delete(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    if request.method == 'POST' and 'password' in request.POST:
        if item.password is None or item.password == request.POST.get('password'):
            item.delete()
            return redirect('list')
        else:
            return redirect('restaurant-detail', id=id)
    else:
        return render(request, 'third/delete.html', {'item': item})