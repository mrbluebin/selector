from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns =[
    path('testtime/',views.get_time.as_view()),
    path('tt/<int:pk>/',views.testD.as_view()),
    path('',views.index,name='index'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)