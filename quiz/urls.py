
from django.urls import path, include
from rest_framework import routers

from quiz.views import QuizViewSet, SimpleQuestionViewSet

router = routers.DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'simple', SimpleQuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
