from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns =[
    path('pro/',views.ProductViewSet.as_view({"get":"list","post":"create"})),
    path('pro/<str:pk>/',views.ProductViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'})),
    path('type/',views.TypelistViewSet.as_view({"get":"list","post":"create"})),
    path('type/<str:pk>/',views.TypelistViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'})),
    path('que/',views.QuestionlistViewSet.as_view({"get":"list","post":"create"})),
    path('que/<str:pk>/',views.QuestionlistViewSet.as_view({'get': 'retrieve','put': 'update','delete': 'destroy'})),
    path('',views.index,name='index'),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

