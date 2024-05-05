"""
URL configuration for projet project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from appliweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appliweb.urls')), # Include urls from 'myfaxes' app
    path('', include('usersapp.urls')), # Include urls from 'usersapp' app
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'appliweb.views.custom_page_not_found_view'
handler500 = 'appliweb.views.custom_error_view'
handler403 = 'appliweb.views.custom_permission_denied_view'
handler400 = 'appliweb.views.custom_bad_request_view'