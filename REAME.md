# 📚 Pesquisa de Livros

Esse projeto surgiu da ideia de criar um programa para pesquisar livros de forma simples, usando a API pública da Open Library.

A proposta é desenvolver uma interface gráfica onde seja possível pesquisar livros, visualizar as informações encontradas e salvar os resultados para consultar depois.

## Tecnologias utilizadas

- **Python** — linguagem utilizada no projeto.
- **CustomTkinter** — criação da interface gráfica.
- **Requests** — para fazer as consultas à API.
- **SQLite** — para guardar os livros em um banco de dados.
- **Open Library API** — de onde vêm as informações dos livros.

## O que pretendemos desenvolver

- Pesquisa de livros pelo título.
- Exibição dos livros encontrados.
- Armazenamento dos resultados no banco de dados.
- Consulta dos livros salvos anteriormente.
- Filtros e organização dos resultados.
- Exportação dos dados para CSV ou Excel.

## Como o projeto está organizado

```text
projeto_livros/
├── main.py
├── interface/
│   └── tela_principal.py
├── servicos/
│   ├── coletor.py
│   └── analise.py
├── banco/
│   ├── banco_dados.py
│   └── livros.db
├── exportacao/
│   └── exportacao.py
├── requirements.txt
└── README.md
```

Cada arquivo ficará responsável por uma parte do sistema, deixando o código mais organizado e facilitando o desenvolvimento em grupo.

## Como executar

O projeto ainda está em desenvolvimento. Quando estiver pronto para execução, as instruções de instalação e uso serão atualizadas aqui.

## Equipe

Projeto acadêmico desenvolvido em grupo.