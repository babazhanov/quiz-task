
from django.urls import path, include
from rest_framework import routers

from quiz.views import QuizViewSet, SimpleQuestionViewSet, ChoiceQuestionItemViewSet, ChoiceQuestionViewSet, \
    MultiChoiceQuestionViewSet, MultiChoiceQuestionItemViewSet, MultiChoiceAnswerViewSet, ActiveQuizAPIView, \
    SimpleAnswerViewSet, UserQuizzesAPIView, ChoiceAnswerViewSet

router = routers.DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'simple', SimpleQuestionViewSet)
router.register(r'choice-item', ChoiceQuestionItemViewSet)
router.register(r'choice', ChoiceQuestionViewSet)
router.register(r'multi-choice', MultiChoiceQuestionViewSet)
router.register(r'multi-choice-item', MultiChoiceQuestionItemViewSet)
router.register(r'simple-answer', SimpleAnswerViewSet)
router.register(r'choice-answer', ChoiceAnswerViewSet)
router.register(r'multi-choice-answer', MultiChoiceAnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('user-active-quizzes', ActiveQuizAPIView.as_view(), name='user-active-quizzes'),
    path('user-quizzes-passed', UserQuizzesAPIView.as_view(), name='user-quizzes-passed'),
]
