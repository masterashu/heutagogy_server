from django.urls import path
from .views import LessonsGetView

urlpatterns = [
    path('lessons', LessonsGetView.as_view(), name='lessons_get_view'),
]
