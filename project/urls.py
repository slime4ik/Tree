"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from menu import views as menu_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('food/', menu_view.food_view, name='food'),
    path('food/citruses/', menu_view.citruse_view, name='citruses'),    # МОЖНО ПРОСТО citruses/ но для понимания пользователя, в какой он ветке, лучше полностью расписать
    path('food/citruses/orange/', menu_view.orange_view, name='orange'),
    path('food/citruses/lime/', menu_view.lime_view, name='lime'),
    # path('drinks/', menu_view.drink_view, name='drinks'),
    # path('drinks/nonalcohol/', menu_view.nonalcohol_view, name='drinks'), 
    # path('drinks/', menu_view.alcohol_view, name='drinks'),
    # path('drinks/', menu_view.juices, name='drinks'),
]

