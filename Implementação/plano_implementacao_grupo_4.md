# Plano de Implementação — Gestão de Despesas Pessoais
**Grupo 4 | LP 2026/2027 | IPBeja**

> Este documento é o **roadmap técnico** de implementação. Descreve, por ordem de dependência, o que implementar, em que ficheiro e como — servindo de guia prático de desenvolvimento.

---

## Visão Geral das Dependências entre Módulos

```
main.py
  └── ui/cli.py
        ├── services/finance_service.py
        │     └── models/carteira.py
        │           └── models/movimento.py
        └── storage/data_manager.py
              └── models/movimento.py
```

> **Regra:** implementar sempre da base para o topo. Começar por `movimento.py`, depois `carteira.py`, depois `data_manager.py` e `finance_service.py`, e por último `cli.py` e `main.py`.

---

## 🏃 Sprint 1 — Fase 1 (até 22 de Outubro)

### Passo 1 — Configuração inicial do repositório

**Ficheiros a criar:**

```
gestao_despesas/
├── .gitignore
├── requirements.txt
├── main.py              ← skeleton vazio
├── models/__init__.py
├── storage/__init__.py
├── services/__init__.py
├── ui/__init__.py
├── tests/__init__.py
└── data/               ← pasta vazia (criar um .gitkeep)
```

**`.gitignore`** (conteúdo mínimo):
```gitignore
__pycache__/
*.pyc
.pytest_cache/
.venv/
*.egg-info/
data/despesas.json
```

**`requirements.txt`** (conteúdo inicial):
```
pytest
tabulate
```

**Commit sugerido:** `chore: configurar estrutura inicial do repositório`

---

### Passo 2 — Classe `Movimento` (`models/movimento.py`)

Esta é a classe base de toda a aplicação. Implementar primeiro.

**O que implementar:**
```python
import uuid
from datetime import datetime

class Movimento:
    """Representa um movimento financeiro (receita ou despesa)."""

    TIPOS_VALIDOS = ("RECEITA", "DESPESA")
    CATEGORIAS_VALIDAS = {"Alimentação", "Transporte", "Lazer", "Saúde", "Habitação", "Outros"}

    def __init__(self, descricao: str, valor: float, categoria: str,
                 data: str, tipo: str, id: str = None):
        # Validar e atribuir cada atributo
        # id deve ser str(uuid.uuid4()) se não fornecido
        # valor deve ser > 0, senão lançar ValueError
        # tipo deve ser "RECEITA" ou "DESPESA"
        # data deve estar no formato "YYYY-MM-DD"
        ...

    def to_dict(self) -> dict:
        """Converte o movimento para dicionário (para guardar em JSON)."""
        ...

    @classmethod
    def from_dict(cls, dados: dict) -> "Movimento":
        """Cria um Movimento a partir de um dicionário (ao carregar do JSON)."""
        ...

    def __str__(self) -> str:
        """Representação legível para o terminal."""
        ...
```

**Pontos importantes:**
- `valor` deve ser sempre `float` positivo — lançar `ValueError` se for <= 0
- `data` deve ser validada com `datetime.strptime(data, "%Y-%m-%d")`
- `tipo` deve ser `"RECEITA"` ou `"DESPESA"` — lançar `ValueError` se outro valor
- O `id` deve ser gerado automaticamente com `str(uuid.uuid4())` se não for fornecido

**Commit sugerido:** `feat(models): implementar classe Movimento com validação de atributos`

---

### Passo 3 — Classe `Carteira` (`models/carteira.py`)

Gere a coleção de movimentos em memória.

**O que implementar:**
```python
from models.movimento import Movimento

class Carteira:
    """Gere a coleção de movimentos financeiros em memória."""

    def __init__(self):
        self._movimentos: list = []

    def adicionar_movimento(self, movimento: Movimento) -> None:
        """Adiciona um movimento à lista."""
        ...

    def listar_movimentos(self) -> list:
        """Retorna todos os movimentos."""
        ...

    def obter_por_id(self, id: str):
        """Procura e retorna um movimento pelo seu ID. Retorna None se não encontrado."""
        # Usar ciclo for com condição
        ...

    def remover_movimento(self, id: str) -> bool:
        """Remove um movimento pelo ID. Retorna True se removido, False se não encontrado."""
        ...

    def atualizar_movimento(self, id: str, **campos) -> bool:
        """Atualiza os campos de um movimento existente."""
        ...
```

**Commit sugerido:** `feat(models): implementar classe Carteira com CRUD de movimentos`

---

### Passo 4 — Skeleton do `main.py`

```python
from ui.cli import CLI

def main():
    app = CLI()
    app.iniciar()

if __name__ == "__main__":
    main()
```

**Commit sugerido:** `chore: criar ponto de entrada main.py`

---

### Critério de conclusão da Fase 1

- [ ] `Movimento` pode ser instanciado e validado
- [ ] `Carteira` consegue adicionar, listar e remover movimentos
- [ ] O projeto tem estrutura de pastas completa no Git
- [ ] Pelo menos 2 commits por membro do grupo

---

## 🏃 Sprint 2 — Fase 2, parte A: Persistência e Exceções (Nov)

### Passo 5 — Exceções personalizadas (`models/exceptions.py`)

```python
class ValorInvalidoError(Exception):
    """Lançada quando o valor de um movimento é inválido (ex: negativo ou zero)."""
    pass

class CategoriaInvalidaError(Exception):
    """Lançada quando uma categoria não existe na lista de categorias válidas."""
    pass

class MovimentoNaoEncontradoError(Exception):
    """Lançada quando um movimento com o ID fornecido não existe."""
    pass

class DataInvalidaError(Exception):
    """Lançada quando a data não está no formato YYYY-MM-DD."""
    pass
```

> Atualizar `Movimento.__init__` para lançar estas exceções em vez de `ValueError`.

**Commit sugerido:** `feat(models): criar exceções personalizadas do domínio`

---

### Passo 6 — Módulo de persistência (`storage/data_manager.py`)

**O que implementar:**
```python
import json
import os
from models.movimento import Movimento

CAMINHO_FICHEIRO = "data/despesas.json"

def salvar_dados(movimentos: list) -> None:
    """Serializa a lista de movimentos para JSON e guarda no ficheiro."""
    # Converter cada Movimento para dict com to_dict()
    # Usar json.dump() com indent=2
    # Garantir que a pasta data/ existe com os.makedirs()
    ...

def carregar_dados() -> list:
    """Lê o ficheiro JSON e devolve uma lista de objetos Movimento."""
    # Se o ficheiro não existir (FileNotFoundError), retornar lista vazia
    # Se o JSON estiver corrompido (json.JSONDecodeError), avisar e retornar lista vazia
    # Usar Movimento.from_dict() para reconstruir os objetos
    ...
```

**Commit sugerido:** `feat(storage): implementar leitura e escrita de dados em JSON`

---

## 🏃 Sprint 3 — Fase 2, parte B: Lógica, Funcional e Testes (Nov–Dez)

### Passo 7 — Lógica de negócio (`services/finance_service.py`)

Este módulo deve usar **funções de ordem superior** de forma fundamentada.

**O que implementar:**
```python
from models.movimento import Movimento

# --- Filtros (usar filter() com lambda) ---

def filtrar_por_tipo(movimentos: list, tipo: str) -> list:
    """Filtra movimentos por tipo ('RECEITA' ou 'DESPESA')."""
    return list(filter(lambda m: m.tipo == tipo, movimentos))

def filtrar_por_categoria(movimentos: list, categoria: str) -> list:
    """Filtra movimentos por categoria."""
    return list(filter(lambda m: m.categoria == categoria, movimentos))

def filtrar_por_mes(movimentos: list, ano: int, mes: int) -> list:
    """Filtra movimentos por mês e ano."""
    ...

def filtrar_por_intervalo_valores(movimentos: list, minimo: float, maximo: float) -> list:
    """Filtra movimentos cujo valor está dentro de um intervalo."""
    ...

# --- Ordenação (usar sorted() com key=lambda) ---

def ordenar_por_data(movimentos: list, descendente: bool = False) -> list:
    """Ordena movimentos por data."""
    return sorted(movimentos, key=lambda m: m.data, reverse=descendente)

def ordenar_por_valor(movimentos: list, descendente: bool = True) -> list:
    """Ordena movimentos por valor."""
    return sorted(movimentos, key=lambda m: m.valor, reverse=descendente)

# --- Cálculos ---

def calcular_saldo(movimentos: list) -> float:
    """Calcula o saldo atual (receitas - despesas)."""
    receitas = sum(m.valor for m in movimentos if m.tipo == "RECEITA")
    despesas = sum(m.valor for m in movimentos if m.tipo == "DESPESA")
    return receitas - despesas

def total_por_categoria(movimentos: list) -> dict:
    """Devolve um dicionário {categoria: total_gasto} para despesas."""
    # Usar dicionário para agrupar
    ...

def resumo_mensal(movimentos: list, ano: int, mes: int) -> dict:
    """Devolve resumo do mês: total receitas, total despesas, saldo."""
    ...

# --- Exportação (usar map()) ---

def exportar_para_lista_dicts(movimentos: list) -> list:
    """Converte lista de movimentos para lista de dicionários."""
    return list(map(lambda m: m.to_dict(), movimentos))
```

**Commit sugerido:** `feat(service): implementar filtros e ordenação com funções de ordem superior`

---

### Passo 8 — Interface CLI (`ui/cli.py`)

A CLI deve ser o único ponto de interação com o utilizador.

**Estrutura de menus a implementar:**
```
=== GESTÃO DE DESPESAS PESSOAIS ===
1. Adicionar movimento
2. Listar todos os movimentos
3. Pesquisar / Filtrar
   3.1 Por categoria
   3.2 Por mês/ano
   3.3 Por intervalo de valores
4. Ordenar movimentos
   4.1 Por data
   4.2 Por valor
5. Atualizar movimento
6. Remover movimento
7. Ver resumo / Saldo atual
8. Ver totais por categoria
0. Sair
```

**Padrão de validação de input a aplicar em todos os campos:**
```python
def pedir_float(mensagem: str) -> float:
    """Solicita um número decimal ao utilizador com validação."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Erro: O valor deve ser positivo.")
                continue
            return valor
        except ValueError:
            print("Erro: Introduza um número válido.")

def pedir_data(mensagem: str) -> str:
    """Solicita uma data no formato YYYY-MM-DD com validação."""
    from datetime import datetime
    while True:
        data = input(mensagem)
        try:
            datetime.strptime(data, "%Y-%m-%d")
            return data
        except ValueError:
            print("Erro: Formato inválido. Use YYYY-MM-DD (ex: 2026-10-15).")
```

**Commit sugerido:** `feat(ui): implementar CLI com menus e validação de inputs`

---

### Passo 9 — Testes automatizados (`tests/`)

**`tests/test_movimentos.py`** — o que testar:
```python
# Criar movimento válido com sucesso
# Criar movimento com valor negativo → deve lançar exceção
# Criar movimento com data inválida → deve lançar exceção
# Criar movimento com tipo inválido → deve lançar exceção
# to_dict() e from_dict() são inversos (round-trip)
# Carteira.adicionar_movimento() aumenta o tamanho da lista
# Carteira.remover_movimento() com ID existente retorna True
# Carteira.remover_movimento() com ID inexistente retorna False
```

**`tests/test_storage.py`** — o que testar:
```python
# salvar_dados() cria ficheiro JSON corretamente
# carregar_dados() reconstrói os mesmos movimentos
# carregar_dados() com ficheiro inexistente retorna lista vazia
# carregar_dados() com JSON corrompido retorna lista vazia (sem crash)
```

**`tests/test_service.py`** — o que testar:
```python
# filtrar_por_tipo() retorna apenas RECEITAS ou apenas DESPESAS
# filtrar_por_categoria() retorna apenas da categoria pedida
# ordenar_por_valor() retorna lista ordenada corretamente
# calcular_saldo() = soma receitas - soma despesas
# total_por_categoria() agrupa corretamente por categoria
# resumo_mensal() calcula valores corretos para um mês específico
```

**Comando para correr todos os testes:**
```bash
pytest tests/ -v
```

**Commit sugerido:** `test: adicionar testes unitários para modelos, storage e service`

---

## 🏃 Sprint 4 — Fase 3: Polimento Final (Jan)

### Passo 10 — Refatoração e PEP 8

- [ ] Correr `flake8 .` para identificar violações PEP 8
- [ ] Verificar que todos os nomes de funções estão em `snake_case`
- [ ] Verificar que todos os nomes de classes estão em `PascalCase`
- [ ] Adicionar docstring em todos os módulos, classes e funções

**Commit sugerido:** `refactor: aplicar PEP 8 e adicionar docstrings completas`

---

### Passo 11 — Finalizar `README.md`

O README deve conter **obrigatoriamente** estas secções:

```markdown
# Gestão de Despesas Pessoais

## Autores
## Descrição do Problema e da Solução
## Organização dos Módulos
## Instalação
## Execução
## Exemplos de Utilização
## Executar os Testes
## Dependências
## Limitações Conhecidas
```

---

### Passo 12 — Relatório Técnico (`docs/relatorio.md`)

Documento separado do README com:

```markdown
# Relatório Técnico — Gestão de Despesas Pessoais

## 1. Descrição do Problema
## 2. Arquitetura da Solução
   ### Diagrama de Módulos
   ### Diagrama de Classes
## 3. Decisões de Design
   ### Estruturas de Dados Escolhidas e Justificação
   ### Padrões de POO Utilizados
   ### Programação Funcional Aplicada
## 4. Dificuldades Encontradas e Soluções
## 5. Limitações e Melhorias Futuras
```

**Commit sugerido:** `docs: criar relatório técnico com arquitetura e decisões de design`

---

## 📊 Cronograma Visual

| Semana | Tarefas |
|---|---|
| **8–14 Out** | Passo 1 (repo) + Passo 2 (`Movimento`) |
| **15–22 Out** | Passo 3 (`Carteira`) + Passo 4 (`main.py`) → **Entrega 1** |
| **Nov** | Passo 5 (exceções) + Passo 6 (persistência) + Passo 7 (serviços) |
| **1–7 Dez** | Passo 8 (CLI completa) + Passo 9 (testes) |
| **8–17 Dez** | Integração, testes finais, README preliminar → **Entrega 2** |
| **18 Dez–7 Jan** | Passo 10 (refatoração) + Passo 11 (README) + Passo 12 (relatório) |
| **8–13 Jan** | Testes cross-platform, preparação defesa → **Entrega Final** |

---

## Referências Rápidas

| Conceito | Onde aplicar |
|---|---|
| `uuid.uuid4()` | `models/movimento.py` — gerar IDs únicos |
| `datetime.strptime()` | `models/movimento.py` + `ui/cli.py` — validar datas |
| `json.dump()` / `json.load()` | `storage/data_manager.py` |
| `filter(lambda ...)` | `services/finance_service.py` — filtros |
| `sorted(key=lambda ...)` | `services/finance_service.py` — ordenação |
| `map(lambda ...)` | `services/finance_service.py` — exportação |
| `try/except` | `ui/cli.py` + `storage/data_manager.py` |
| `pytest.raises()` | `tests/` — testar exceções |
| `tabulate()` | `ui/cli.py` — formatar tabelas no terminal |
