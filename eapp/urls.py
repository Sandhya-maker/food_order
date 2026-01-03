# from django.urls import path
# from . import views

# app_name = 'eapp'

# urlpatterns = [
#     path("", views.index, name="home"),  
#     path("category/<str:slug>/", views.index, name="category"),
# ]


from django.urls import path
from . import views

app_name = "eapp"

urlpatterns = [
    path("", views.index, name="home"),
    path("category/<str:slug>/", views.index, name="category"),
    path("food/<int:id>/", views.food_detail, name="food_detail"),
]


