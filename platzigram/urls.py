"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# Django imports
from django.contrib import admin
from django.urls import path
from django.conf import settings
# Para mostrar las imagenes en modo desarrollo
from django.conf.urls.static import static

# Views imports
from platzigram import settings, views as local_views
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', local_views.hello_world),
    path('sorted/', local_views.sorted),
    path('hi/<str:name>/<int:age>', local_views.sayHi),
    path('posts/', posts_views.list_posts),
    # MEDIA_URL y MEDIA_ROOT son variables definidas en el config
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)