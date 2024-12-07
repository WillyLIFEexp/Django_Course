from django.urls import path
from . import views

urlpatterns = [
    # This is the home page
    path('', views.index, name="index"),
    # This is another page
    path('next', views.next_url, name="next_url"),

    # Path parameter
    # This is the link if user input the correct parameter
    # We can set path converter in <>, such as <int:number>
    path('check/<str:category>', views.need_para_url, name="need_para_url"),
    # This is the link when user didn't input and we have to use defulat setting
    path('check/', views.need_para_url, name="need_para_url"),

    # Query parameter
    path('getuser', views.qryview, name='qryview')
]