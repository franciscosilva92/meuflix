# 🎬 MeuFlix - Catálogo Pessoal de Filmes e Séries

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

Um sistema web completo de catálogo pessoal inspirado na interface da **Netflix**. Desenvolvido para cadastrar, organizar, visualizar detalhes, editar e remover seus filmes e séries favoritos de forma simples e visual.

---

## ✨ Funcionalidades

- **Vitrine Estilo Streaming:** Interface escura (*Dark Mode*) com banner de destaque automático baseado no título com a maior nota cadastrada.
- **Categorização Automática:** Separação visual entre **Filmes** e **Séries** em grades responsivas.
- **Modal Dinâmico de Detalhes:** Ao clicar em qualquer pôster, uma janela sobreposta exibe o banner ampliado, nota de relevância, ano, gênero, sinopse completa e ações rápidas.
- **CRUD Completo:**
  - **Cadastrar:** Adicione novos títulos com URL de pôster, nota (0 a 10), gênero, ano e comentário/sinopse pessoal.
  - **Editar:** Atualize qualquer informação de um título já cadastrado.
  - **Excluir:** Remova títulos do catálogo com confirmação de segurança.

---

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python 3 & Flask
- **Banco de Dados:** SQLite3
- **Front-end:** HTML5, CSS3, Bootstrap 5 & JavaScript (Vanilla)
- **Servidor de Produção:** Gunicorn (configurado para deploy no Render.com)

---

## 📂 Estrutura do Projeto

```text
meu_catalogo_netflix/
├── app.py                 # Rotas da aplicação e conexão com o SQLite
├── catalogo.db            # Banco de dados local (gerado automaticamente)
├── requirements.txt       # Dependências do projeto
├── .gitignore             # Arquivos ignorados pelo Git
├── static/
│   └── style.css          # Estilização personalizada (tema escuro e modal)
└── templates/
    ├── base.html          # Estrutura base HTML e imports
    ├── index.html         # Vitrine principal e Modal dinâmico
    └── form.html          # Formulário de cadastro e edição
```

---

## 🚀 Como Executar Localmente

Siga os passos abaixo para rodar o projeto na sua máquina:

### 1. Clone o repositório
```bash
git clone https://github.com/SEU-USUARIO/meuflix.git
cd meuflix
```

### 2. Crie e ative um ambiente virtual
* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Inicie a aplicação
```bash
python app.py
```

Acesse no seu navegador: **`http://127.0.0.1:5000`**

---

## ☁️ Deploy (Hospedagem)

Este projeto está pronto para hospedagem no **Render.com**:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

> **Nota:** No plano gratuito do Render, o armazenamento de arquivos é temporário. Alterações feitas diretamente online serão resetadas quando o servidor reiniciar por inatividade, mantendo os registros salvos no arquivo `catalogo.db` enviado ao repositório.

---

## 📝 Licença

Este projeto foi desenvolvido para fins de estudo e uso pessoal. Sinta-se à vontade para clonar, modificar e aprimorar!
