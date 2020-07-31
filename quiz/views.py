from django.shortcuts import render
from rest_framework import viewsets

from quiz.models import Quiz, SimpleQuestion, ChoiceQuestionItem, ChoiceQuestion, MultiChoiceQuestion, \
    MultiChoiceQuestionItem, MultiChoiceAnswer
from quiz.serializers import QuizSerializer, SimpleQuestionSerializer, ChoiceQuestionItemSerializer, \
    ChoiceQuestionSerializer, MultiChoiceQuestionSerializer, MultiChoiceQuestionItemSerializer, \
    MultiChoiceAnswerSerializer


class QuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class SimpleQuestionViewSet(viewsets.ModelViewSet):

    queryset = SimpleQuestion.objects.all()
    serializer_class = SimpleQuestionSerializer


class ChoiceQuestionItemViewSet(viewsets.ModelViewSet):

    queryset = ChoiceQuestionItem.objects.all()
    serializer_class = ChoiceQuestionItemSerializer


class ChoiceQuestionViewSet(viewsets.ModelViewSet):

    queryset = ChoiceQuestion.objects.all()
    serializer_class = ChoiceQuestionSerializer


class MultiChoiceQuestionViewSet(viewsets.ModelViewSet):

    queryset = MultiChoiceQuestion.objects.all()
    serializer_class = MultiChoiceQuestionSerializer


class MultiChoiceQuestionItemViewSet(viewsets.ModelViewSet):

    queryset = MultiChoiceQuestionItem.objects.all()
    serializer_class = MultiChoiceQuestionItemSerializer


class MultiChoiceAnswerViewSet(viewsets.ModelViewSet):

    queryset = MultiChoiceAnswer.objects.all()
    serializer_class = MultiChoiceAnswerSerializer