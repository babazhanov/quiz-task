
from django.urls import path, include
from rest_framework import routers

from quiz.views import QuizViewSet, SimpleQuestionViewSet, ChoiceQuestionItemViewSet, ChoiceQuestionViewSet, \
    MultiChoiceQuestionViewSet, MultiChoiceQuestionItemViewSet, MultiChoiceAnswerViewSet

router = routers.DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'simple', SimpleQuestionViewSet)
router.register(r'choice-item', ChoiceQuestionItemViewSet)
router.register(r'choice', ChoiceQuestionViewSet)
router.register(r'multi-choice', MultiChoiceQuestionViewSet)
router.register(r'multi-choice-item', MultiChoiceQuestionItemViewSet)
router.register(r'multi-choice-answer', MultiChoiceAnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
