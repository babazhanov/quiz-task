from django.shortcuts import render
from rest_framework import viewsets

from quiz.models import Quiz, SimpleQuestion
from quiz.serializers import QuizSerializer, SimpleQuestionSerializer


class QuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class SimpleQuestionViewSet(viewsets.ModelViewSet):

    queryset = SimpleQuestion.objects.all()
    serializer_class = SimpleQuestionSerializer



