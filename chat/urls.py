from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.chat_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('login', views.loginView, name="login"),
    path('chat/', views.chat, name='chat'),
    path('register/', views.registerView, name='register'),

]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
