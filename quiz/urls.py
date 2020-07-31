
from django.urls import path, include
from rest_framework import routers

from quiz.views import QuizViewSet

router = routers.DefaultRouter()
router.register(r'quizzes', QuizViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
