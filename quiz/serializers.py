from rest_framework import serializers

from quiz.models import Quiz, SimpleQuestion, ChoiceQuestionItem, ChoiceQuestion, MultiChoiceQuestion, \
    MultiChoiceQuestionItem, MultiChoiceAnswer


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
        fields = ('quiz', 'question', 'answer',)


class ChoiceQuestionItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChoiceQuestionItem
        fields = ('choice_question', 'choice_value',)


class ChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChoiceQuestion
        fields = ('quiz', 'question', 'choice',)


class MultiChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiChoiceQuestion
        fields = ('quiz', 'question')


class MultiChoiceQuestionItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiChoiceQuestionItem
        fields = ('choice_question', 'choice_value')


class MultiChoiceAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiChoiceAnswer
        fields = ('choice_question', 'answer')