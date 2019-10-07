from rest_framework import routers

from home import views

router = routers.DefaultRouter()

router.register(r"home", views.HomeViewSet, basename="homes")

urlpatterns = router.urls
