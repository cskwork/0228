"""mainsite URL Configuration

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
from django.contrib import admin
# Use include() to add URLS from the blog application 
from django.urls import path, include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

#BASE URLPATTERNS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('board.urls')), #Link to board urls.py
    path('home/', include('home.urls')), #Link to home urls.py
    path('summernote/', include('django_summernote.urls')),
    #PWA
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix

]

#Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', RedirectView.as_view(url='/home/', permanent=True)),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]  