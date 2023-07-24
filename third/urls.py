from django.urls import path

# from . import views
#
# urlpatterns = [
#     path('list/', views.list, name='list'),
#     path('create/', views.create, name='restaurant-create'),
#     path('update/', views.update, name='restaurant-update'),
#     # path('detail/', views.detail, name='restaurant-detail'),
#     path('delete/', views.delete, name='restaurant-delete'),
#
#     path('restaurant/<int:id>/', views.detail, name='restaurant-detail'),
#     path('restaurant/<int:restaurant_id>/review/create/', views.review_create, name='review-create'),
#     path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', views.review_delete, name='review-delete'),
#     path('review/list/', views.review_list, name='review-list'),
# ]


from .views import base_views, restaurant_views, review_views

urlpatterns = [
    # base_views.py
    # path('list/', base_views.list, name='list'),

    # restaurant_views.py
    path('create/', restaurant_views.create, name='restaurant-create'),
    path('update/', restaurant_views.update, name='restaurant-update'),
    path('delete/', restaurant_views.delete, name='restaurant-delete'),
    path('restaurant/<int:id>/delete', restaurant_views.delete, name='restaurant-delete'),
    path('restaurant/<int:id>/', restaurant_views.detail, name='restaurant-detail'),

    # review_views.py
    path('restaurant/<int:restaurant_id>/review/create/', review_views.review_create, name='review-create'),
    path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', review_views.review_delete, name='review-delete'),
    path('review/list/', review_views.review_list, name='review-list'),
]

from .views.base_views import BaseView, ListBaseView

urlpatterns += [
    # CBV
    # path('list/', BaseView.as_view()),

    # Generic View
    path('list/', ListBaseView.as_view()),
]
