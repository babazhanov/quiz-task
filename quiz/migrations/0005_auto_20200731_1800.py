# Generated by Django 2.2.10 on 2020-07-31 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_multichoiceanswer_multichoicequestion_multichoicequestionitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicequestion',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.ChoiceQuestionItem', verbose_name='Ответ'),
        ),
    ]