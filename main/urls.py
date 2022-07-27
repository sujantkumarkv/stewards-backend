from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('stewards/<str:user__username>/', views.StewardView.as_view()),
    path('stewards/', views.StewardsView.as_view()),
    path('workstreams/<str:short_name>/', views.WorkStreamView.as_view()),
    path('workstreams/', views.WorkStreamsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
