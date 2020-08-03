from abc import ABC

from rest_framework import serializers

from quiz.models import Quiz, SimpleQuestion, ChoiceQuestionItem, ChoiceQuestion, MultiChoiceQuestion, \
    MultiChoiceQuestionItem, MultiChoiceAnswer, SimpleAnswer, ChoiceAnswer


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'date_start', 'date_end', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            # Запрет на изменение "Дата начала"
            self.fields.get('date_start').read_only = True


class SimpleQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimpleQuestion
        fields = ('quiz', 'question')


class ChoiceQuestionItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChoiceQuestionItem
        fields = ('choice_question', 'choice_value',)


class ChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChoiceQuestion
        fields = ('quiz', 'question',)


class MultiChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiChoiceQuestion
        fields = ('quiz', 'question')


class MultiChoiceQuestionItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiChoiceQuestionItem
        fields = ('choice_question', 'choice_value')


class SimpleAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimpleAnswer
        fields = ('question', 'answer', 'user_id')


class ChoiceAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChoiceAnswer
        fields = ('question', 'answer', 'user_id')


class MultiChoiceAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiChoiceAnswer
        fields = ('question', 'answer', 'user_id')


class GeneralAnswerSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    user_id = serializers.IntegerField()
    question = serializers.CharField()
    answer = serializers.CharField()
