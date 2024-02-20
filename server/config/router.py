from rest_framework import routers

from apps.members.views import MemberViewSet

router = routers.DefaultRouter()
router.register('member', MemberViewSet)
