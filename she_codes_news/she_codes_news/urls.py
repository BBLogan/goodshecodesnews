"""she_codes_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# News Setup Step 6: adding the URLS for our news/ app
# Users Setup Step 7: add the users app URLs to the project
# Users Setup Step 15: create a urls.py file for the users app

# she_codes_news/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('news/', include('news.urls', namespace='news')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
]