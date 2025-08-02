from django.urls import path
from .views import OptimizeInstanceView

urlpatterns = [
    path('optimize/', OptimizeInstanceView.as_view(), name='optimize-instance'),
]