from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VulnerabilityViewSet,
    FixedVulnerabilityViewSet,
    UnfixedVulnerabilityViewSet,
    VulnerabilitySummaryViewSet,
    DeleteVulnerabilityView
)

router = DefaultRouter()
router.register(r'vulnerabilities', VulnerabilityViewSet, basename='vulnerability')
router.register(r'fixed', FixedVulnerabilityViewSet, basename='fixed')
router.register(r'vulnerabilities-unfixed', UnfixedVulnerabilityViewSet, basename='unfixed')
router.register(r'vulnerabilities-summary', VulnerabilitySummaryViewSet, basename='summary')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'vulnerabilities/delete/<str:cve_id>/',
        DeleteVulnerabilityView.as_view(),
        name='delete-vulnerability'
    )
]
