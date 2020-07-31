from django.db import models


class Quiz(models.Model):
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title

    title = models.CharField(verbose_name="Текст опроса", max_length=80)
    date_start = models.DateField(verbose_name="Дата начала")
    date_end = models.DateField(verbose_name="Дата окончания")
    description = models.TextField(verbose_name="Описание")


class Question(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return str(self.quiz)

    quiz = models.ForeignKey(Quiz, verbose_name="Опрос", on_delete=models.CASCADE)


class SimpleQuestion(Question):
    class Meta:
        verbose_name = 'Ответ текстом'
        verbose_name_plural = 'Ответы текстом'

    def __str__(self):
        return "Simple: ".format(self.answer)

    answer = models.TextField(verbose_name="Ответ")


class ChoiceQuestionItem(models.Model):
    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Вариант ответа'

    def __str__(self):
        return str(self.choice_value)

    choice_value = models.TextField(verbose_name="Вариант ответа")


class ChoiceQuestion(Question):
    class Meta:
        verbose_name = 'Вопрос с одним вариантом ответа'
        verbose_name_plural = 'Вопросы с одним вариантом ответа'

    def __str__(self):
        return str(self.choice)

    choice = models.ForeignKey(ChoiceQuestionItem, verbose_name="Правильный ответ", on_delete=models.CASCADE)