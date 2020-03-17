# CondGuai-Açu
Aplicação para gerenciar condominio do Edifício Colina do Guai-Açu

![Python application](https://github.com/jlplautz/CondGuai-Acu/workflows/Python%20application/badge.svg)
[![Updates](https://pyup.io/repos/github/jlplautz/CondGuai-Acu/shield.svg)](https://pyup.io/repos/github/jlplautz/CondGuai-Acu/)
[![Python 3](https://pyup.io/repos/github/jlplautz/CondGuai-Acu/python-3-shield.svg)](https://pyup.io/repos/github/jlplautz/CondGuai-Acu/)
[![codecov](https://codecov.io/gh/jlplautz/course-django/branch/master/graph/badge.svg)](https://codecov.io/gh/jlplautz/course-django)



<h1>Procedimento executado</h1>

name: Python application

on: [pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        pip install pipenv
        pipenv sync --dev
    - name: Link with flake8
      run: |
        pipenv run flake8 .
```
CondGuai-Acu $ tree
.
├── LICENSE
└── README.md

CondGuai-Acu $ pyenv versions
  system
* 3.8.0 (set by /home/plautz/.pyenv/version)
CondGuai-Acu $ pyenv local 3.8.0
CondGuai-Acu $ pyenv local
3.8.0
CondGuai-Acu $ pyenv global
3.8.0

CondGuai-Acu $ pipenv shell
Creating a virtualenv for this project…
Pipfile: /home/plautz/PycharmProjects/CondGuai-Acu/Pipfile
Using /home/plautz/.pyenv/versions/3.8.0/bin/python3.8 (3.8.0) to create virtualenv…
⠦ Creating virtual environment...Already using interpreter /home/plautz/.pyenv/versions/3.8.0/bin/python3.8
Using base prefix '/home/plautz/.pyenv/versions/3.8.0'
New python executable in /home/plautz/PycharmProjects/CondGuai-Acu/.venv/bin/python3.8
Also creating executable in /home/plautz/PycharmProjects/CondGuai-Acu/.venv/bin/python
Installing setuptools, pip, wheel...
done.
✔ Successfully created virtual environment! 
Virtualenv location: /home/plautz/PycharmProjects/CondGuai-Acu/.venv
Creating a Pipfile for this project…
Launching subshell in virtual environment…
 . /home/plautz/PycharmProjects/CondGuai-Acu/.venv/bin/activate
CondGuai-Acu $  . /home/plautz/PycharmProjects/CondGuai-Acu/.venv/bin/activate

(CondGuai-Acu) CondGuai-Acu $ pipenv lock --clear
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Updated Pipfile.lock (db4242)!

(CondGuai-Acu) CondGuai-Acu $ pipenv install --dev flake8
+--------------------------------------------------------+
criar o arquivo .flake8 na raiz do projeto
[flake8]
max-line-length = 120
exclude = .venv
+--------------------------------------------------------+
criar o arquivo .pyup.yml
requirements:
  - Pipfile
  - Pipfile.lock
+--------------------------------------------------------+
```

<b>Inserir no github o Simple workflow Actions</b>
```
name: Python application

on: [pull_request]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        pip install pipenv
        pipenv sync --dev
    - name: Link with flake8
      run: |
        pipenv run flake8 .
```

<b>Instalar lib django</b>
```
CondGuai-Acu $ pipenv install django
```

<b>Ferramentas basicas do Django (linha de comando)</b>
```
(CondGuai-Acu) CondGuai-Acu $ django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).

(CondGuai-Acu) CondGuai-Acu $ django-admin startproject GuaiAcu .
(CondGuai-Acu) CondGuai-Acu $ cd GuaiAcu/
(CondGuai-Acu) GuaiAcu $ tree
.
├── asgi.py
├── __init__.py
├── settings.py
├── urls.py
└── wsgi.py

(CondGuai-Acu) GuaiAcu $ mng runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

March 14, 2020 - 22:21:26
Django version 3.0.4, using settings 'GuaiAcu.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

<b>Instalar as libs pytest-cov e codecov</b>
```
(CondGuai-Acu) CondGuai-Acu $ pipenv install --dev  pytest-cov codecov
```

<b>Publicar projeto no Heroku</b>
```
ALLOWED_HOSTS = [] => ALLOWED_HOSTS = ['*']

Criar o file Procfile para salientar ao heroku como nossa aplicação vai rodar
     => web: gunicorn GuaiAcu.wsgi --log-file -

Instalar o gunicorn (dependencia em produção não é uma pendencia de desenvolvimento)
CondGuai-Acu $ pipenv install gunicorn

Criar um applicação no Heroku e publicar o projeto
CondGuai-Acu $ heroku apps:create condguaiacu
Creating ⬢ condguaiacu... done
https://condguaiacu.herokuapp.com/ | https://git.heroku.com/condguaiacu.git

(CondGuai-Acu) CondGuai-Acu $ git remote -v
heroku  https://git.heroku.com/condguaiacu.git (fetch)
heroku  https://git.heroku.com/condguaiacu.git (push)
origin  git@github.com:jlplautz/CondGuai-Acu.git (fetch)
origin  git@github.com:jlplautz/CondGuai-Acu.git (push)

(CondGuai-Acu) CondGuai-Acu $ heroku config:set DISABLE_COLLECTSTATIC=1
```

<b>Criado app base com django no projeto</b>
```
(CondGuai-Acu) GuaiAcu $ mng startapp base
(CondGuai-Acu) GuaiAcu $ tree
.
├── asgi.py
├── base
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-38.pyc
│   ├── settings.cpython-38.pyc
│   ├── urls.cpython-38.pyc
│   └── wsgi.cpython-38.pyc
├── settings.py
├── urls.py
└── wsgi.py

=> uma view simples consiste em uma função que chamaremos home
def home(request):
    return HttpRequest('Olá Django')

=> Alterar a configuração do file setting.py
   'GuaiAcu.base',

=> fazer o mapeamento da função que se encontra na views
   path('', home),

=> instalar o plugin pytet-django
CondGuai-Acu $ pipenv install -d pytest-django

=> criar o file pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = GuaiAcu.settings
```

<b>Criado app base com django no projeto</b>

```
CondGuai-Acu $ pipenv install --dev 'pytest-cov' codecov


=> Rodar os tests com CODECOV
(CondGuai-Acu) CondGuai-Acu $ pipenv run pytest --cov=GuaiAcu
platform linux -- Python 3.8.0, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
django: settings: GuaiAcu.settings (from ini)
rootdir: /home/plautz/PycharmProjects/CondGuai-Acu, inifile: pytest.ini
plugins: django-3.8.0, cov-2.8.1
collected 1 item                                                                                                                  

GuaiAcu/base/tests/test_home.py .                                                                                           [100%]

----------- coverage: platform linux, python 3.8.0-final-0 -----------
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
GuaiAcu/__init__.py                       0      0   100%
GuaiAcu/asgi.py                           4      4     0%
GuaiAcu/base/__init__.py                  0      0   100%
GuaiAcu/base/admin.py                     0      0   100%
GuaiAcu/base/apps.py                      3      3     0%
GuaiAcu/base/migrations/__init__.py       0      0   100%
GuaiAcu/base/models.py                    0      0   100%
GuaiAcu/base/tests/__init__.py            0      0   100%
GuaiAcu/base/tests/test_home.py           4      0   100%
GuaiAcu/base/views.py                     3      0   100%
GuaiAcu/settings.py                      18      0   100%
GuaiAcu/urls.py                           4      0   100%
GuaiAcu/wsgi.py                           4      4     0%
---------------------------------------------------------
TOTAL                                    40     11    72%

=> Alterar o file pythonapp.yml
    - name: Test with pytest
      run: |
        pipenv run pytest GuaiAcu --cov=GuaiAcu
    - name: Posting Coverage
      env:
        CODECOV_TOKEN: "98f15345-4725-46ec-b7ff-d18a226fdfac"
      run: |
        pipenv run codecov
```

# Instalar a lib python Decouple

```
CondGuai-Acu $ pipenv install 'python-decouple'

=> Alterar a configuração do settings.py DEBUG = True
DEBUG = config('DEBUG', cast=bool)

=> Criar o file .env na raiz do projeto
DEBUG=True

=> Criar o diretório contrib na raiz do projeto
- criar o env-sample dentro do diretório contrib
- DEBUG=FALSE

=> configurar a variavel no heroku 
(CondGuai-Acu) GuaiAcu $ heroku config:set DEBUG=False
Setting DEBUG and restarting ⬢ condguaiacu... done, v13
DEBUG: False

=> Alterar o file pythonapp.yml
    - name: Copying configurations
      run: |
        cp contrib/env-sample .env
```

#  Seting para Secret key 
```
Secret key é utiliazada em vários pontos com necessidade de assinatura criptografa dentro do django
- as sessoes que são arquivos que são enviados ao navegador para ele  manter o usuario logado
- envio de mensagens
- quando vai fazer o reset do password quando estiver o sistema de login
- esta configuração deve ser mantida em segredo, vamos usar o python decouple para setar esta 
  chave secreta no servidor. Para cada instancia possa definir sua chave secreta

=> temos que atualizar o file o env_sample
SECRET_KEY=defina sua chave secreta 

=> Da mesma forma temos que definir no file .env
SECRET_KEY=CHAVE SECRETA

=> Defini a Secret_Key em uma variavel de ambiente para evitar problema com Heroku
(CondGuai-Acu) CondGuai-Acu $ python
Python 3.8.0 (default, Feb  3 2020, 16:24:25) 
[GCC 7.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'***************************************************'
>>> 
(CondGuai-Acu) CondGuai-Acu $ heroku config:set SECRET_KEY='u8ip6ga0kt-6s42ls(=t2dfr4)h28^apidi-%if-jk4vio&6_z'
Setting SECRET_KEY and restarting ⬢ condguaiacu... done, v17
SECRET_KEY: ***************************************************
```