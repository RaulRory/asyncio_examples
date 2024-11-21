# AsyncIO Examples Repository

Este repositório foi criado com o intuito de manter exemplos de código utilizando **asyncIO**, apresentados durante a palestra. Aqui você encontrará códigos organizados em uma estrutura clara, com suporte ao framework **FastAPI**.

---

## Estrutura de Pastas

```plaintext
.
├── asyncio_examples/
│   ├── asyncio_rece_conditions.py
│   ├── asyncio_multiple_taks.py
│   ├── asyncio_example.py
│   ├── asyncio_blocked.py
├── tests/
│   ├── conftest.py  
│   ├── test_examples_api.py
```

---

## Como Configurar o Ambiente

1. Instale o Poetry: Execute o comando abaixo no terminal para instalar o Poetry globalmente:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Verifique a instalação: Após a instalação, confirme se o Poetry está funcionando:

```bash
poetry --version
```

3. Entre no ambiente virtual do Poetry

```bash
poetry shell
```

4. Instale as dependências do projeto:

```bash
poetry install
```

## Executando os exemplos

Para rodar os exemplos que possuem fastAPI execute:

```bash
fastapi dev asyncio_examples/<nome-do-arquivo>
```

Para os exemplos sem o fastAPI execute:

```bash
python3 <nome-do-arquivo>
```

---

## Contribuições
Pull requests são bem-vindos! 😊