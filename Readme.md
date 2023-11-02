### Medical+

Medical+ это проект сайта медицинского центра, разработанный в django. Администратор может добавить врача, Пользователь может просмотреть профиль врача, а также записаться на прием.
Они также могут связаться по электронной почте.

### Настройка, установка и запуск

Чтобы запустить приложение на локальном компьютере, вам потребуется Python 3+, установленный на вашем компьютере. 
Выполните все шаги, чтобы запустить этот проект.

1.  Создайте виртуальное окружение, либо запустите проект с Poetry :
```bash
virtualenv env_name
```
    
2.  Активируйте виртуальное окружение:
```bash
On Linux - source virtualenv_name/bin/activate
On Windows - virtualenv_name/Scripts/activate
```

3. Сначала вам нужно клонировать или скачать мой проект из репозитория github:
```bash
git clone https://github.com/taures88/Medical.git
```
4. Затем создайте БД и внесите свои данные:
``` bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your name',
        'USER': 'your user',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

5. Установите файл зависимостей
```bash
  pip install -r requirements.txt
``` 

6. Запустите сервер!
```python
  python manage.py runserver
```

7. Затем перейдите по адресу ```http://127.0.0.1:8000``` в своем браузере.

### Чтобы создать суперпользователя, откройте терминал и введите:
```
python manage.py createsuperuser
```
### Для отправки электронной почты заполните информацию в настройках вашего проекта.
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.com'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your email password'
```

