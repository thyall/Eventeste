# Eventex

Sistema de eventos encomendado pelo welcome to de django

## Como desenvolver?
1. Clone o repositório.
2. Crie o virtualenve com python 3.7
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o.env
6. Execute os testes

```console
git clone https://github.com/thyall/Eventeste.git wttd
cd wttd
python -m venv .wttd
windows--->  activate.bat or .wttd\Scripts\activate  para o linux --->  source .wtdd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

##  Como fazer o deploy?

1. Crie uma instância no heroku.
2. Enve as configurações para o heroku.
3. DEfine uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o servilo de emial.
6. Envie o código para o heroku.

```console
heroku creat minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py` --> Unix
heroku config:set DEBUG=False
#coonfigura email
git push heroku master --force
```
[Link](https://eventex-thyalldgreville.herokuapp.com/)