# ApplicationIKI

## Para Instalar

Para instalar as dependências do projeto, executar:

```bash
python --version
```

```bash
sudo apt-get install python python3
```


**OBS: É viavel a criação de uma virtualenv para isolar sua maquina ao instalar dependencias da aplicação, para que assim
possamos ter um ambiente voltado ao projeto sem interferir o seu sistema.

Acesse a pasta ApplicationIKI para criarmos a virtualenv:

```bash
cd ApplicationIK
```

Na pasta do projeto, no caso ApplicationIK, executa-se o comando abaixo para cirar sua virtualenv:

```bash
python -m venv NOMEVIRTUALENV
```


Após sua criação execute o comando abaixo para ativar sua virtualenv:

```bash
source NOMEVIRTUALENV/bin/activate
```
**ATENÇÃO USUARIOS DE WINDOWS**

Execute o comando abaixo para ativar sua virtualenv caso esteja utilizando windows:

```bash
NOMEVIRTUALENV\Scripts\activate
```

Após sua ativação, prossiga instalando as dependencias do projeto:

```bash
pip3 install -U Django
```

```bash
pip3 install -r requirements.txt
```

Para criar as _Migrations_:

```bash
python3 manage.py makemigrations
```

Para efetivar as _Migrations_ no banco de dados:

```bash
python3 manage.py migrate
```

Criando SUPERUSER para acesso à aplicação:

```bash
python3 manage.py createsuperuser
```

## Para Executar

```bash
python3 manage.py runserver
```
