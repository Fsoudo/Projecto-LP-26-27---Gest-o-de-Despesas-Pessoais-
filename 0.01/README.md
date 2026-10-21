# Gestor de Despesas Pessoais — versão 0.01 (pseudocódigo)

Projeto de **Linguagens de Programação** – Licenciatura em Engenharia Informática, IPBeja, 2026/2027
**Tema:** Grupo 4 – Gestão de despesas pessoais

> Esta versão (0.01) corresponde à **Fase 1 – Modelação**. A solução está
> descrita em **pseudocódigo**; a implementação em Python 3 é feita na versão
> seguinte, seguindo esta estrutura módulo a módulo.

## Autores

| Nome | Número | Email |
|------|--------|-------|
| Francisco Soudo | 14060 | 14060@stu.ipbeja.pt |
| João Soares |25961 | 25961@stu.ipbeja.pt|


## Problema e solução

O objetivo é ajudar o utilizador a controlar o seu orçamento **diário** e **mensal**
registando **receitas** e **despesas**. Cada movimento tem data, tipo, categoria
(alimentação, transporte, lazer, …), descrição e valor. A aplicação permite
registar, consultar, alterar e remover movimentos, filtrá-los e ordená-los, e
apresenta resumos: totais e saldo por mês, despesas por categoria, gasto de um
dia e verificação de um orçamento mensal.


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
|__ requirements.txt       # Dependências

```


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

## Pseudocódigo

Dividimos o programa em seis partes, cada uma com a sua responsabilidade. A
ideia é que, na Fase 2, cada parte dê origem a um módulo em Python sem ser
preciso repensar a lógica.

### 1. Algoritmo principal

É por aqui que o programa começa. O algoritmo principal limita-se a chamar o
menu (`executar`, que está na interface). Pusemos o `TENTAR` para que, se o
utilizador carregar em Ctrl+C, o programa termine com uma mensagem em vez de
mostrar um erro.

```
ALGORITMO GestorDeDespesasPessoais

USA interface (executar)

INÍCIO
    TENTAR
        executar()
    EM CASO DE INTERRUPÇÃO (Ctrl+C)
        // o que não foi guardado com a opção 0 perde-se
        ESCREVER "Programa interrompido. As alterações desta sessão não foram guardadas."
    FIM TENTAR
FIM
```

### 2. Modelo de dados

Cada movimento é um **tuplo** com 6 campos e o conjunto de movimentos é uma
**lista** de tuplos. Escolhemos o tuplo porque um movimento, depois de criado,
não deve ser alterado campo a campo: quando o utilizador edita um movimento,
criamos um tuplo novo e trocamo-lo na lista. A lista, essa sim, vai mudando
(acrescentar, remover, substituir).

O valor guarda-se sempre positivo. É o tipo (receita ou despesa) que diz se o
dinheiro entra ou sai.

```
MÓDULO modelo

// Um movimento tem este aspeto:
//
//     (id, data, tipo, categoria, descricao, valor)
//
//   id        -> inteiro, nunca se repete
//   data      -> texto no formato "AAAA-MM-DD"
//   tipo      -> "receita" ou "despesa"
//   categoria -> depende do tipo (ver listas mais abaixo)
//   descricao -> texto livre
//   valor     -> real, sempre maior que 0

// Para não andarmos a escrever m[5] sem saber o que é,
// demos nomes às posições do tuplo
CONSTANTE ID        <- 0
CONSTANTE DATA      <- 1
CONSTANTE TIPO      <- 2
CONSTANTE CATEGORIA <- 3
CONSTANTE DESCRICAO <- 4
CONSTANTE VALOR     <- 5

CONSTANTE CAMPOS <- ("id", "data", "tipo", "categoria", "descricao", "valor")

CONSTANTE RECEITA <- "receita"
CONSTANTE DESPESA <- "despesa"
CONSTANTE TIPOS   <- (RECEITA, DESPESA)

CONSTANTE CATEGORIAS_RECEITA <- ("salario", "bolsa", "presente", "vendas", "outros")
CONSTANTE CATEGORIAS_DESPESA <- ("alimentacao", "transporte", "lazer",
                                 "habitacao", "saude", "educacao", "outros")


FUNÇÃO categorias_do_tipo(tipo) : tuplo
INÍCIO
    SE tipo = RECEITA ENTÃO
        DEVOLVER CATEGORIAS_RECEITA
    SENÃO SE tipo = DESPESA ENTÃO
        DEVOLVER CATEGORIAS_DESPESA
    SENÃO
        DEVOLVER ()          // tipo desconhecido, não tem categorias
    FIM SE
FIM


FUNÇÃO criar_movimento(id, data, tipo, categoria, descricao, valor) : tuplo
INÍCIO
    // arredondamos já aqui para não aparecerem valores como 12.4999999
    DEVOLVER (id, data, tipo, categoria, descricao, ARREDONDAR(valor, 2))
FIM


// Não usamos o tamanho da lista como id porque, depois de se apagar um
// movimento, podíamos acabar com dois ids iguais. Procuramos o maior e somamos 1.
FUNÇÃO proximo_id(movimentos) : inteiro
INÍCIO
    maior <- 0
    PARA CADA movimento EM movimentos FAZER
        SE movimento[ID] > maior ENTÃO
            maior <- movimento[ID]
        FIM SE
    FIM PARA
    DEVOLVER maior + 1
FIM


// Transforma um movimento numa linha de texto para mostrar na tabela
FUNÇÃO formatar_movimento(movimento) : texto
INÍCIO
    SE movimento[TIPO] = RECEITA ENTÃO
        sinal <- "+"
    SENÃO
        sinal <- "-"
    FIM SE
    DEVOLVER movimento[ID] + " | " + movimento[DATA] + " | " + movimento[TIPO]
             + " | " + movimento[CATEGORIA] + " | " + movimento[DESCRICAO]
             + " | " + sinal + movimento[VALOR] (com 2 casas decimais) + " €"
FIM
```

### 3. Validação

Antes de criar ou alterar um movimento verificamos se os dados fazem sentido.
Cada verificação ficou numa função pequena, para depois ser fácil testá-las uma
a uma. A `validar_campos` junta tudo e devolve uma lista com os erros
encontrados; assim o utilizador vê todos os problemas de uma vez, em vez de os
ir descobrindo um de cada vez.

```
MÓDULO validacao

USA modelo (TIPOS, categorias_do_tipo)


// Verifica se o texto é uma data que existe mesmo, no formato AAAA-MM-DD
FUNÇÃO data_valida(texto) : lógico
INÍCIO
    // primeiro vemos se tem a forma certa...
    SE COMPRIMENTO(texto) <> 10 ENTÃO
        DEVOLVER FALSO
    FIM SE
    SE texto[4] <> "-" OU texto[7] <> "-" ENTÃO
        DEVOLVER FALSO
    FIM SE

    ano <- texto[0..3]
    mes <- texto[5..6]
    dia <- texto[8..9]
    SE ano, mes ou dia não forem números ENTÃO
        DEVOLVER FALSO
    FIM SE

    // ...e depois se a data existe no calendário
    SE mes < 1 OU mes > 12 ENTÃO
        DEVOLVER FALSO
    FIM SE
    SE dia < 1 OU dia > DIAS_DO_MES(ano, mes) ENTÃO
        DEVOLVER FALSO       // por exemplo, 2026-02-30 parece bem mas não existe
    FIM SE

    DEVOLVER VERDADEIRO
FIM


// Em Portugal escrevemos "12,50", mas muita gente usa "12.50".
// Aceitamos as duas formas. Se não for um número positivo, devolve NULO.
FUNÇÃO converter_valor(texto) : real ou NULO
INÍCIO
    texto <- REMOVER_ESPACOS(texto)
    texto <- SUBSTITUIR(",", ".", texto)
    SE texto não representa um número ENTÃO
        DEVOLVER NULO
    FIM SE

    valor <- CONVERTER_PARA_REAL(texto)
    SE valor <= 0 ENTÃO
        DEVOLVER NULO
    FIM SE
    DEVOLVER ARREDONDAR(valor, 2)
FIM


FUNÇÃO tipo_valido(tipo) : lógico
INÍCIO
    DEVOLVER tipo PERTENCE A TIPOS
FIM


FUNÇÃO categoria_valida(tipo, categoria) : lógico
INÍCIO
    DEVOLVER categoria PERTENCE A categorias_do_tipo(tipo)
FIM


// A descrição não pode estar vazia nem ter ";",
// porque o ";" é o separador que usamos no ficheiro CSV
FUNÇÃO descricao_valida(descricao) : lógico
INÍCIO
    DEVOLVER REMOVER_ESPACOS(descricao) <> "" E ";" NÃO PERTENCE A descricao
FIM


// Devolve a lista de erros. Se vier vazia, está tudo bem.
FUNÇÃO validar_campos(data, tipo, categoria, descricao, valor) : lista
INÍCIO
    erros <- []

    SE NÃO data_valida(data) ENTÃO
        ACRESCENTAR "Data inválida (use AAAA-MM-DD)." A erros
    FIM SE

    // se o tipo estiver errado nem vale a pena olhar para a categoria
    SE NÃO tipo_valido(tipo) ENTÃO
        ACRESCENTAR "Tipo inválido." A erros
    SENÃO SE NÃO categoria_valida(tipo, categoria) ENTÃO
        ACRESCENTAR "Categoria inválida para o tipo." A erros
    FIM SE

    SE NÃO descricao_valida(descricao) ENTÃO
        ACRESCENTAR "Descrição vazia ou com ';'." A erros
    FIM SE

    SE valor não é número OU valor <= 0 ENTÃO
        ACRESCENTAR "O valor tem de ser positivo." A erros
    FIM SE

    DEVOLVER erros
FIM
```

### 4. Operações

É o módulo com mais trabalho. Todas as funções recebem a lista de movimentos
como primeiro parâmetro e nenhuma delas lê ou escreve no ecrã; isso fica para a
interface. Assim conseguimos testar as contas sem ter de interagir com o menu.

Dividimos as operações em quatro grupos: CRUD, filtros, ordenação e resumos.

```
MÓDULO operacoes

USA modelo, validacao
```

#### 4.1 CRUD (criar, consultar, alterar e remover)

```
FUNÇÃO adicionar_movimento(movimentos, data, tipo, categoria, descricao, valor) : tuplo
INÍCIO
    erros <- validar_campos(data, tipo, categoria, descricao, valor)
    SE erros não está vazia ENTÃO
        ASSINALAR ERRO(erros)
    FIM SE

    novo_id <- proximo_id(movimentos)
    movimento <- criar_movimento(novo_id, data, tipo, categoria, descricao, valor)
    ACRESCENTAR movimento A movimentos
    DEVOLVER movimento
FIM


// Diz em que posição da lista está o movimento com aquele id.
// Se não existir, devolve -1.
FUNÇÃO procurar_indice(movimentos, id) : inteiro
INÍCIO
    PARA i DE 0 ATÉ COMPRIMENTO(movimentos) - 1 FAZER
        SE movimentos[i][ID] = id ENTÃO
            DEVOLVER i
        FIM SE
    FIM PARA
    DEVOLVER -1
FIM


FUNÇÃO obter_movimento(movimentos, id) : tuplo ou NULO
INÍCIO
    i <- procurar_indice(movimentos, id)
    SE i = -1 ENTÃO
        DEVOLVER NULO
    FIM SE
    DEVOLVER movimentos[i]
FIM


// Os campos que vierem a NULO ficam como estavam.
// Como não dá para mudar um tuplo, construímos um novo e pomo-lo no lugar do antigo.
FUNÇÃO atualizar_movimento(movimentos, id, data, tipo, categoria, descricao, valor) : tuplo
INÍCIO
    i <- procurar_indice(movimentos, id)
    SE i = -1 ENTÃO
        ASSINALAR ERRO("Não existe nenhum movimento com esse id.")
    FIM SE

    antigo <- movimentos[i]
    SE data      = NULO ENTÃO data      <- antigo[DATA]      FIM SE
    SE tipo      = NULO ENTÃO tipo      <- antigo[TIPO]      FIM SE
    SE categoria = NULO ENTÃO categoria <- antigo[CATEGORIA] FIM SE
    SE descricao = NULO ENTÃO descricao <- antigo[DESCRICAO] FIM SE
    SE valor     = NULO ENTÃO valor     <- antigo[VALOR]     FIM SE

    // validamos outra vez porque a mistura de dados novos e antigos
    // pode não fazer sentido (ex.: mudar o tipo e manter a categoria)
    erros <- validar_campos(data, tipo, categoria, descricao, valor)
    SE erros não está vazia ENTÃO
        ASSINALAR ERRO(erros)
    FIM SE

    novo <- criar_movimento(id, data, tipo, categoria, descricao, valor)
    movimentos[i] <- novo
    DEVOLVER novo
FIM


FUNÇÃO remover_movimento(movimentos, id) : lógico
INÍCIO
    i <- procurar_indice(movimentos, id)
    SE i = -1 ENTÃO
        DEVOLVER FALSO       // não havia nada para remover
    FIM SE
    REMOVER movimentos[i]
    DEVOLVER VERDADEIRO
FIM
```

#### 4.2 Pesquisa e filtros

Os filtros seguem todos a mesma receita: percorrer a lista e copiar para uma
lista nova os movimentos que interessam. A lista original nunca é alterada.

```
FUNÇÃO filtrar_por_tipo(movimentos, tipo) : lista
INÍCIO
    resultado <- []
    PARA CADA m EM movimentos FAZER
        SE m[TIPO] = tipo ENTÃO
            ACRESCENTAR m A resultado
        FIM SE
    FIM PARA
    DEVOLVER resultado
FIM


FUNÇÃO filtrar_por_categoria(movimentos, categoria) : lista
INÍCIO
    resultado <- []
    PARA CADA m EM movimentos FAZER
        SE m[CATEGORIA] = categoria ENTÃO
            ACRESCENTAR m A resultado
        FIM SE
    FIM PARA
    DEVOLVER resultado
FIM


// Como as datas estão no formato AAAA-MM-DD, comparar como texto
// dá a mesma ordem que comparar datas, por isso não é preciso convertê-las
FUNÇÃO filtrar_por_periodo(movimentos, data_inicio, data_fim) : lista
INÍCIO
    resultado <- []
    PARA CADA m EM movimentos FAZER
        SE data_inicio <= m[DATA] E m[DATA] <= data_fim ENTÃO
            ACRESCENTAR m A resultado
        FIM SE
    FIM PARA
    DEVOLVER resultado
FIM


FUNÇÃO filtrar_por_mes(movimentos, ano, mes) : lista
INÍCIO
    // para outubro de 2026 o prefixo fica "2026-10"
    prefixo <- ano (com 4 dígitos) + "-" + mes (com 2 dígitos)
    resultado <- []
    PARA CADA m EM movimentos FAZER
        SE m[DATA] COMEÇA POR prefixo ENTÃO
            ACRESCENTAR m A resultado
        FIM SE
    FIM PARA
    DEVOLVER resultado
FIM


// Procura um pedaço de texto na descrição.
// Passamos tudo a minúsculas para "Pingo Doce" e "pingo doce" darem o mesmo.
FUNÇÃO pesquisar_descricao(movimentos, texto) : lista
INÍCIO
    texto <- MINUSCULAS(texto)
    resultado <- []
    PARA CADA m EM movimentos FAZER
        SE texto ESTÁ CONTIDO EM MINUSCULAS(m[DESCRICAO]) ENTÃO
            ACRESCENTAR m A resultado
        FIM SE
    FIM PARA
    DEVOLVER resultado
FIM
```

#### 4.3 Ordenação

Usámos a ordenação por inserção por ser simples e fácil de seguir à mão.
Trabalhamos sempre sobre uma cópia, para não baralhar a lista original. Em vez
de escrever uma ordenação para cada campo, a `ordenar_por_campo` recebe a
posição do campo no tuplo (`DATA`, `VALOR`, …).

```
FUNÇÃO ordenar_por_campo(movimentos, campo, decrescente) : lista
INÍCIO
    ordenada <- CÓPIA(movimentos)

    PARA i DE 1 ATÉ COMPRIMENTO(ordenada) - 1 FAZER
        atual <- ordenada[i]
        j <- i - 1
        // empurra para a direita os que devem ficar depois do "atual"
        ENQUANTO j >= 0 E vem_depois(ordenada[j][campo], atual[campo], decrescente) FAZER
            ordenada[j + 1] <- ordenada[j]
            j <- j - 1
        FIM ENQUANTO
        ordenada[j + 1] <- atual
    FIM PARA

    DEVOLVER ordenada
FIM


// Diz se "a" deve aparecer depois de "b", conforme a ordem pedida
FUNÇÃO vem_depois(a, b, decrescente) : lógico
INÍCIO
    SE decrescente ENTÃO
        DEVOLVER a < b
    SENÃO
        DEVOLVER a > b
    FIM SE
FIM


// Atalhos, para a interface ficar mais legível
FUNÇÃO ordenar_por_data(movimentos, decrescente) : lista
INÍCIO
    DEVOLVER ordenar_por_campo(movimentos, DATA, decrescente)
FIM

FUNÇÃO ordenar_por_valor(movimentos, decrescente) : lista
INÍCIO
    DEVOLVER ordenar_por_campo(movimentos, VALOR, decrescente)
FIM
```

#### 4.4 Resumos e orçamento

Estas funções respondem às perguntas que o utilizador realmente faz: quanto
ganhei e quanto gastei, onde gastei mais, quanto gastei hoje e se já passei o
orçamento do mês.

```
FUNÇÃO calcular_totais(movimentos) : tuplo (receitas, despesas, saldo)
INÍCIO
    receitas <- 0
    despesas <- 0
    PARA CADA m EM movimentos FAZER
        SE m[TIPO] = RECEITA ENTÃO
            receitas <- receitas + m[VALOR]
        SENÃO
            despesas <- despesas + m[VALOR]
        FIM SE
    FIM PARA
    saldo <- receitas - despesas
    DEVOLVER (ARREDONDAR(receitas, 2), ARREDONDAR(despesas, 2), ARREDONDAR(saldo, 2))
FIM


// Soma o que foi gasto (ou recebido) em cada categoria.
// Categorias a zero não aparecem; o resultado vem do maior para o menor.
FUNÇÃO totais_por_categoria(movimentos, tipo) : lista de tuplos (categoria, total)
INÍCIO
    resultado <- []
    PARA CADA categoria EM categorias_do_tipo(tipo) FAZER
        total <- 0
        PARA CADA m EM movimentos FAZER
            SE m[TIPO] = tipo E m[CATEGORIA] = categoria ENTÃO
                total <- total + m[VALOR]
            FIM SE
        FIM PARA
        SE total > 0 ENTÃO
            ACRESCENTAR (categoria, ARREDONDAR(total, 2)) A resultado
        FIM SE
    FIM PARA

    // ordenamos outra vez por inserção, agora pelo total (posição 1), do maior para o menor
    PARA i DE 1 ATÉ COMPRIMENTO(resultado) - 1 FAZER
        atual <- resultado[i]
        j <- i - 1
        ENQUANTO j >= 0 E resultado[j][1] < atual[1] FAZER
            resultado[j + 1] <- resultado[j]
            j <- j - 1
        FIM ENQUANTO
        resultado[j + 1] <- atual
    FIM PARA

    DEVOLVER resultado
FIM


// Quanto se gastou num dia (só despesas). Serve para o orçamento diário.
FUNÇÃO total_do_dia(movimentos, data) : real
INÍCIO
    total <- 0
    PARA CADA m EM movimentos FAZER
        SE m[DATA] = data E m[TIPO] = DESPESA ENTÃO
            total <- total + m[VALOR]
        FIM SE
    FIM PARA
    DEVOLVER ARREDONDAR(total, 2)
FIM


FUNÇÃO verificar_orcamento(movimentos, ano, mes, limite)
       : tuplo (gasto, restante, percentagem, excedido)
INÍCIO
    do_mes <- filtrar_por_mes(movimentos, ano, mes)

    // dos três totais só nos interessa o das despesas
    (_, gasto, _) <- calcular_totais(do_mes)

    restante <- limite - gasto
    SE limite > 0 ENTÃO
        percentagem <- gasto / limite * 100
    SENÃO
        percentagem <- 0     // para não dividir por zero
    FIM SE
    excedido <- gasto > limite

    DEVOLVER (gasto, restante, percentagem, excedido)
FIM
```

### 5. Persistência (ficheiro CSV)

Os movimentos ficam guardados no ficheiro `dados/movimentos.csv`, uma linha por
movimento e com os campos separados por `;`. A primeira linha é o cabeçalho.

Ao carregar, se o ficheiro ainda não existir (por exemplo, na primeira vez que
se usa o programa) começamos com a lista vazia. Se alguma linha estiver
estragada, é ignorada, para o programa não deixar de arrancar por causa disso.

```
MÓDULO persistencia

USA modelo (CAMPOS, criar_movimento)

CONSTANTE FICHEIRO_PADRAO <- "dados/movimentos.csv"


PROCEDIMENTO guardar_movimentos(movimentos, caminho)
INÍCIO
    ABRIR caminho PARA ESCRITA COMO ficheiro
    ESCREVER LINHA JUNTAR(CAMPOS, ";") EM ficheiro     // cabeçalho
    PARA CADA m EM movimentos FAZER
        ESCREVER LINHA JUNTAR(m, ";") EM ficheiro
    FIM PARA
    FECHAR ficheiro
FIM


FUNÇÃO carregar_movimentos(caminho) : lista
INÍCIO
    movimentos <- []
    SE caminho NÃO EXISTE ENTÃO
        DEVOLVER movimentos
    FIM SE

    ABRIR caminho PARA LEITURA COMO ficheiro
    LER LINHA DE ficheiro                               // o cabeçalho não interessa
    ENQUANTO NÃO FIM_DE_FICHEIRO(ficheiro) FAZER
        campos <- DIVIDIR(LER LINHA DE ficheiro, ";")

        // só aproveitamos linhas com os 6 campos e com id e valor numéricos
        SE COMPRIMENTO(campos) = 6 E campos[0] é inteiro E campos[5] é número ENTÃO
            m <- criar_movimento(INTEIRO(campos[0]), campos[1], campos[2],
                                 campos[3], campos[4], REAL(campos[5]))
            ACRESCENTAR m A movimentos
        FIM SE
    FIM ENQUANTO
    FECHAR ficheiro

    DEVOLVER movimentos
FIM
```

### 6. Interface (menu na consola)

É a única parte do programa que fala com o utilizador. As funções de leitura
insistem até a resposta ser válida, por isso o resto do programa recebe sempre
dados em condições.

```
MÓDULO interface

USA modelo, validacao, operacoes, persistencia
```

#### 6.1 Ler dados do teclado

Todas seguem o mesmo esquema: pedir, validar, e se estiver mal avisar e voltar
a pedir. O parâmetro `permitir_vazio` serve para a opção de alterar, onde
carregar só em Enter quer dizer "deixa como está".

```
FUNÇÃO ler_data(mensagem, permitir_vazio) : texto ou NULO
INÍCIO
    REPETIR
        ESCREVER mensagem
        LER texto
        SE texto = "" ENTÃO
            SE permitir_vazio ENTÃO
                DEVOLVER NULO
            FIM SE
            DEVOLVER DATA_DE_HOJE()      // Enter sem nada = hoje
        FIM SE
        SE data_valida(texto) ENTÃO
            DEVOLVER texto
        FIM SE
        ESCREVER "Data inválida. Use AAAA-MM-DD."
    ATÉ FALSO       // nunca acaba por aqui, sai sempre por um DEVOLVER
FIM


// Mostra as opções numeradas. O utilizador pode escrever o número ou o nome.
FUNÇÃO ler_opcao(mensagem, opcoes, permitir_vazio) : texto ou NULO
INÍCIO
    PARA n DE 1 ATÉ COMPRIMENTO(opcoes) FAZER
        ESCREVER n + ". " + opcoes[n - 1]
    FIM PARA

    REPETIR
        ESCREVER mensagem
        LER texto
        SE texto = "" E permitir_vazio ENTÃO
            DEVOLVER NULO
        FIM SE
        SE texto é número E 1 <= texto <= COMPRIMENTO(opcoes) ENTÃO
            DEVOLVER opcoes[texto - 1]
        FIM SE
        SE texto PERTENCE A opcoes ENTÃO
            DEVOLVER texto
        FIM SE
        ESCREVER "Opção inválida."
    ATÉ FALSO
FIM


FUNÇÃO ler_valor(mensagem, permitir_vazio) : real ou NULO
INÍCIO
    REPETIR
        ESCREVER mensagem
        LER texto
        SE texto = "" E permitir_vazio ENTÃO
            DEVOLVER NULO
        FIM SE
        valor <- converter_valor(texto)
        SE valor <> NULO ENTÃO
            DEVOLVER valor
        FIM SE
        ESCREVER "Valor inválido. Introduza um número positivo (ex.: 12,50)."
    ATÉ FALSO
FIM

// ler_texto, ler_inteiro e ler_ano_mes fazem exatamente o mesmo,
// só muda a validação, por isso não as repetimos aqui.
```

#### 6.2 Mostrar movimentos

```
PROCEDIMENTO mostrar_movimentos(movimentos)
INÍCIO
    SE movimentos está vazia ENTÃO
        ESCREVER "(sem movimentos)"
    SENÃO
        ESCREVER cabeçalho da tabela
        PARA CADA m EM movimentos FAZER
            ESCREVER formatar_movimento(m)
        FIM PARA
        // no fim da tabela mostramos logo os totais do que foi listado
        (receitas, despesas, saldo) <- calcular_totais(movimentos)
        ESCREVER "Receitas: ", receitas, "  Despesas: ", despesas, "  Saldo: ", saldo
    FIM SE
FIM
```

#### 6.3 Ações do menu

Cada opção do menu tem o seu procedimento. Aqui só se pedem os dados e se
mostram os resultados; as contas são feitas pelas funções do módulo `operacoes`.

```
PROCEDIMENTO acao_registar(movimentos)
INÍCIO
    data      <- ler_data("Data (Enter = hoje): ", FALSO)
    tipo      <- ler_opcao("Tipo: ", TIPOS, FALSO)
    categoria <- ler_opcao("Categoria: ", categorias_do_tipo(tipo), FALSO)
    descricao <- ler_texto("Descrição: ", FALSO)
    valor     <- ler_valor("Valor (€): ", FALSO)

    m <- adicionar_movimento(movimentos, data, tipo, categoria, descricao, valor)
    ESCREVER "Movimento registado com o id ", m[ID]
FIM


PROCEDIMENTO acao_listar(movimentos)
INÍCIO
    mostrar_movimentos(ordenar_por_data(movimentos, FALSO))
FIM


PROCEDIMENTO acao_alterar(movimentos)
INÍCIO
    id <- ler_inteiro("Id do movimento: ")
    m <- obter_movimento(movimentos, id)
    SE m = NULO ENTÃO
        ESCREVER "Não existe nenhum movimento com esse id."
        SAIR
    FIM SE

    ESCREVER formatar_movimento(m)
    ESCREVER "(Enter para manter o valor atual)"

    data <- ler_data("Nova data: ", VERDADEIRO)
    tipo <- ler_opcao("Novo tipo: ", TIPOS, VERDADEIRO)

    SE tipo = NULO ENTÃO
        tipo_final <- m[TIPO]
    SENÃO
        tipo_final <- tipo
    FIM SE

    // se o tipo mudou, a categoria antiga pode já não servir
    // (ex.: "salario" numa despesa), por isso aí é obrigatório escolher outra
    categoria <- ler_opcao("Nova categoria: ", categorias_do_tipo(tipo_final), tipo = NULO)
    descricao <- ler_texto("Nova descrição: ", VERDADEIRO)
    valor     <- ler_valor("Novo valor (€): ", VERDADEIRO)

    TENTAR
        novo <- atualizar_movimento(movimentos, id, data, tipo, categoria, descricao, valor)
        ESCREVER "Atualizado: ", formatar_movimento(novo)
    EM CASO DE ERRO e
        ESCREVER "Não foi possível alterar: ", e
    FIM TENTAR
FIM


PROCEDIMENTO acao_remover(movimentos)
INÍCIO
    id <- ler_inteiro("Id do movimento: ")
    m <- obter_movimento(movimentos, id)
    SE m = NULO ENTÃO
        ESCREVER "Não existe nenhum movimento com esse id."
        SAIR
    FIM SE

    // pedimos confirmação, porque apagar não tem volta
    ESCREVER formatar_movimento(m)
    ESCREVER "Tem a certeza? (s/n)"
    LER resposta
    SE resposta = "s" ENTÃO
        remover_movimento(movimentos, id)
        ESCREVER "Movimento removido."
    SENÃO
        ESCREVER "Operação cancelada."
    FIM SE
FIM


PROCEDIMENTO acao_filtrar(movimentos)
INÍCIO
    ESCREVER "1-Tipo  2-Categoria  3-Mês  4-Intervalo de datas  5-Texto"
    LER escolha

    ESCOLHER escolha
        CASO "1":
            tipo <- ler_opcao("Tipo: ", TIPOS, FALSO)
            resultado <- filtrar_por_tipo(movimentos, tipo)
        CASO "2":
            // "outros" existe nos dois tipos, por isso pedimos também o tipo
            tipo <- ler_opcao("Tipo: ", TIPOS, FALSO)
            categoria <- ler_opcao("Categoria: ", categorias_do_tipo(tipo), FALSO)
            resultado <- filtrar_por_tipo(filtrar_por_categoria(movimentos, categoria), tipo)
        CASO "3":
            (ano, mes) <- ler_ano_mes()
            resultado <- filtrar_por_mes(movimentos, ano, mes)
        CASO "4":
            inicio <- ler_data("Data inicial: ", FALSO)
            fim    <- ler_data("Data final: ", FALSO)
            resultado <- filtrar_por_periodo(movimentos, inicio, fim)
        CASO "5":
            texto <- ler_texto("Texto a procurar: ", FALSO)
            resultado <- pesquisar_descricao(movimentos, texto)
        OUTRO:
            ESCREVER "Opção inválida."
            SAIR
    FIM ESCOLHER

    mostrar_movimentos(ordenar_por_data(resultado, FALSO))
FIM


PROCEDIMENTO acao_ordenar(movimentos)
INÍCIO
    ESCREVER "1-Data asc  2-Data desc  3-Valor asc  4-Valor desc"
    LER escolha
    ESCOLHER escolha
        CASO "1": mostrar_movimentos(ordenar_por_data(movimentos, FALSO))
        CASO "2": mostrar_movimentos(ordenar_por_data(movimentos, VERDADEIRO))
        CASO "3": mostrar_movimentos(ordenar_por_valor(movimentos, FALSO))
        CASO "4": mostrar_movimentos(ordenar_por_valor(movimentos, VERDADEIRO))
        OUTRO:    ESCREVER "Opção inválida."
    FIM ESCOLHER
FIM


PROCEDIMENTO acao_resumo_mes(movimentos)
INÍCIO
    (ano, mes) <- ler_ano_mes()
    do_mes <- filtrar_por_mes(movimentos, ano, mes)
    (receitas, despesas, saldo) <- calcular_totais(do_mes)
    ESCREVER receitas, despesas, saldo

    // uma "barra" de # por categoria: cada # vale 5% das despesas do mês
    PARA CADA (categoria, total) EM totais_por_categoria(do_mes, DESPESA) FAZER
        percentagem <- total / despesas * 100
        ESCREVER categoria, total, percentagem, REPETIR("#", percentagem / 5)
    FIM PARA
FIM


PROCEDIMENTO acao_gasto_dia(movimentos)
INÍCIO
    data <- ler_data("Data (Enter = hoje): ", FALSO)
    total <- total_do_dia(movimentos, data)
    ESCREVER "Total gasto em ", data, ": ", total

    // o orçamento diário é opcional
    limite <- ler_valor("Orçamento diário (Enter para ignorar): ", VERDADEIRO)
    SE limite <> NULO ENTÃO
        SE total > limite ENTÃO
            ESCREVER "Excedeu o orçamento diário em ", total - limite
        SENÃO
            ESCREVER "Ainda pode gastar ", limite - total
        FIM SE
    FIM SE
FIM


PROCEDIMENTO acao_orcamento(movimentos)
INÍCIO
    (ano, mes) <- ler_ano_mes()
    limite <- ler_valor("Orçamento para o mês (€): ", FALSO)
    (gasto, restante, percentagem, excedido) <- verificar_orcamento(movimentos, ano, mes, limite)

    ESCREVER "Gasto: ", gasto, " de ", limite, " (", percentagem, "%)"
    SE excedido ENTÃO
        ESCREVER "ORÇAMENTO EXCEDIDO em ", -restante
    SENÃO SE percentagem >= 80 ENTÃO
        // um aviso antes de passar o limite
        ESCREVER "Atenção: já usou mais de 80%. Restam ", restante
    SENÃO
        ESCREVER "Restam ", restante
    FIM SE
FIM
```

#### 6.4 Ciclo principal

Carrega os dados, mostra o menu e repete até o utilizador escolher sair. Os
dados só são escritos no ficheiro na opção 0.

```
PROCEDIMENTO executar()
INÍCIO
    movimentos <- carregar_movimentos(FICHEIRO_PADRAO)
    ESCREVER "Carregados ", COMPRIMENTO(movimentos), " movimentos."

    ENQUANTO VERDADEIRO FAZER
        ESCREVER "===== GESTOR DE DESPESAS PESSOAIS ====="
        ESCREVER "1 - Registar movimento"
        ESCREVER "2 - Listar movimentos"
        ESCREVER "3 - Alterar movimento"
        ESCREVER "4 - Remover movimento"
        ESCREVER "5 - Pesquisar / filtrar"
        ESCREVER "6 - Ordenar movimentos"
        ESCREVER "7 - Resumo de um mês"
        ESCREVER "8 - Gasto de um dia"
        ESCREVER "9 - Verificar orçamento mensal"
        ESCREVER "0 - Guardar e sair"
        LER escolha

        ESCOLHER escolha
            CASO "1": acao_registar(movimentos)
            CASO "2": acao_listar(movimentos)
            CASO "3": acao_alterar(movimentos)
            CASO "4": acao_remover(movimentos)
            CASO "5": acao_filtrar(movimentos)
            CASO "6": acao_ordenar(movimentos)
            CASO "7": acao_resumo_mes(movimentos)
            CASO "8": acao_gasto_dia(movimentos)
            CASO "9": acao_orcamento(movimentos)
            CASO "0":
                guardar_movimentos(movimentos, FICHEIRO_PADRAO)
                ESCREVER "Dados guardados. Até à próxima!"
                TERMINAR CICLO
            OUTRO:
                ESCREVER "Opção inválida."
        FIM ESCOLHER
    FIM ENQUANTO
FIM
```


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
