# Sistema de Reservas com Django

Esse projeto é um sistema de reservas/sistema de empréstimos desenvolvido como treino com
Django (6.x) e Python (3.13). O objetivo principal foi praticar conceitos essenciais do
desenvolvimento web com Django, modelagem de dados e fluxo completo de CRUD.

Principais objetivos de estudo
-----------------------------
- Estrutura de um projeto Django e organização em apps (`core`, `pessoas`, `itens`, `emprestimos`).
- Views baseadas em função: implementação das views para listar, criar e editar recursos.
- Forms: criação e validação com `forms.py` para entrada de dados do usuário.
- Banco de dados leve: uso do SQLite (`db.sqlite3`) para desenvolvimento e testes locais.
- Arquivo de ambiente: exemplos de configuração com `.env` / `.env.example`.

Recursos e arquitetura do projeto
--------------------------------
- Apps principais:
  - `core`: páginas e layout base do sistema.
  - `pessoas`: CRUD de pessoas/usuários do sistema.
  - `itens`: categorias e itens que podem ser emprestados.
  - `emprestimos`: fluxo de empréstimo/reserva de itens.

Como rodar o projeto
--------------------
1. Criar e ativar um ambiente virtual (recomendado):

	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

2. Instalar dependências:

	```powershell
	pip install -r requirements.txt
	```

3. Configurar variáveis de ambiente: copie `.env.example` para `.env` e ajuste se necessário.

4. Aplicar migrações e criar superusuário:

	```powershell
	python treinodjango\manage.py migrate
	python treinodjango\manage.py createsuperuser
	```

5. Executar servidor de desenvolvimento:

	```powershell
	python treinodjango\manage.py runserver
	```

Executar testes
---------------
Rode os testes das apps com:

```powershell
python treinodjango\manage.py test
```

Boas práticas e próximos passos sugeridos
---------------------------------------
- Adicionar `README` mais detalhado por app, explicando modelos e decisões de design.
- Incluir testes adicionais cobrindo views e formulários.
- Integrar controle de versão para arquivos estáticos e configurar `collectstatic`.
- Substituir SQLite por PostgreSQL para ambientes de produção.

Licença
-------
Este repositório é um projeto de estudo; adapte o uso conforme necessário.
