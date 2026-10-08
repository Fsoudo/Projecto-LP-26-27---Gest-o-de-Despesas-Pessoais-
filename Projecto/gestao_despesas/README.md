# Gestão de Despesas Pessoais

> Projeto desenvolvido no âmbito da UC Linguagens de Programação — IPBeja 2026/2027

---

## Autores

| Nome | Número de Aluno |
|---|---|
| *A preencher* | *A preencher* |
| *A preencher* | *A preencher* |
| *A preencher* | *A preencher* |

---

## Descrição do Problema e da Solução

> *A preencher pelo grupo.*  
> Descrever brevemente o problema (gestão de despesas pessoais) e a solução desenvolvida.

---

## Organização dos Módulos

```
gestao_despesas/
│
├── models/
│   ├── movimento.py       # Classe Movimento — entidade base com validação
│   ├── carteira.py        # Classe Carteira — gere a coleção de movimentos
│   └── exceptions.py      # Exceções personalizadas do domínio
│
├── storage/
│   └── data_manager.py    # Persistência em JSON (salvar/carregar)
│
├── services/
│   └── finance_service.py # Lógica de negócio: filtros, ordenação, cálculos
│
├── ui/
│   └── cli.py             # Interface de linha de comandos
│
├── tests/
│   ├── test_movimentos.py # Testes das classes Movimento e Carteira
│   ├── test_storage.py    # Testes de persistência JSON
│   └── test_service.py    # Testes da lógica de negócio
│
├── data/
│   └── despesas.json      # Ficheiro de dados (gerado automaticamente)
│
├── docs/
│   └── relatorio.md       # Relatório técnico do projeto
│
├── main.py                # Ponto de entrada
├── requirements.txt       # Dependências
└── .gitignore
```

---

## Instalação

```bash
# 1. Clonar o repositório
git clone <url-do-repositório>
cd gestao_despesas

# 2. Criar e ativar ambiente virtual (recomendado)
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt
```

---

## Execução

```bash
python main.py
```

---

## Exemplos de Utilização

> *A preencher pelo grupo com capturas do menu ou exemplos de sessão.*

---

## Executar os Testes

```bash
pytest tests/ -v
```

---

## Dependências

| Biblioteca | Versão | Propósito |
|---|---|---|
| `pytest` | latest | Testes unitários |
| `tabulate` | latest | Formatação de tabelas no terminal |

---

## Limitações Conhecidas

> *A preencher pelo grupo.*

---

*Projeto desenvolvido para fins académicos — IPBeja, 2026/2027.*
