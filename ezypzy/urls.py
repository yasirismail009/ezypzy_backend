from django.urls import path
from ezypzy import views

urlpatterns = [
    path('file_save/', views.FileSave.as_view()),
]
