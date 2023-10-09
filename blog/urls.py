

from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('Post', views.IntruderImage)

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path('api_root/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
