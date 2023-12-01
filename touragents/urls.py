from django.urls import path
from .views import TourAgentListCreateView, TourAgentDetailView

urlpatterns = [
    path('touragents/', TourAgentListCreateView.as_view(), name='touragent-list'),
    path('touragents/<uuid:pk>/', TourAgentDetailView.as_view(), name='touragent-detail'),
]
