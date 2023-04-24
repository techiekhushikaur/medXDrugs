from django.urls import path
from . import views

from django.contrib import admin
from social_django.models import Association, Nonce, UserSocialAuth

admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)

urlpatterns = [
    path('login/',views.user_login,name = 'user_login'),
    path('logout/',views.user_logout ,name = 'user_logout'),
    path('register/',views.register,name = 'register'),
    path('registerNGO/',views.registerNGO,name = 'registerNGO'),
    path('edit_profile/',views.edit_profile , name = 'edit_profile'),
    path('profilepage/<str:username>/',views.profilepage,name='profilepage'),
   
]


