from django.urls import path
from .views import home, book, category, indication, search

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:book_id>', book, name='book'),
    path('category/<str:category_name>', category, name='category'),
    path('form', indication, name='indication'),
    path('search', search, name='search'),
]