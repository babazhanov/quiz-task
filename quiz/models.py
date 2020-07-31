from django.db import models


class Quiz(models.Model):
    class Meta:
        pass

    def __str__(self):
        pass


    title = models.CharField(verbose_name="Текст вопроса", max_length=80)
    date_start = models.DateField(verbose_name="Дата начала")
    date_end = models.DateField(verbose_name="Дата окончания")
    description = models.TextField(verbose_name="Описание")


class Question(models.Model):
    class Meta:
        pass

    def __str__(self):
        pass


    quiz = models.ForeignKey(Quiz, verbose_name="Опрос", on_delete=models.CASCADE)


class SimpleAnswer(models.Model):
    class Meta:
        pass

    def __str__(self):
        pass


    question = models.ForeignKey(Question, verbose_name="Вопрос", on_delete=models.CASCADE)
    answer = models.TextField(verbose_name="Описание")
