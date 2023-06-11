from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.UsersHome.as_view(), name='index'),

]

urlpatterns += [
    path('about/', views.UsersAbout.as_view(), name='about'),
    path('add_user/', views.AddUser.as_view(), name='add_user'),
    path('analysis/', views.AnalysisListView.as_view(), name='analysis'),
    path('category/<int:category_id>/', views.AnalysisListView.as_view(), name='category'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),




]