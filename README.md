# CondGguai-Açu
Aplicação para gerenciar condominio do Edifício Colina do Guai-Açu

<h1>Procedimento executado</h1>

<b>Criar ambiente virtual para o projeto</b>
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

