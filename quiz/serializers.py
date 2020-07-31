from rest_framework import serializers

from quiz.models import Quiz, SimpleQuestion, ChoiceQuestionItem, ChoiceQuestion


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
        fields = ('quiz', 'answer',)
