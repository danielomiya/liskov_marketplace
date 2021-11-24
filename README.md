# Liskov Marketplace

Uma implementação simples baseada no projeto de Engenharia de Software desenvolvido na UPM.

## Grupo

- Daniel Omiya 41995449
- Guilherme Pensutti 41921704
- Hugo Amorim 41991184

## Como rodar o projeto?

    $ python3 -m pip install -r requirements.txt
    $ make run

## _Endpoints_ do projeto

- `POST /api/users`

      $ curl -XPOST http://localhost:3000/api/users \
        -H 'Content-Type: application/json' \
        -d '{"name": "John Doe", "birth_date": "1997-06-17", "cpf_cnpj": "11111111111", "email": "john@doe.com", "phone": "5511913246352", "password": "123"}'

- `POST /api/users/token`

      $ curl -XPOST http://localhost:3000/api/users/token \
        -H 'Content-Type: application/json' \
        -d '{"email": "john@doe.com", "password": "123"}'

## Casos de uso implementados

- Registro do clientes
- Acesso à plataforma

## Melhorias

- atualmente a implementação dos repositórios está em memória, uma melhoria futura é a persistência em banco de dados
- geração de token de acesso ao sistema, em vez de apenas mostrar que o usuário está autenticado

---

_That's all folks!_
