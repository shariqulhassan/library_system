from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('borrow/<int:id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:id>/', views.return_book, name='return_book'),
    path('category/<int:category_id>/', views.category_view, name='category_view'),
]
