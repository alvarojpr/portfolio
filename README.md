# Portfólio de Análista de Dados – Álvaro J. P. Rodrigues

[![Render](https://img.shields.io/badge/deploy-render-green?style=flat-square)](https://portfolio-bofi.onrender.com/)

Este é meu portfólio online como analista de dados, desenvolvido com Django e hospedado na plataforma Render. Aqui você encontra meus projetos, habilidades, experiência e um pouco sobre mim na área de dados, com foco em coleta, tratamento, análise e visualização.

🔗 **Acesse o portfólio online:**  
👉 [https://portfolio-bofi.onrender.com/](https://portfolio-bofi.onrender.com/)

---

## ✨ Funcionalidades

- Página inicial com informações sobre mim
- Página de projetos com estudos de caso e descrições detalhadas
- Administração via Django Admin para adicionar, editar conteúdos e ver mensagens
- Design responsivo e leve, com uso de HTML, CSS e templates Django

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django 5.2
- **Banco de dados:** PostgreSQL (Render)
- **Frontend:** HTML5, CSS3
- **Deploy:** Render
- **Outros:** Gunicorn, Whitenoise, dj-database-url, python-dotenv

---

## 📂 Estrutura

```bash
portfolio/
├── core/                # Aplicativo principal
│   ├── templates/       # Templates HTML
│   ├── static/          # Arquivos estáticos (CSS, imagens)
│   ├── models.py        # Modelos de dados
├── portfolio/           # Configurações do projeto Django
├── manage.py
├── requirements.txt
└── README.md
