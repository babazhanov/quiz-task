from django.shortcuts import render
from rest_framework import viewsets

from quiz.models import Quiz
from quiz.serializers import QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer