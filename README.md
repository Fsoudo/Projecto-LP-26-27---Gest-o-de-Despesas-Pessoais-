# Plano de Desenvolvimento do Projeto: Gestão de Despesas Pessoais
**Unidade Curricular:** Linguagens de Programação (2026/2027)  
**Instituição:** Licenciatura em Engenharia Informática — IPBeja  
**Docente:** Prof. Pedro Moreira  
**Tema:** Grupo 4 — Gestão de Despesas Pessoais  

---

## 1. Visão Geral e Enquadramento

O objetivo deste projeto é desenvolver uma aplicação em **Python 3** modular, orientada a objetos, resiliente a erros, testada e persistente, para permitir aos utilizadores gerirem as suas despesas e receitas diárias e mensais.

A implementação privilegia a **qualidade da solução** em detrimento da quantidade de funcionalidades, garantindo código limpo, testado e bem documentado.

### Funcionalidades Mínimas Exigidas
* **CRUD Completo:** Criar, consultar, atualizar e remover receitas e despesas.
* **Categorização e Períodos:** Registo de categorias (ex.: Alimentação, Transporte, Lazer) e acompanhamento mensal/diário.
* **Filtros e Pesquisas:** Filtragem por data, categoria ou intervalo de valores; ordenação por data ou valor.
* **Persistência de Dados:** Guardar e carregar dados via ficheiros **JSON** ou **CSV**.
* **Tratamento de Erros:** Validação estrita de *inputs* com blocos `try/except` e exceções personalizadas.
* **Orientação a Objetos (POO):** Utilização de classes e objetos com separação clara de responsabilidades.
* **Programação Funcional:** Uso de funções de ordem superior (`map`, `filter`, `sorted` com `key=`, `lambda`).
* **Testes Automatizados:** Testes unitários cobrindo as funcionalidades nucleares com `pytest` ou `unittest`.
* **Interface:** Interface de linha de comandos (CLI) interativa e intuitiva.

---

## 2. Estrutura Modular do Projeto

O código deve ser estritamente organizado em módulos funcionais:

```text
gestao_despesas/
│
├── models/
│   ├── __init__.py
│   ├── movimento.py       # Classes: Movimento, Receita, Despesa
│   └── carteira.py        # Classe: Carteira/Orcamento (gestão da coleção de movimentos)
│
├── storage/
│   ├── __init__.py
│   └── data_manager.py    # Leitura e escrita de ficheiros (JSON)
│
├── services/
│   ├── __init__.py
│   └── finance_service.py # Lógica de negócio: resumos, calculo de saldo, estatísticas
│
├── ui/
│   ├── __init__.py
│   └── cli.py             # Interface no terminal (Menus, inputs, formatação de tabelas)
│
├── tests/
│   ├── test_movimentos.py # Testes das classes do modelo
│   ├── test_storage.py    # Testes de leitura/escrita de ficheiros
│   └── test_service.py    # Testes da lógica de cálculo e filtros
│
├── data/
│   └── despesas.json      # Ficheiro de persistência (armazenamento local)
│
├── docs/
│   └── relatorio.md       # Relatório técnico do projeto
│
├── .gitignore
├── README.md              # Documentação oficial do projeto
├── requirements.txt       # Dependências do projeto (ex: pytest, tabulate)
└── main.py                # Ponto de entrada da aplicação
```

---

## 3. Planeamento Cronológico por Entregas

### 📅 Fase 1: Entrega Intermédia 1 (Até 22 de Outubro)
> **Objetivo:** Definir a proposta, modelo de dados inicial, estrutura Git e funções/classes base.  
> ⚠️ **Esta fase inclui uma defesa oral** — todos os membros devem saber explicar o problema e as decisões iniciais.

- [ ] **Documento de Proposta:**
  - Descrever claramente o problema a resolver e o cenário de utilização.
  - Listar as funcionalidades essenciais previstas para a aplicação.
  - Identificar riscos e dificuldades antecipadas (ex: validação de datas, IDs únicos).
  - Justificar a escolha das estruturas de dados a utilizar (listas, tuplos, dicionários).
- [ ] **Configuração do Repositório Git:**
  - Garantir o acesso ao repositório Git fornecido pelo docente.
  - Criar o ficheiro `.gitignore` (para ignorar `__pycache__`, `.pytest_cache`, `.venv`).
  - Adicionar o ficheiro `requirements.txt` básico.
- [ ] **Modelação Orientada a Objetos (`models/movimento.py`):**
  - Implementar a classe base `Movimento` contendo:
    - Atributos: `id` (único), `descricao`, `valor` (float), `categoria`, `data` (YYYY-MM-DD), `tipo` ("RECEITA" / "DESPESA").
  - Criar subclasses ou métodos de validação para garantir que os valores são positivos.
- [ ] **Coleção de Dados Inicial (`models/carteira.py`):**
  - Implementar a classe `Carteira` com uma lista interna para armazenar os movimentos.
  - Métodos base com controlo de fluxo (ciclos e condições): `adicionar_movimento()`, `listar_movimentos()`, `remover_movimento()`.
- [ ] **Skeleton da Aplicação:**
  - Criar o ficheiro `main.py` funcional que inicia o programa.
- [ ] **Registo Git:**
  - Realizar commits periódicos e descritivos por parte de todos os membros do grupo.
- [ ] **Preparação para a Defesa Oral:**
  - Todos os membros devem saber explicar o problema, as decisões de estruturas de dados e os riscos identificados.

---

### 📅 Fase 2: Entrega Intermédia 2 (Até 17 de Dezembro)
> **Objetivo:** Protótipo quase completo, persistência, validações/exceções, programação funcional e testes unitários.  
> ⚠️ **Esta fase inclui uma defesa oral** — o docente pode colocar questões sobre o código e as decisões tomadas.

- [ ] **Módulo de Persistência (`storage/data_manager.py`):**
  - Implementar a serialização/desserialização de dados em **JSON** (`salvar_dados()`, `carregar_dados()`).
  - Tratar exceções de ficheiro inexistente (`FileNotFoundError`) e ficheiro corrompido (`json.JSONDecodeError`).
- [ ] **Tratamento de Exceções e Validações (`ui/cli.py` & `models/`):**
  - Tratar entradas do utilizador (garantir conversão segura de `float` para montantes e validação de datas no formato ISO).
  - Criar exceções personalizadas (ex: `SaldoInvalidoError`, `CategoriaInvalidaError`).
- [ ] **Estruturas de Dados Avançadas:**
  - Usar **dicionários** para agrupamentos (ex: totais de despesas agrupados por categoria).
  - Usar **conjuntos** (`set`) para gerir a lista de categorias únicas disponíveis.
  - Usar **estruturas aninhadas** onde adequado (ex: dicionário de movimentos por mês).
- [ ] **Programação Funcional (`services/finance_service.py`):**
  - Aplicar funções de ordem superior na lógica de filtros e ordenação:
    - `filter()` — ex: filtrar apenas despesas de uma categoria.
    - `sorted(key=lambda m: m.valor)` — ordenar movimentos por valor ou data.
    - `map()` — ex: converter movimentos para formato de exportação.
  - Implementar cálculo do saldo atual, total de receitas e total de despesas do mês.
  - Implementar filtragem por mês/ano, intervalo de datas e categorias.
- [ ] **Testes Automatizados (`tests/`):**
  - Criar testes usando `pytest` para:
    - Adição e remoção de movimentos.
    - Cálculos do saldo e totais por categoria.
    - Gravação e leitura correta de ficheiros.
    - Comportamento com entradas inválidas (exceções esperadas).
- [ ] **Documentação Inicial:**
  - Criar o ficheiro `README.md` preliminar com instruções de instalação e execução.
  - Documentar o código com comentários e docstrings nas funções principais.
- [ ] **Demonstração do Protótipo:**
  - A aplicação deve funcionar em modo quase completo, evidenciando persistência, exceções e testes operacionais.
- [ ] **Preparação para a Defesa Oral:**
  - Cada membro deve saber explicar o seu módulo, as decisões de programação funcional e como os testes foram construídos.
  - Incorporar no plano o feedback recebido do docente.

---

### 📅 Fase 3: Entrega Final (Até 13 de Janeiro)
> **Objetivo:** Refatoração, limpeza de código, documentação final, relatório técnico e preparação para defesa.

- [ ] **Refatoração e Boas Práticas:**
  - Garantir o cumprimento das convenções PEP 8 (nomes de variáveis em snake_case, nomes de classes em PascalCase).
  - Adicionar docstrings em todas as funções, módulos e classes.
  - Eliminar duplicação de lógica entre módulos.
- [ ] **Relatório Técnico (`docs/relatorio.md`):**
  - Documento separado do README, com as seguintes secções:
    - Descrição do problema e objetivos.
    - Diagrama ou descrição da arquitetura de módulos.
    - Decisões de design (estruturas de dados escolhidas e justificação, padrões POO utilizados).
    - Dificuldades encontradas e como foram resolvidas.
    - Limitações conhecidas e possíveis melhorias futuras.
- [ ] **Finalização do Ficheiro `README.md`:**
  - Identificação clara dos autores do grupo.
  - Descrição detalhada do problema e da solução desenvolvida.
  - Instruções detalhadas de instalação e execução num ambiente limpo.
  - **Organização dos módulos** (descrição de cada ficheiro e a sua responsabilidade).
  - Dependências utilizadas e instruções para instalar via `requirements.txt`.
  - Exemplos de utilização / capturas do menu.
  - Instruções de como executar os testes automatizados (`pytest`).
  - Limitações conhecidas.
- [ ] **Validação do Repositório Git:**
  - Confirmar que o histórico de commits reflete o trabalho distribuído ao longo do tempo por todos os membros.
- [ ] **Testes de Compatibilidade Cross-Platform:**
  - Testar a aplicação num ambiente totalmente limpo em **Windows, Linux ou macOS**.
  - Garantir que as instruções do README funcionam num ambiente sem configuração prévia.
- [ ] **Preparação para a Defesa Final:**
  - Garantir que todos os membros sabem explicar as decisões técnicas e partes do código.
  - Preparar uma apresentação sintética da solução desenvolvida.
  - Ser capaz de demonstrar e justificar todas as funcionalidades perante o docente.

---

## 4. Guia de Boas Práticas de Commit (Git)

Os commits devem ser regulares e descritivos. Evite commits gigantescos ou genéricos como "Update" ou "Fix".

**Exemplos de Mensagens de Commit Recomendadas:**
* `feat(models): criar classe Movimento e validadores de valor`
* `feat(storage): implementar leitura e escrita em ficheiro JSON`
* `feat(service): adicionar filtros com funções de ordem superior (filter/sorted)`
* `fix(ui): adicionar bloco try-except na leitura de datas`
* `test(service): adicionar testes unitários para cálculo de saldos`
* `docs: atualizar instructivo de execução no README.md`
* `docs: criar relatório técnico com decisões de design`

---

## 5. Critérios de Qualidade a Garantir

A qualidade da solução é tão importante quanto a quantidade de funcionalidades. Antes de qualquer entrega, verificar:

- [ ] O código é legível: nomes de variáveis e funções são significativos e descritivos?
- [ ] Não existe duplicação de lógica entre módulos (princípio DRY)?
- [ ] A separação de responsabilidades está clara (modelos, lógica, interface, persistência)?
- [ ] As funções de ordem superior são usadas de forma fundamentada e não forçada?
- [ ] A cobertura de testes é suficiente para as funcionalidades nucleares?
- [ ] O programa nunca termina abruptamente com uma exceção não tratada?

---

## 6. Checklist de Verificação Antes da Entrega Final

- [ ] O código executa sem erros em Python 3?
- [ ] A aplicação funciona num ambiente limpo apenas instalando o `requirements.txt`?
- [ ] O CRUD de despesas e receitas está 100% funcional?
- [ ] A persistência em ficheiro JSON funciona ao fechar e reabrir o programa?
- [ ] Todas as entradas inválidas do utilizador são capturadas sem fechar o programa (*crash*)?
- [ ] O conjunto de testes automatizados executa e passa com sucesso (`pytest`)?
- [ ] São utilizadas funções de ordem superior (`filter`, `sorted`, `map`) na lógica de serviço?
- [ ] O ficheiro `README.md` inclui a secção de organização dos módulos?
- [ ] O relatório técnico (`docs/relatorio.md`) está completo?
- [ ] O histórico de commits é regular, distribuído e com mensagens descritivas?
- [ ] A aplicação foi testada num ambiente limpo (Windows/Linux/macOS)?
- [ ] Todos os membros sabem explicar o código e as decisões técnicas?
