# Levantamento de Requisitos — Projeto de Livros

## 1. Objetivo do projeto

Desenvolver um programa em Python que permita pesquisar livros por meio da API pública Open Library, visualizar os resultados, armazenar os dados em um banco de dados e consultar os livros salvos posteriormente.

**API utilizada:** [https://openlibrary.org/search.json](https://openlibrary.org/search.json)

## 2. Requisitos funcionais (RF)

Descrevem as funcionalidades que o sistema deverá oferecer.

- **RF01 — Pesquisar livros:** permitir que o usuário pesquise livros pelo título.
- **RF02 — Consultar API:** buscar informações dos livros na API Open Library.
- **RF03 — Exibir resultados:** mostrar os livros encontrados na interface gráfica.
- **RF04 — Salvar livros:** armazenar os dados dos livros no banco de dados SQLite.
- **RF05 — Evitar duplicidade:** impedir que o mesmo registro de livro seja salvo mais de uma vez, utilizando uma identificação externa quando disponível.
- **RF06 — Consultar livros salvos:** permitir visualizar os livros armazenados anteriormente.
- **RF07 — Analisar resultados:** permitir contar, filtrar ou organizar os livros encontrados.
- **RF08 — Exportar dados:** permitir exportar os livros para arquivos CSV ou Excel.

## 3. Requisitos não funcionais (RNF)

Descrevem características de qualidade e funcionamento do sistema.

- **RNF01 — Linguagem:** o sistema deverá ser desenvolvido em Python.
- **RNF02 — Interface gráfica:** utilizar uma biblioteca como CustomTkinter para criar a interface.
- **RNF03 — Banco de dados:** utilizar SQLite para armazenar os livros localmente.
- **RNF04 — Comunicação:** realizar consultas à API por meio de requisições HTTP.
- **RNF05 — Tratamento de erros:** informar ao usuário quando houver falha de conexão, erro na API ou ausência de resultados.
- **RNF06 — Organização:** manter o código separado em arquivos e pastas de acordo com suas responsabilidades.
- **RNF07 — Persistência:** os livros salvos deverão continuar disponíveis após o fechamento do programa.

## 4. Regras de negócio (RN)

- **RN01:** a pesquisa deverá utilizar o título informado pelo usuário.
- **RN02:** somente os dados retornados pela API deverão ser utilizados como fonte das informações dos livros.
- **RN03:** livros já cadastrados não deverão ser duplicados no banco de dados.
- **RN04:** os resultados deverão apresentar as informações disponíveis, como título, autor e ano de publicação.
- **RN05:** a exportação deverá utilizar os dados disponíveis no sistema.

## 5. Dados dos livros

O sistema poderá armazenar os seguintes campos:

- Identificação externa do livro na API.
- Título.
- Autor ou autores.
- Ano de publicação.

Os campos deverão considerar que algumas informações podem não estar disponíveis na API.

## 6. Estrutura do projeto

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

### Responsabilidade dos arquivos

- **main.py:** iniciar o programa.
- **interface/tela_principal.py:** criar a interface e exibir os resultados.
- **servicos/coletor.py:** consultar a API e organizar os dados recebidos.
- **servicos/analise.py:** filtrar, contar e organizar os resultados.
- **banco/banco_dados.py:** criar tabelas, salvar e consultar livros.
- **banco/livros.db:** armazenar os dados localmente.
- **exportacao/exportacao.py:** exportar os dados para CSV ou Excel.
- **requirements.txt:** listar as bibliotecas externas utilizadas.
- **README.md:** apresentar o projeto e explicar como executá-lo.

## 7. Fluxo principal do sistema

1. O usuário informa o título do livro na interface.
2. O sistema envia a pesquisa para a API Open Library.
3. O coletor recebe e organiza os dados retornados.
4. Os livros são salvos no banco, evitando duplicidades.
5. A interface apresenta os resultados ao usuário.
6. O usuário poderá consultar os livros salvos ou exportar os dados.

## 8. Observação

Este levantamento representa uma proposta inicial. Os requisitos poderão ser ajustados conforme as decisões do grupo e as orientações do professor.
