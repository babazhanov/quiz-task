# quiz-task
Опросы

### Установка
```shell script
sudo apt-get update && apt-get upgrade -y
sudo apt-get install -y python3 python3-pip python3-dev git
pip3 install virtualenv
git clone https://github.com/babazhanov/quiz-task
cd quiz-task
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
# В дальнейшем стоит настроить nginx и uWSGI
```

### API
/quizzes/ - Просмотр и ввод информации об опросе
* title - Название
* date_start - Дата старта
* date_end - Дата окончания
* description - Описание


/simple/ - Вопрос с текстовым ответом 

/choice/ - Вопрос с одним вариантом выбора

/choice-item/ - Варианты для choice

/multi-choice/ - Вопрос с множественными вариантами

/multi-choice-item/ - Варианты для multi-choice

/multi-choice-answer/ - Ответы для multi-choice
