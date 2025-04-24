# 🚀 API - Sabor Express (FastAPI)

Esta é uma API REST desenvolvida com **FastAPI** para gerenciar restaurantes, permitindo cadastrar, listar, atualizar e remover dados de restaurantes. É uma evolução do projeto `sabor-express`, utilizando recursos modernos como documentação automática via Swagger e execução assíncrona.

---

## 🧰 Tecnologias Utilizadas

- 🐍 Python 3.10+
- ⚡ FastAPI
- 🔄 Uvicorn
- 📄 Pydantic
- 🧪 Testes via Swagger ou ferramentas como Insomnia/Postman

---

## 📂 Estrutura do Projeto

```
api-sabor-express/
├── app/
│   ├── main.py
│   ├── models.py
│   └── routes.py
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/matheusmoyaoliveira/api-sabor-express.git
cd api-sabor-express
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode o servidor com Uvicorn:
```bash
uvicorn app.main:app --reload
```

---

## 📑 Documentação Automática

Após rodar o servidor, acesse no navegador:

- Swagger UI: [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)
- Redoc: [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)

---

## 🎯 Funcionalidades da API

| Método | Rota                | Descrição                          |
|--------|---------------------|------------------------------------|
| GET    | /restaurantes       | Lista todos os restaurantes        |
| POST   | /restaurantes       | Cadastra um novo restaurante       |
| GET    | /restaurantes/{id}  | Detalha um restaurante por ID      |
| PUT    | /restaurantes/{id}  | Atualiza dados de um restaurante   |
| DELETE | /restaurantes/{id}  | Remove um restaurante do sistema   |

---

## 📌 Observações

- Essa API usa estrutura modular com pastas separadas para rotas e modelos.
- Ainda não utiliza banco de dados — os dados são manipulados em memória.
- Ideal para aprendizado sobre APIs REST e FastAPI.

---

## 🧑‍💻 Autor

**Matheus Moya Oliveira**  
🔗 [LinkedIn](https://www.linkedin.com/in/matheusmoyaoliveira/)  
🐙 [GitHub](https://github.com/matheusmoyaoliveira)
