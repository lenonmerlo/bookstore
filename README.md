# Bookstore

Bem-vindo à API da Bookstore! Esta API foi desenvolvida usando Django e Django REST Framework e fornece funcionalidades para gerenciar produtos e pedidos de uma livraria.

## Sumário

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Executando o Projeto](#executando-o-projeto)
- [Endpoints](#endpoints)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Instalação

1. Clone o repositório:

```sh
git clone https://github.com/seu-usuario/bookstore.git
cd bookstore
```

Instale as dependências do projeto usando Poetry:

```sh
poetry install
```

## Configuração

Crie um arquivo .env ou env.dev no diretório raiz do projeto com as seguintes variáveis:

plaintext
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=bookstore_dev_db
SQL_USER=bookstore_dev
SQL_PASSWORD=bookstore_dev
SQL_HOST=db
SQL_PORT=5432

Configure o Docker Compose para iniciar os serviços necessários:

```sh
docker-compose up --build
```

## Executando o Projeto

Inicie os serviços Docker:

```sh
docker-compose up -d
```

Acesse a aplicação no navegador:

http://localhost:8000


## Endpoints

A API possui os seguintes endpoints principais:

### Produtos

GET /bookstore/v1/product/ - Lista todos os produtos

POST /bookstore/v1/product/ - Cria um novo produto

GET /bookstore/v1/product/:id/ - Recupera um produto pelo ID

PUT /bookstore/v1/product/:id/ - Atualiza um produto pelo ID

DELETE /bookstore/v1/product/:id/ - Deleta um produto pelo ID

### Pedidos

GET /bookstore/v1/order/ - Lista todos os pedidos

POST /bookstore/v1/order/ - Cria um novo pedido

GET /bookstore/v1/order/:id/ - Recupera um pedido pelo ID

PUT /bookstore/v1/order/:id/ - Atualiza um pedido pelo ID

DELETE /bookstore/v1/order/:id/ - Deleta um pedido pelo ID

## Testes

Execute os testes do projeto usando o comando:

```sh
docker-compose exec web python manage.py test
```

## Contribuição

Se você deseja contribuir com este projeto, por favor siga os passos abaixo:

Faça um fork do repositório

Crie uma branch para sua feature (git checkout -b feature/nova-feature)

Commit suas mudanças (git commit -m 'Adiciona nova feature')

Faça um push para a branch (git push origin feature/nova-feature)

Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
