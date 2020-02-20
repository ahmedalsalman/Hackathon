"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from wishapp import views
from django.conf.urls.static import static
from django.conf import settings
from wishapp import models

urlpatterns = [
    path('admin/', admin.site.urls),

    path('wishapp/home/<int:user_id>/list/',views.wishlist ,name='wishlist'),
    path('wishapp/home/<int:user_id>/list/addwish/',views.add_wish ,name='addwish'),
    path('wishapp/home/<int:user_id>/list/<int:wish_id>/delwish/',views.delete_wish ,name='delwish'),
    path('wishapp/home/<int:user_id>/list/<int:wish_id>',models.Wish),

    path('wishapp/home/',views.home ,name='home'),
    path('wishapp/noaccess/',views.no_access ,name='no-access'),
    path('wishapp/home/signup/',views.signup ,name='signup'),
    path('wishapp/home/signin/',views.signin ,name='signin'),
    path('wishapp/home/signout/',views.signout ,name='signout'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
