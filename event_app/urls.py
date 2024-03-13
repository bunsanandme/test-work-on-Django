from django.urls import path
from .views import OrganizationList, OrganizationDetail, EventDetail, EventList
app_name = 'event_app'

urlpatterns = [
    path('organization/', OrganizationList.as_view(), name='organization-list'),
    path('organization/<int:pk>/', OrganizationDetail.as_view(), name='organization-detail'),
    path('event/', EventList.as_view(), name='event-list'),
    path('event/<int:pk>/', EventDetail.as_view(), name='event-detail'),
]