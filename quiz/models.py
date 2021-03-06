from django.db import models


class Quiz(models.Model):
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title

    title = models.CharField(verbose_name="Название", max_length=80)
    date_start = models.DateField(verbose_name="Дата начала")
    date_end = models.DateField(verbose_name="Дата окончания")
    description = models.TextField(verbose_name="Описание")


class Question(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Абстрактный Вопрос'
        verbose_name_plural = 'Абстрактные Вопросы'

    def __str__(self):
        return str(self.quiz)

    quiz = models.ForeignKey(Quiz, verbose_name="Опрос", on_delete=models.CASCADE)
    question = models.TextField(verbose_name="Вопрос")


class SimpleQuestion(Question):
    class Meta:
        verbose_name = 'Ответ текстом'
        verbose_name_plural = 'Ответы текстом'

    def __str__(self):
        return "Simple: {}".format(self.question)


class ChoiceQuestionItem(models.Model):
    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Вариант ответа'

    def __str__(self):
        return "Item: {} {}".format(self.choice_question, self.choice_value)

    choice_question = models.ForeignKey("ChoiceQuestion", verbose_name="Вопрос с выбором", on_delete=models.CASCADE,
                                        null=True)
    choice_value = models.TextField(verbose_name="Вариант ответа")


class ChoiceQuestion(Question):
    class Meta:
        verbose_name = 'Вопрос с одним вариантом ответа'
        verbose_name_plural = 'Вопросы с одним вариантом ответа'

    def __str__(self):
        return "Choice: {}".format(self.question)


class MultiChoiceQuestion(Question):
    class Meta:
        verbose_name = 'Вопрос с несколькими вариантами'
        verbose_name_plural = 'Вопросы с несколькими вариантами'

    def __str__(self):
        return "MultiChoice: {}".format(self.question)


class MultiChoiceQuestionItem(models.Model):
    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Вариант ответа'

    def __str__(self):
        return "Item: {} {}".format(self.choice_question, self.choice_value)

    choice_question = models.ForeignKey(MultiChoiceQuestion, verbose_name="Вопрос с множественным выбором",
                                        on_delete=models.CASCADE, null=True)
    choice_value = models.TextField(verbose_name="Вариант ответа")


# Классы ответов для пользователей
class Answer(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Абстрактный Ответ'
        verbose_name_plural = 'Абстрактные Ответы'

    def __str__(self):
        return "User ID: {}".format(self.user_id)

    user_id = models.IntegerField(verbose_name="ID пользователя", null=True)


class SimpleAnswer(Answer):
    class Meta:
        verbose_name = 'Ответ текстом'
        verbose_name_plural = 'Ответы текстом'

    def __str__(self):
        return "Simple: {} {}".format(self.question, self.answer)

    question = models.ForeignKey(SimpleQuestion, verbose_name="Простой вопрос",
                                 on_delete=models.CASCADE, null=True)
    answer = models.TextField(verbose_name="Ответ")


class ChoiceAnswer(Answer):
    class Meta:
        verbose_name = 'Ответ с одним вариантом'
        verbose_name_plural = 'Ответ с одним вариантом'

    def __str__(self):
        return "Choice: {} {}".format(self.question, self.answer)

    question = models.ForeignKey(ChoiceQuestion, verbose_name="Вопрос с одним вариантом",
                                 on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(ChoiceQuestionItem, verbose_name="Ответ", on_delete=models.CASCADE, null=True)


class MultiChoiceAnswer(Answer):
    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'

    question = models.ForeignKey(MultiChoiceQuestion, verbose_name="Вопрос с множественным выбором",
                                        on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(MultiChoiceQuestionItem, verbose_name="Один из ответов",
                               on_delete=models.SET_NULL, null=True)
