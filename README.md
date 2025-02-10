# Trabalho Final Teoria da Computação

## Introdução
Este projeto consiste na implementação de uma API RESTful para manipular autômatos utilizando a biblioteca [Automata](https://github.com/caleb531/automata) e o framework [FastAPI](https://fastapi.tiangolo.com/). O objetivo é permitir a criação e manipulação de autômatos finitos, autômatos com pilha e máquinas de Turing.

## Como Executar o Projeto
### 1. **Clonar o Repositório**
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

## 2. **Instalar as dependências**

- pip install automata-lib
- pip install 'automata-lib[visual]'
- pip install "fastapi[standard]"

## 2. Startar a API

- fastapi dev main.py

A API estará disponível em: `http://127.0.0.1:8000`. E a documentação em: `http://127.0.0.1:8000/docs`

## Exemplo de Uso
### Criando um AFD
```json
{
    "type": "DFA",
    "states": ["q0", "q1"],
    "alphabet": ["a", "b"],
    "transitions": {
        "q0": {"a": "q1", "b": "q0"},
        "q1": {"a": "q1", "b": "q0"}
    },
    "initial_state": "q0",
    "accept_states": ["q1"]
}
```

### Testando uma String
```json
{
    "input_string": "abba"
}
```


## Autor
- **Lucas de Oliveira Pereira** - lucas.pereira17@estudante.ufla.br

