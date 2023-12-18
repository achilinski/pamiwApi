from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api import views

schema_view = get_schema_view(
    openapi.Info(
        title='BetterCalendar-API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('all-books/', views.get_all_books, name='get_all_books'),
    path('all-authors/', views.get_all_authors, name='get_all_authors'),
    path('all-categories/', views.get_all_categories, name='get_all_categories'),
    path('all-users/', views.get_all_users, name='get_all_users'),
    path('book/<int:pk>/', views.get_book, name='get_book'),
    path('author/<int:pk>/', views.get_author, name='get_author'),
    path('category/<int:pk>/', views.get_Category, name='get_Category'),
    path('user/<int:pk>/', views.get_user, name='get_user'),
    path('delete-book/<int:pk>/', views.delete_book, name='delete_book'),
    path('delete-author/<int:pk>/', views.delete_author, name='delete_author'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete_category'),
    path('delete-user/<int:pk>/', views.delete_user, name='delete_user'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-user/', views.add_user, name='add_user'),
    path('edit-book/<int:pk>/', views.edit_book, name='edit_book'),
    path('edit-author/<int:pk>/', views.edit_author, name='edit_author'),
    path('edit-category/<int:pk>/', views.edit_category, name='edit_category'),
    path('edit-user/<int:pk>/', views.edit_user, name='edit_user'),
    path('books-by-category/<int:pk>/', views.get_books_by_category, name='get_books_by_category'),
    path('books-by-author/<int:pk>/', views.get_books_by_author, name='get_books_by_author'),
    path('books-by-user/<int:pk>/', views.get_books_read_by_user, name='get_books_read_by_user'),
    path('best-authors/<int:n>/', views.get_best_authors, name='get_best_authors'),
    path('best-books/<int:n>/', views.get_best_books, name='get_best_books'),
    path('search-books/<str:title>/', views.search_books, name='search_books'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),


]