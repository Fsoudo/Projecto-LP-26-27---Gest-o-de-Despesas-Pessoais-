# Gestor de Despesas Pessoais — versão 0.01 (pseudocódigo)

Projeto de **Linguagens de Programação** – Licenciatura em Engenharia Informática, IPBeja, 2026/2027
**Tema:** Grupo 4 – Gestão de despesas pessoais

> Esta versão (0.01) corresponde à **Fase 1 – Modelação**. A solução está
> descrita em **pseudocódigo**; a implementação em Python 3 é feita na versão
> seguinte, seguindo esta estrutura módulo a módulo.

## Autores

| Nome | Número | Email |
|------|--------|-------|
| Francisco Soudo | _(preencher)_ | fsoudo@gmail.com |
| _(preencher)_ | | |
| _(preencher)_ | | |

## Problema e solução

O objetivo é ajudar o utilizador a controlar o seu orçamento **diário** e **mensal**
registando **receitas** e **despesas**. Cada movimento tem data, tipo, categoria
(alimentação, transporte, lazer, …), descrição e valor. A aplicação permite
registar, consultar, alterar e remover movimentos, filtrá-los e ordená-los, e
apresenta resumos: totais e saldo por mês, despesas por categoria, gasto de um
dia e verificação de um orçamento mensal.

Interface **textual** (menu na consola). Dados guardados num ficheiro **CSV**
(`dados/movimentos.csv`).

A modelação detalhada (estruturas de dados e justificações, funcionalidades,
riscos) está em [docs/FASE1_modelacao.md](docs/FASE1_modelacao.md).

## Organização

| Ficheiro | Conteúdo |
|----------|----------|
| `pseudocodigo/principal.txt` | Algoritmo principal (ponto de entrada) |
| `pseudocodigo/modelo.txt` | Estrutura do movimento (tuplo), tipos e categorias |
| `pseudocodigo/validacao.txt` | Validação de datas, valores, tipos, categorias e descrições |
| `pseudocodigo/operacoes.txt` | CRUD, pesquisa/filtragem, ordenação, totais e orçamento |
| `pseudocodigo/persistencia.txt` | Leitura e escrita do ficheiro CSV |
| `pseudocodigo/interface.txt` | Menu textual e leitura dos dados do utilizador |
| `pseudocodigo/casos_de_teste.txt` | Casos de teste (entrada → resultado esperado) |
| `dados/movimentos.csv` | Dados de exemplo |
| `docs/FASE1_modelacao.md` | Documento de modelação da Fase 1 |

## Convenções do pseudocódigo

| Pseudocódigo | Significado (Python) |
|--------------|----------------------|
| `x <- valor` | atribuição (`x = valor`) |
| `SE … ENTÃO … SENÃO SE … SENÃO … FIM SE` | `if / elif / else` |
| `PARA CADA x EM lista FAZER … FIM PARA` | `for x in lista:` |
| `PARA i DE a ATÉ b FAZER … FIM PARA` | `for i in range(a, b + 1):` |
| `ENQUANTO cond FAZER … FIM ENQUANTO` | `while cond:` |
| `REPETIR … ATÉ cond` | ciclo que executa pelo menos uma vez |
| `ESCOLHER x  CASO … OUTRO … FIM ESCOLHER` | sequência de `if / elif / else` |
| `FUNÇÃO f(...) : tipo … DEVOLVER …` | `def f(...): … return …` |
| `PROCEDIMENTO p(...)` | função sem valor de retorno |
| `( a, b, c )` | tuplo |
| `[ ]`, `ACRESCENTAR x A lista`, `REMOVER lista[i]` | lista, `append`, `del` |
| `LER x` / `ESCREVER …` | `input()` / `print()` |
| `TENTAR … EM CASO DE ERRO … FIM TENTAR` | `try / except` |
| `ASSINALAR ERRO(...)` | `raise ValueError(...)` |
| `NULO`, `VERDADEIRO`, `FALSO` | `None`, `True`, `False` |

## Limitações conhecidas (Fase 1)

- Um só utilizador e um só ficheiro de dados.
- Valores representados como reais (arredondados a 2 casas decimais).
- Os orçamentos (diário/mensal) não são guardados; são pedidos no momento.
- Se o programa for interrompido, as alterações da sessão não são guardadas.

## Roadmap

- **Fase 1 (22/out)** – modelação com listas e tuplos, algoritmos em
  pseudocódigo com ciclos e condições, estrutura do projeto. ✔
- **Fase 2 (17/dez)** – implementação em Python 3 com vários módulos,
  dicionários/conjuntos, classes (`Movimento`, `Carteira`), funções de ordem
  superior, ficheiros CSV/JSON, exceções e testes automáticos (`unittest`).
- **Final (13/jan)** – limpeza do código, relatório e apresentação.
