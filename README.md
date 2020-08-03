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
#####Интерфейс администратора (требуется авторизация)
/quizzes/ - Просмотр и ввод информации об опросе

/simple/ - Вопрос с текстовым ответом 

/choice/ - Вопрос с одним вариантом выбора

/choice-item/ - Варианты для choice

/multi-choice/ - Вопрос с множественными вариантами

/multi-choice-item/ - Варианты для для вопросов с множественным выбором

#####Интерфейс пользователя
/simple-answer/ - Простой ответ текстом

/choice-answer/ - Ответ для вопросов с одним вариантом

/multi-choice-answer/ - Ответы для вопросов с множественным выбором

/user-active-quizzes/ - Список активных опросов

/user-quizzes-passed\[?user_id=USER_ID\]/ - просмотр пройдённых опросов; 
при указании параметра USER_ID, происходит фильтрация по ID пользователя