"""
URL configuration for alteasy_django_tt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from books.views import (
    BookListView, BookUpdateView, BookCreateView, BookDeleteView, BookDetailView
)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>', BookDetailView.as_view()),
    path('edit/<int:pk>', BookUpdateView.as_view()),
    path('new', BookCreateView.as_view()),
    path('delete/<int:pk>', BookDeleteView.as_view()),
    path('admin/', admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name='admin/login.html')),
    path("accounts/logout/", auth_views.LogoutView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
