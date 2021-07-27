from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('detail/<int:pk>',views.project_view,name='detail'),
    ]