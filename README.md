# CondGuai-Açu
Aplicação para gerenciar condominio do Edifício Colina do Guai-Açu

![Python application](https://github.com/jlplautz/CondGuai-Acu/workflows/Python%20application/badge.svg)
[![Updates](https://pyup.io/repos/github/jlplautz/CondGuai-Acu/shield.svg)](https://pyup.io/repos/github/jlplautz/CondGuai-Acu/)
[![Python 3](https://pyup.io/repos/github/jlplautz/CondGuai-Acu/python-3-shield.svg)](https://pyup.io/repos/github/jlplautz/CondGuai-Acu/)


#Procedimento executado

<b> File pythonapp.yml no github para Continous Integration</b>

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
<b>Diretório do projeto</b<

```
CondGuai-Acu $ tree
.
├── LICENSE
└── README.md
```

<b>Criação do ambiente virtual</b<

```
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
```
<b>Criar o file pipfile.lock e Clear caches</b>
```
(CondGuai-Acu) CondGuai-Acu $ pipenv lock --clear
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Updated Pipfile.lock (db4242)!
```

<b>Instalar a lib flake8</b>
>(CondGuai-Acu) CondGuai-Acu $ pipenv install --dev flake8

<b>criar o arquivo .flake8 na raiz do projeto</b>
```
[flake8]
max-line-length = 120
exclude = .venv
```

<b>criar o arquivo .pyup.yml</b>
```
requirements:
  - Pipfile
  - Pipfile.lock
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

# Instalar lib django
>CondGuai-Acu $ pipenv install django

# Ferramentas basicas do Django (linha de comando)
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

# Publicar projeto no Heroku
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

# Criado app base com django no projeto
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
```

<b>=> uma view simples consiste em uma função que chamaremos home</b>
```
def home(request):
    return HttpRequest('Olá Django')
```

<b>=> Alterar a configuração do file setting.py</b>
>   'GuaiAcu.base',

<b>=> fazer o mapeamento da função que se encontra na views</b>
>   path('', home),

<b>=> instalar o plugin pytet-django</b>
>CondGuai-Acu $ pipenv install -d pytest-django

<b>=> criar o file pytest.ini</b>
```
[pytest]
DJANGO_SETTINGS_MODULE = GuaiAcu.settings
```

# Criado app base com django no projeto

<b>=> Instalar as libs pytest-cov' e codecov</b>
>CondGuai-Acu $ pipenv install --dev 'pytest-cov' codecov

<b>=> Rodar os tests com CODECOV</b>
```
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
```
<b>=> Alterar o file pythonapp.yml</b>
```
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

<b>=> Instalar lib 'python-decouple'</b>
>CondGuai-Acu $ pipenv install 'python-decouple'

<b>=> Alterar a configuração do settings.py DEBUG = True</b>
>DEBUG = config('DEBUG', cast=bool)

<b>=> Criar o file .env na raiz do projeto</b>
>DEBUG=True

<b>=> Criar o diretório contrib na raiz do projeto</b>
> criar o env-sample dentro do diretório contrib
> DEBUG=FALSE

<b>=> configurar a variavel no heroku</b>
```
(CondGuai-Acu) GuaiAcu $ heroku config:set DEBUG=False
Setting DEBUG and restarting ⬢ condguaiacu... done, v13
DEBUG: False
```

<b>=> Alterar o file pythonapp.yml</b>
```
    - name: Copying configurations
      run: |
        cp contrib/env-sample .env
```

#  Seting para Secret key 

<b>Secret key é utiliazada em vários pontos com necessidade de assinatura criptografa dentro do django</b>
> as sessoes que são arquivos que são enviados ao navegador para ele  manter o usuario logado
> envio de mensagens
> quando vai fazer o reset do password quando estiver o sistema de login
> esta configuração deve ser mantida em segredo, vamos usar o python decouple para setar esta 
  chave secreta no servidor. Para cada instancia possa definir sua chave secreta

<b>=> temos que atualizar o file o env_sample</b>
>SECRET_KEY=defina sua chave secreta 

<b>=> Da mesma forma temos que definir no file .env</b>
>SECRET_KEY=CHAVE SECRETA

<b>=> Defini a Secret_Key em uma variavel de ambiente para evitar problema com Heroku</b>
```
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

# Criar dominio e Allowed_Hots

<b>=> no heroku criar o domains</b>
>(CondGuai-Acu) CondGuai-Acu $ heroku domains:add guaiacu.lindart.com.br

<b>=> Para verificar o domains</b>
>(CondGuai-Acu) CondGuai-Acu $ heroku domains

<b>=> No Cloudflare</b>
> criar CNAME record 
> guaiacu.<domain criado no heroku>

<b>=> No settings vamos configurar os dois dominios</b>
> atual => ALLOWED_HOSTS = ['*']
> configurado => ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

<b>=> Heroku configurar ALLOWED_HOSTS</b>
>(CondGuai-Acu) CondGuai-Acu $ heroku config:set ALLOWED_HOSTS='condguaiacu.herokuapp.com, guaiacu.lindart.com.br'

# Endereço de Banco de Dados

<b>No arquivo setting.py esta definido um BD padrão default, como sendo na realidade sqlite3.</b>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

<b> Vamos inserir a variável DATABASE-URL no settings</b> 

>default_db_url = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
>
>parse_database = partial(dj_database_url.parse, conn_max_age=600)
>
>DATABASES = {'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)}

<b>Inserido as libs j-database-url e psycopg2-binary</b>
>CondGuai-Acu $ pipenv install dj-database-url
>
>CondGuai-Acu $ pipenv install psycopg2-binary

# Testes com Postgresql 

<b>Instalar o postgresql no servidor de integraçã continua no file pythonapp.yml</b>
```
    services:
      postgres:
        image: postgres:12.0
```
<b>Adicionar informação no file env-sample para conter:</b>
>DATABASE_URL=postgres://postgres:postgres@localhost/testdb

# Corrigir lingua e Fuso Horário

<b>configurar a língua  (file settings_py)</b>

|   LANGUAGE_CODE  |    TIME_ZONE   |   
|------------------|----------------|
|   'en-us'        |    'UTC'       |

|   LANGUAGE_CODE  |    TIME_ZONE      |   
|------------------|-------------------|
|   'pt-br'        |'America/Sao_Paulo'|

# Comando de Coleta de Arquivos Estáticos

<b>Acessando via linha de comando com o env ativado</b>
>(CondGuai-Acu) CondGuai-Acu $ mng collectstatic

<b>Criar no file settings.py</b>
>STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

<b>Acessando via linha de comando com o env ativado</b>
>(CondGuai-Acu) CondGuai-Acu $ mng collectstatic


```
130 static files copied to '/home/plautz/PycharmProjects/CondGuai-Acu/staticfiles'.
staticfiles
    admin  
        css
        fonts
        img 
        js
```
<b>inserir diretorio staticfiles no gitignore</b>
>mediafiles/
>
>staticfiles/

# Usuario na Amazon e  S3 criação e configuração

<b> inserir no file .env</b>

>AWS_ACCESS_KEY_ID=********************
>
>AWS_SECRET_ACCESS_KEY=****************************************
>
>AWS_STORAGE_BUCKET_NAME=coursedjango

<b> S3 => Scalable Storage in the Cloud</b>

- Criar o  S3 Bucket 
  https://s3.console.aws.amazon.com/s3/home?region=us-east-2
  
- Alterar as Permissions do diretorio Bucket

- Setting => Bucket Policy
  condcguaiacu
 
- Para facilitar a criação da Policy procurar no google => amazon policy generator
step-1  Type pf Policy => S3 Bucket Policy
step-2  Add Statements  
  - Effect Allow
  - Principal (copiar no user summary o User ARN)
  - Actions => All Actions (‘*’)
  - Amozon Resource Name (ARN) => copiar na pagina Bucket policy editor 
  - Generate Policy
  - Copiar o arquivo de policy (formato JSON Document) e voltar para a 
    pagina Bucket Policy para colar a politica. E salvar esta configuração
    
# Instalar a lib django_s3_folder_storage 

>CondGuai-Acu $ pipenv install django_s3_folder_storage

<b>inserir no file settings.py</b>
```
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

# STORAGE CONFIGURATION IN S3 AWS
# ================================================================
if AWS_ACCESS_KEY_ID:
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', }
    AWS_PRELOAD_METADATA = True
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_CUSTOM_DOMAIN = None
#    COLLECTFAST_ENABLED = True
    AWS_DEFAULT_ACL = 'private'

    # Static Assets
    # ===========================================================
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    STATIC_S3_PATH = 'static'
    STATIC_ROOT = f'/{STATIC_S3_PATH}/'
    STATIC_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    # Upload_Media_Filder
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = 'media'
    MEDIA_ROOT = f'/{DEFAULT_S3_PATH}/'
    MEDIA_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{DEFAULT_S3_PATH}/'

    INSTALLED_APPS.append('s3_folder_storage')
    INSTALLED_APPS.append('storages')
```
<b>Atualizando a pagina do Bucket, verificamos que os arquivos foram carregados</b>
>https://s3.console.aws.amazon.com/s3/home?region=sa-east-1

<b>Editar o file env_sample e inserir as configuraçoes do AWS</b>
```
# Configuraçoes do AWS
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
```

# Otimizando Uploads com Collectfast 

<b>setar as variaveis do AWS no servidor</b>
>(CondGuai-Acu) CondGuai-Acu $ heroku config:set AWS_ACCESS_KEY_ID=xyz
>
>ondGuai-Acu) CondGuai-Acu $ heroku config:set AWS_SECRET_ACCESS_KEY=yxz
>
>CondGuai-Acu) CondGuai-Acu $ heroku config:set AWS_STORAGE_BUCKET_NAME=condguaiacu
>
>(CondGuai-Acu) CondGuai-Acu $ heroku config:unset DISABLE_COLLECTSTATIC

<b>Lib Collectfast => minizar o tempo do deployment no servidor</b>
>CondGuai-Acu $ pipenv install Collectfast

<b>add 'collectfast' to your INSTALLED_APPS, before 'django.contrib.staticfiles'</b>
>'collectfast',

<b>Configuração de ambiente de desenvolvimento</b>
>COLLECTFAST_ENABLED = False

<b>STORAGE CONFIGURATION IN S3 AWS</b>
>COLLECTFAST_ENABLED = True

# Sobrescrever a Classe User 

<b>no file models.py</b>
> Criar a class User que herda da class AbstractUser
>
>Fazer as adptações pois a nasse User nao tem atributo username

|   USERNAME_FIELD = 'username' |   USERNAME_FIELD = 'email' |

<b>Criar a classe UserManager herdando  da class UserManager(BaseUsermanager)</b>
>Fazer as adptações pois a nasse User nao tem atributo username

<b>file settings informar ao frameworking qual será a classe base utilizada  como usuario</b>
>AUTH_USER_MODEL = 'base.User'

# Comando makemigrations

<b>como criar e inspecionar migrações de banco de dados</b>
>mng showmigrations
```
(CondGuai-Acu) CondGuai-Acu $ mng makemigrations base
Migrations for 'base':
  GuaiAcu/base/migrations/0001_initial.py
    - Create model User
(CondGuai-Acu) CondGuai-Acu $ docker 
```

# Conexão com Banco e Migrações 

- Menu => DataBase (+) escolher o banco SQLite
- inserir name => guaiacu.sqlite
- navegar no projeto  ate encontrat o file 
  /home/plautz/PycharmProjects/CondGuai-Acu/db.sqlite3
- fazer um Test Connection

<b>aplicar as migraçoes para o banco de dados => mng migrate</b>
>(CondGuai-Acu) CondGuai-Acu $ mng migrate
>(CondGuai-Acu) CondGuai-Acu $ mng showmigrations
>base
 [X] 0001_initial

<b>criar um usuário (superuser) </b>
```
(CondGuai-Acu) CondGuai-Acu $ mng createsuperuser
Endereço de email: admin@admin.com
Password: 
Password (again): 
A senha é muito parecida com endereço de email
Esta senha é muito curta. Ela precisa conter pelo menos 8 caracteres.
Esta senha é muito comum.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

#  Admin do Usuário 
<b>Procedimento para customizar a tabela usuarios</b>

- copiar a class UserAdmin(admin.ModeAdmin)django.contrib.auth.admin
  copiar toda a classe
- remover o i import Group, User
|   from django.contrib.auth.models import Group, User | 
- importar => from pyprg.base.models import User
- remover a class GroupAmin para não sobrescrever
- consertar alguma propriedades da classe UserAdmin

# Aplicando Migrações no Heroku 

<b>Aplicar as migraçoes de forma automatica, adicionar no Procfile file</b>
>release: python manage.py migrate --noinput
> Atenção
>Depois de alterar o Procfile é necessário fazer o commit da branch para atualizar o Heroku

<b>criar super-user no banco do heroku</b>
>(CondGuai-Acu) CondGuai-Acu $ heroku run python manage.py createsuperuser
>
>Endereço de email: admin#admin.com
>Password: 
>Password (again): 

# Backup do Postgresql

<b>comando para backup no heroku</b>
>heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Sao_Paulo'

<b>para conferir o horario dos backups</b>
>(CondGuai-Acu) CondGuai-Acu $ heroku pg:backups:schedules

<b>como verificar os backups</b>
>(CondGuai-Acu) CondGuai-Acu $ heroku pg:backups

<b>como fazer o download dos backups</b>
>(CondGuai-Acu) CondGuai-Acu $ heroku pg:backups:url a001

# Django Debug Toolbar 

<b>instalar a lib django debug toolbar</b>
>CondGuai-Acu $ pipenv install django-debug-toolbar

```
# Configuração Django Debug Toolbar
INTERNAL_IPS = config('INTERNAL_IPS', cast=Csv(), default='127.0.0.1')
if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
```
<b>inserir no arquivo urls.py</b>
```
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
```
<b>inserir a variavel INTERNAL_IPS</b>
>INTERNAL_IPS=127.0.0.1

<b>inserir na views.py content_type=’text/html’</b>
```
def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>', content_type=’text/html’)
```

# Monitorando Erros com Sentry 

<b> Instalar a lib  sentry-sdk

>(CondGuai-Acu) CondGuai-Acu $ pipenv install sentry-sdk

- inserir a variavel de ambiente a chave dsn no file .env
- inserir a varialvel de ambiente a chave dsn no file env-sample
- inserir na file setting.py
```
SENTRY_DSN = config('SENTRY_DSN', default=None)
if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()])
```

# Construir Landpage do projeto

- Twitter Bootstrap e Layoutit 
  https://getbootstrap.com/documentation
  https://www.layoutit.com/

Obs: depois de elaborada a pagina no Layoutit podemos copiar o html ou fazer 
     o download do arwquivo *.zip

# Instalar Arquivos Estáticos Localmente

- copiar a pasta SRC para dentro da app base
- criar um diretorio templates
- criar um diretorio base dentro do templates
- copiar a file index.html para dentro do diretorio templates/base
- e outros steps...

# Template Tag Static

a template tag "static" para fazer seus arquivos estáticos funcionarem na home

- Carregar os arquivos estaticos na aplicação
>(CondGuai-Acu) CondGuai-Acu $ mng collectstatic

- usar as templates tags do Django – que tem a directiva {%  %})
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>

    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <link href="{% static 'css/style.css' %}" rel="stylesheet">
    <script src="{% static 'js/jquery.min.js' %} "></script>
    <script src="{% static 'js/bootstrap.min.js' %} "></script>
    <script src="{% static 'js/scripts.js' %} "></script>
```

# Criação de Função para Testar Conteúdo
```
def test_titulo(client: Client):
    """
    Vamos testar o titulo da homepage e vamos utilizar aquela função assertContains
    Esta função recebe a resposta que foi gerada atraves da  execusão do metodo da views
    e como segundo parametro ela vai se certificar se existe uma string dentro desta
    responta com um formato especifico
    :param client:
    :return:
    """
    resp = client.get('/')
    assert_contains(resp, '<title>Condominio Guai-Açu</title>')
```

# Encapsulando Urls em Apps

- Criar o file urls.py dentro da app base e copiar o conteudo da urls.py da raiz
- definir uma variavel a nivel de modulo chamada app_name
- vamos utilizar a função include presente no pacote django.url.conf 
  onde vamos passar a string pyprg.base.urls.
```  
from django.urls import path
from GuaiAcu.base.views import home
app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
```

# Rodapé

<b>alguns elementos de HTML, CSS e classes do Twitter Bootstrap.</b>

- alterar class = “container-fluid” para class=  “container”
- criar um rodape
```
 <footer class="main-footer mt-5 pt-4">
      <div class="container">
          <div class="row">
              <div class="col text-light">
                  <h3>Entre em Contato</h3>
                  <address>
                      +55 41 99651-4346
                      <br />
                      <a href="mailto:jorge.plautz@gmail.com" class="text-light">jorge.plautz@gmail.com</a>
                  </address>
              </div>
          </div>
      </div>
      <div class="rights pb-4 text-light">
      <div class="container">
          <div class="row">
              <div class="col">
                  {% now 'Y' %} Ed.Colina do Guai-Açu. Todos os direitos reservados.
              </div>
          </div>
      </div>
  </footer>
```
- Inserir no file style.css
```
.main-footer{background-color: #50c93d;}
.rights{background-color: #28a745;}
```
