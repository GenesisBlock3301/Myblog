from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name ='home'),
    path('home/<str:cat_name>/',views.catagory,name = 'catagory'),
    path('summery/<post_id>/',views.summery,name ='summery'),
    path('detail/<post_id>/',views.detail,name ='detail'),
    path('about/',views.about, name = "about"),
    path('problem/',views.problem, name = 'problem'),
    path('problem-list/',views.problem_list , name = "problem-list"),
]
