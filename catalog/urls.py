from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('foto/<int:pk>', views.DetailPageView.as_view(model=models.Foto), name='detail'),
    path('add', views.AddPageView.as_view(), name='add'),
    path('update/<int:pk>', views.UpdatePageView.as_view(model=models.Foto), name='update'),
    path('search', views.SearchPageView.as_view(), name='search'),
    path('delete/<int:pk>', views.DeletePageView.as_view(model=models.Foto), name='delete'),

]