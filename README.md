# django-login-ajax

Test Django Login via Ajax

## Como desenvolver?

* Clone o repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Configure a instância com o `.env`.
* Execute as migrações no banco de dados.
* Crie um usuário
* Rode a aplicação

```
git clone https://github.com/rg3915/django-login-ajax.git
cd django-login-ajax
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ou

* Clone o repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Execute o setup

```
git clone https://github.com/rg3915/django-login-ajax.git
cd django-login-ajax
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```