from rest_framework.routers import DefaultRouter

from dotsapp.views import *

router = DefaultRouter()

router.register(r'comment', CommentDataViewSet, basename='Comment')
router.register(r'', DotsDataViewSet, basename='Dots')

urlpatterns = router.urls