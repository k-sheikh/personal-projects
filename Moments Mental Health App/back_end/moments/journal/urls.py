from django.urls import path

from rest_framework import routers
from .views import EntryViewSet, MomentViewSet, PromptViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'entry', EntryViewSet, basename="entry")
router.register(r'moment', MomentViewSet, basename="moment")
router.register(r'prompt', PromptViewSet, basename="prompt")
router.register(r'user', UserViewSet, basename="user")

urlpatterns = router.urls