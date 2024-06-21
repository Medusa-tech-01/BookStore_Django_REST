"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import *

urlpatterns = [
    path('', BookListView.as_view(), name="list_books"),
    path('add/', BookCreateView.as_view(), name="add_book"),
    path('update/<int:pk>/', BookUpdateView.as_view(), name="update_books"),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name="delete_books"),

    path('list/view/', list_books, name="list_books_view"),
    path('add/view/', add_books, name="add_books_view"),
    path('update/view/<int:pk>/', update_books, name="update_books_view"),
    path('delete/view/<int:pk>/', delete_books, name="delete_books_view"),
    path('admin/', admin.site.urls),
]
