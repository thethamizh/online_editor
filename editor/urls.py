from django.urls import path
from .views import save_text, get_text, index

urlpatterns = [
    path('', index, name='index'),  # Add this line
    path('save/', save_text, name='save_text'),
    path('text/<str:text_id>/', get_text, name='get_text'),
]
