from rest_framework import routers
from .views import RegularPlanViewset
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'plans', RegularPlanViewset)

urlpatterns = [
    path('', include(router.urls)),
]
