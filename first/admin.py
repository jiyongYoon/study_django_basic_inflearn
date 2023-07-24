from django.contrib import admin
from third.models import *

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('point', 'comment', 'restaurant')
    search_fields = ('point', 'restaurant')
    actions = ['make_point_as_5']

    def make_point_as_5(self, request, queryset):
        queryset.update(point='5')
    make_point_as_5.short_description = "평점 5점으로 올리기"


admin.site.register(Review, ReviewAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address') # 테이블 형태로 보고싶다면 컬럼명 추가
    search_fields = ('address', ) # 검색 컬럼 추가


admin.site.register(Restaurant, RestaurantAdmin)
