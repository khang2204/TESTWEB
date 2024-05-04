"""
URL configuration for DjangoWeb project.

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
from django.urls import path,include
from DjangoApp import views
from DjangoApp.views import ai_suggest,CustomPasswordResetView,CustomPasswordResetDoneView,CustomPasswordConfirmView,CustomPasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('usr/<int:user_id>/',views.whilelogin,name="whilelogin"),
    path('passwordreset/',CustomPasswordResetView.as_view(),name="passwordreset"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('passwordreset/done/',CustomPasswordResetDoneView.as_view(),name="passwordresetdone"),
    path('passwordreset/reset/<uidb64>/<token>/',CustomPasswordConfirmView.as_view(),name="passwordresetconfirm"),
    path('passwordreset/reset/<uidb64>/<token>/done',CustomPasswordResetCompleteView.as_view(),name="passwordresetcomplete"),
    path('post/<int:post_id>/', views.post, name='post'),
    path('search/', views.search, name="search"),
    path('aisuggest/', ai_suggest,name="AI suggest"),
    path('usr/<int:user_id>/editprofile/', views.editprofile, name="Edit Profile"),
    path('logout/',views.logoutPage,name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
