from django.urls import path
from . import views

urlpatterns = [
    path('', views.artdata_search, name='artdata-search2'),
    path('filter/', views.ArtDataListView.as_view()),
    path('import/', views.upload_csv),
    path('search/', views.artdata_search, name='artdata-search'),
    path('<str:id>/', views.artdata_detail, name='artdata-detail'),

]
