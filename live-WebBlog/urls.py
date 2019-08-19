from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name ='home'),
    path('detail/<post_id>/',views.detail,name ='detail'),
    # path('detail/<post_id>/comments/',views.create_comment,name ='comment'),
]
