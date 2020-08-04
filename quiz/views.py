from datetime import date

from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response

from quiz.models import Quiz, SimpleQuestion, ChoiceQuestionItem, ChoiceQuestion, MultiChoiceAnswer, SimpleAnswer, \
    ChoiceAnswer
from quiz.serializers import QuizSerializer, SimpleQuestionSerializer, ChoiceQuestionItemSerializer, \
    ChoiceQuestionSerializer, MultiChoiceAnswerSerializer, SimpleAnswerSerializer, TextAnswerSerializer, \
    ChoiceAnswerSerializer, TextMultiAnswerSerializer


class QuizViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class SimpleQuestionViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    queryset = SimpleQuestion.objects.all()
    serializer_class = SimpleQuestionSerializer


class ChoiceQuestionItemViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    queryset = ChoiceQuestionItem.objects.all()
    serializer_class = ChoiceQuestionItemSerializer


class ChoiceQuestionViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (DjangoModelPermissions,)

    queryset = ChoiceQuestion.objects.all()
    serializer_class = ChoiceQuestionSerializer


class SimpleAnswerViewSet(viewsets.ModelViewSet):
    queryset = SimpleAnswer.objects.all()
    serializer_class = SimpleAnswerSerializer


class ChoiceAnswerViewSet(viewsets.ModelViewSet):
    queryset = ChoiceAnswer.objects.all()
    serializer_class = ChoiceAnswerSerializer


class MultiChoiceAnswerViewSet(viewsets.ModelViewSet):
    queryset = MultiChoiceAnswer.objects.all()
    serializer_class = MultiChoiceAnswerSerializer


class ActiveQuizAPIView(generics.ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        today = date.today()
        return Quiz.objects.filter(date_start__lte=today, date_end__gte=today)


class UserQuizzesAPIView(ListAPIView):
    def list(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }

        simple_answers = SimpleAnswer.objects.all()
        choice_answers = ChoiceAnswer.objects.all()
        multi_choice_answers = MultiChoiceAnswer.objects.all()
        try:
            user_id = int(request.GET.get('user_id'))
            simple_answers = SimpleAnswer.objects.filter(user_id=user_id)
            choice_answers = ChoiceAnswer.objects.filter(user_id=user_id)
            multi_choice_answers = MultiChoiceAnswer.objects.filter(user_id=user_id)
        except Exception:
            pass

        simple_serializer = TextAnswerSerializer(simple_answers, many=True, context=serializer_context)
        choice_serializer = TextAnswerSerializer(choice_answers, many=True, context=serializer_context)
        multi_choice_serializer = TextMultiAnswerSerializer(multi_choice_answers, many=True, context=serializer_context)

        return Response({"answers": simple_serializer.data + choice_serializer.data + multi_choice_serializer.data})
