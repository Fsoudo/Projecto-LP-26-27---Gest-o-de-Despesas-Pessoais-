# Relatório Técnico — Gestão de Despesas Pessoais

**Grupo 4 | Linguagens de Programação 2026/2027 | IPBeja**  
**Docente:** Prof. Pedro Moreira

---

## 1. Descrição do Problema

> *A preencher pelo grupo.*  
> Descrever o problema de gestão de despesas pessoais, o contexto de utilização e os objetivos da aplicação desenvolvida.

---

## 2. Arquitetura da Solução

### 2.1 Diagrama de Módulos

> *A preencher pelo grupo.*  
> Apresentar um diagrama (pode ser em texto ASCII ou Mermaid) mostrando as dependências entre módulos.

```
main.py
  └── ui/cli.py
        ├── services/finance_service.py
        │     └── models/carteira.py
        │           └── models/movimento.py
        └── storage/data_manager.py
              └── models/movimento.py
```

### 2.2 Diagrama de Classes

> *A preencher pelo grupo.*  
> Descrever as classes implementadas e as suas relações (atributos e métodos principais).

---

## 3. Decisões de Design

### 3.1 Estruturas de Dados Escolhidas e Justificação

> *A preencher pelo grupo.*  
> Explicar por que razão se usou lista para os movimentos, dicionários para agrupamentos, conjuntos para categorias, etc.

### 3.2 Padrões de POO Utilizados

> *A preencher pelo grupo.*  
> Descrever a hierarquia de classes, encapsulamento e separação de responsabilidades.

### 3.3 Programação Funcional Aplicada

> *A preencher pelo grupo.*  
> Indicar onde e como foram usadas `filter()`, `sorted(key=lambda)` e `map()`, e justificar a sua escolha.

---

## 4. Dificuldades Encontradas e Soluções

> *A preencher pelo grupo.*  
> Descrever os principais problemas encontrados durante o desenvolvimento e como foram resolvidos.

| Dificuldade | Solução Adotada |
|---|---|
| *Exemplo: validação de datas* | *Uso de datetime.strptime com try/except* |

---

## 5. Limitações e Melhorias Futuras

> *A preencher pelo grupo.*  
> Listar limitações conhecidas da solução atual e funcionalidades que poderiam ser adicionadas.

**Limitações:**
- ...

**Melhorias Futuras:**
- ...
