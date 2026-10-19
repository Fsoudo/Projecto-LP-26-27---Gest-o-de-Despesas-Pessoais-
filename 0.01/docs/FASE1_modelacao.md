# Fase 1 – Modelação (Entrega intermédia 1 – 22 de outubro)

**Tema:** Grupo 4 – Gestão de despesas pessoais

## 1. Tema e cenário da aplicação

Muitas pessoas (estudantes incluídos) não sabem ao certo quanto gastam por mês
nem em quê. A aplicação **Gestor de Despesas Pessoais** permite ao utilizador
registar todos os seus **movimentos financeiros** — **receitas** (salário, bolsa,
presentes…) e **despesas** (alimentação, transporte, lazer…) — e consultar
resumos que o ajudam a controlar o orçamento **diário** e **mensal**.

Cenário típico: o João recebe a bolsa no início do mês e quer saber, a meio do
mês, quanto já gastou em alimentação e quanto lhe resta de um orçamento de
300 €. Regista cada despesa no momento em que a faz e, quando quiser, pede o
resumo do mês.

Interface: **textual** (menu na consola), o que mantém o foco na lógica do
programa e funciona em Windows, Linux e macOS sem dependências externas.

## 2. Funcionalidades essenciais

| # | Funcionalidade | Tipo |
|---|----------------|------|
| F1 | Registar um movimento (data, tipo, categoria, descrição, valor) | Criação |
| F2 | Listar todos os movimentos | Consulta |
| F3 | Procurar um movimento pelo seu identificador | Consulta |
| F4 | Alterar os dados de um movimento | Atualização |
| F5 | Remover um movimento | Remoção |
| F6 | Filtrar movimentos por tipo, categoria, mês ou intervalo de datas | Pesquisa/filtragem |
| F7 | Ordenar movimentos por data ou por valor | Ordenação |
| F8 | Calcular totais (receitas, despesas e saldo) de um período | Resumo |
| F9 | Calcular o total de despesas por categoria | Resumo |
| F10 | Calcular o gasto de um dia (orçamento diário) | Resumo |
| F11 | Verificar o orçamento mensal (gasto, restante, se foi excedido) | Resumo |
| F12 | Guardar e carregar os movimentos num ficheiro CSV | Persistência |

Todas as entradas do utilizador são **validadas** (data válida, tipo e
categoria existentes, valor numérico positivo).

## 3. Escolha dos tipos de dados e coleções

### Movimento → `tuple`

Cada movimento é representado por um **tuplo** com 6 campos fixos:

```
# (id,  data,         tipo,      categoria,      descricao,         valor)
(1, "2026-10-01", "receita", "bolsa",       "Bolsa de estudo", 350.0)
(2, "2026-10-02", "despesa", "alimentacao", "Supermercado",     42.35)
```

| Campo | Tipo | Justificação |
|-------|-------------|--------------|
| `id` | `int` | Identificador único e sequencial, usado para procurar/alterar/remover |
| `data` | `str` (`AAAA-MM-DD`) | O formato ISO permite comparar e ordenar datas como texto (`"2026-10-01" < "2026-10-15"`) |
| `tipo` | `str` | `"receita"` ou `"despesa"` |
| `categoria` | `str` | Uma das categorias pré-definidas |
| `descricao` | `str` | Texto livre |
| `valor` | `float` | Sempre positivo; o sinal é dado pelo `tipo` |

**Porquê um tuplo?** Um movimento é um registo com estrutura fixa (sempre os
mesmos 6 campos, sempre na mesma ordem). O tuplo é **imutável**, o que evita
alterações acidentais a um campo; para atualizar um movimento cria-se um
**novo tuplo** que substitui o antigo na lista. Para o código ficar legível,
as posições dos campos têm nomes (`ID, DATA, TIPO, CATEGORIA, DESCRICAO, VALOR`)
definidos em `pseudocodigo/modelo.txt`.

### Conjunto de movimentos → `list`

Os movimentos são guardados numa **lista** de tuplos. A lista é **mutável**
(podemos acrescentar, substituir e remover elementos) e mantém a ordem de
inserção — é exatamente o que precisamos para o CRUD.

### Valores fixos → `tuple`

Os tipos (`("receita", "despesa")`) e as categorias de cada tipo são tuplos
constantes: são valores que o programa não deve alterar durante a execução.

### Resultados de funções → `tuple`

Funções que devolvem vários valores devolvem um tuplo, p. ex.
`calcular_totais()` → `(total_receitas, total_despesas, saldo)` e
`totais_por_categoria()` → lista de tuplos `(categoria, total)`.

### Evolução prevista (Fase 2)

Na fase 2 o modelo evolui para **dicionários / classes** (`Movimento`,
`Carteira`), **conjuntos** (p. ex. categorias usadas) e **funções de ordem
superior** (`filter`, `map`, `sorted` com `lambda`). A Fase 1 usa
propositadamente apenas listas e tuplos, ciclos e condições, como pedido no
roadmap.

## 4. Primeiras funções (controlo de fluxo)

Descritas em pseudocódigo em `pseudocodigo/operacoes.txt`, usando ciclos
(`PARA`, `ENQUANTO`, `REPETIR`) e condições (`SE … SENÃO SE … SENÃO`):

- `adicionar_movimento`, `procurar_indice`, `obter_movimento`,
  `atualizar_movimento`, `remover_movimento` (CRUD);
- `filtrar_por_tipo`, `filtrar_por_categoria`, `filtrar_por_mes`,
  `filtrar_por_periodo`, `pesquisar_descricao` (pesquisa/filtragem);
- `ordenar_por_data`, `ordenar_por_valor` (ordenação por inserção, feita à
  mão com ciclos);
- `calcular_totais`, `totais_por_categoria`, `total_do_dia`,
  `verificar_orcamento` (resumos).

O menu (`pseudocodigo/interface.txt`) é um ciclo `ENQUANTO` que só termina
quando o utilizador escolhe "Sair"; a leitura de dados repete o pedido
enquanto o valor introduzido não for válido. Os resultados esperados de cada
função estão em `pseudocodigo/casos_de_teste.txt`.

## 5. Estrutura do projeto (versão 0.01)

```
0.01/
├── pseudocodigo/
│   ├── principal.txt        # algoritmo principal
│   ├── modelo.txt           # estrutura do movimento, tipos e categorias
│   ├── validacao.txt        # validação de datas, valores, tipos, categorias
│   ├── operacoes.txt        # CRUD, filtros, ordenação e resumos
│   ├── persistencia.txt     # leitura/escrita CSV
│   ├── interface.txt        # menu textual
│   └── casos_de_teste.txt   # entradas e resultados esperados
├── dados/movimentos.csv     # dados de exemplo
├── docs/FASE1_modelacao.md  # este documento
└── README.md
```

Na versão seguinte cada ficheiro de pseudocódigo dá origem a um módulo
Python com o mesmo nome (`modelo.py`, `operacoes.py`, …).

## 6. Riscos e dificuldades previstas

- **Arredondamentos com `float`** (p. ex. `0.1 + 0.2`): mitigado arredondando
  os totais a 2 casas decimais; na fase 2 pode avaliar-se o uso de `Decimal`
  ou de cêntimos inteiros.
- **Datas inválidas** (`2026-02-30`): a validação verifica o número de dias de cada mês.
- **Imutabilidade dos tuplos**: atualizar obriga a reconstruir o tuplo — é
  uma decisão consciente, mas na fase 2 pode compensar migrar para classes.
- **Ficheiro de dados corrompido ou inexistente**: a aplicação deve arrancar
  com a lista vazia e avisar o utilizador (tratamento de exceções reforçado
  na fase 2).
- **Trabalho em grupo com Git**: risco de conflitos; mitigado com commits
  pequenos e frequentes e divisão do trabalho por módulos.
