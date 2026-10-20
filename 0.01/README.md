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

## Pseudocódigo

### 1. Algoritmo principal

```
=====================================================================
 ALGORITMO GestorDeDespesasPessoais
 Ponto de entrada do programa
=====================================================================

 USA interface (executar)

 INÍCIO
     TENTAR
         executar()
     EM CASO DE INTERRUPÇÃO (Ctrl+C)
         ESCREVER "Programa interrompido. As alterações desta sessão não foram guardadas."
     FIM TENTAR
 FIM
```

### 2. Modelo de dados

```
=====================================================================
 MÓDULO modelo
 Estrutura de dados do Gestor de Despesas Pessoais
=====================================================================

 Um MOVIMENTO é um TUPLO com 6 campos (imutável):

     (id, data, tipo, categoria, descricao, valor)

     id         : inteiro   -> identificador único
     data       : texto     -> formato AAAA-MM-DD
     tipo       : texto     -> "receita" ou "despesa"
     categoria  : texto     -> uma das categorias do tipo
     descricao  : texto
     valor      : real > 0  -> o sinal é dado pelo tipo

 O conjunto de movimentos é uma LISTA de tuplos (mutável).

---------------------------------------------------------------------
 CONSTANTES
---------------------------------------------------------------------

 // posições dos campos dentro do tuplo
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

---------------------------------------------------------------------
 FUNÇÃO categorias_do_tipo(tipo) : tuplo
---------------------------------------------------------------------
 INÍCIO
     SE tipo = RECEITA ENTÃO
         DEVOLVER CATEGORIAS_RECEITA
     SENÃO SE tipo = DESPESA ENTÃO
         DEVOLVER CATEGORIAS_DESPESA
     SENÃO
         DEVOLVER ()                      // tuplo vazio
     FIM SE
 FIM

---------------------------------------------------------------------
 FUNÇÃO criar_movimento(id, data, tipo, categoria, descricao, valor) : tuplo
---------------------------------------------------------------------
 INÍCIO
     DEVOLVER (id, data, tipo, categoria, descricao, ARREDONDAR(valor, 2))
 FIM

---------------------------------------------------------------------
 FUNÇÃO proximo_id(movimentos) : inteiro
 Devolve o maior id existente + 1
---------------------------------------------------------------------
 INÍCIO
     maior <- 0
     PARA CADA movimento EM movimentos FAZER
         SE movimento[ID] > maior ENTÃO
             maior <- movimento[ID]
         FIM SE
     FIM PARA
     DEVOLVER maior + 1
 FIM

---------------------------------------------------------------------
 FUNÇÃO formatar_movimento(movimento) : texto
 Devolve uma linha de tabela para mostrar o movimento
---------------------------------------------------------------------
 INÍCIO
     SE movimento[TIPO] = RECEITA ENTÃO
         sinal <- "+"
     SENÃO
         sinal <- "-"
     FIM SE
     DEVOLVER movimento[ID] + " | " + movimento[DATA] + " | " + movimento[TIPO]
              + " | " + movimento[CATEGORIA] + " | " + movimento[DESCRICAO]
              + " | " + sinal + movimento[VALOR] (2 casas decimais) + " €"
 FIM
```

### 3. Validação

```
=====================================================================
 MÓDULO validacao
 Validação dos dados introduzidos pelo utilizador
=====================================================================

 USA modelo (TIPOS, categorias_do_tipo)

---------------------------------------------------------------------
 FUNÇÃO data_valida(texto) : lógico
 Verifica se o texto é uma data real no formato AAAA-MM-DD
---------------------------------------------------------------------
 INÍCIO
     SE COMPRIMENTO(texto) <> 10 ENTÃO
         DEVOLVER FALSO
     FIM SE
     SE texto[4] <> "-" OU texto[7] <> "-" ENTÃO
         DEVOLVER FALSO
     FIM SE
     ano <- texto[0..3]   mes <- texto[5..6]   dia <- texto[8..9]
     SE ano, mes ou dia não forem números ENTÃO
         DEVOLVER FALSO
     FIM SE
     SE mes < 1 OU mes > 12 ENTÃO
         DEVOLVER FALSO
     FIM SE
     SE dia < 1 OU dia > DIAS_DO_MES(ano, mes) ENTÃO    // ex.: 30/02 é inválido
         DEVOLVER FALSO
     FIM SE
     DEVOLVER VERDADEIRO
 FIM

---------------------------------------------------------------------
 FUNÇÃO converter_valor(texto) : real ou NULO
 Aceita "12,50" ou "12.50". Devolve NULO se não for um número positivo.
---------------------------------------------------------------------
 INÍCIO
     texto <- SUBSTITUIR(",", ".", REMOVER_ESPACOS(texto))
     SE texto não representa um número ENTÃO
         DEVOLVER NULO
     FIM SE
     valor <- CONVERTER_PARA_REAL(texto)
     SE valor <= 0 ENTÃO
         DEVOLVER NULO
     FIM SE
     DEVOLVER ARREDONDAR(valor, 2)
 FIM

---------------------------------------------------------------------
 FUNÇÃO tipo_valido(tipo) : lógico
---------------------------------------------------------------------
 INÍCIO
     DEVOLVER tipo PERTENCE A TIPOS
 FIM

---------------------------------------------------------------------
 FUNÇÃO categoria_valida(tipo, categoria) : lógico
---------------------------------------------------------------------
 INÍCIO
     DEVOLVER categoria PERTENCE A categorias_do_tipo(tipo)
 FIM

---------------------------------------------------------------------
 FUNÇÃO descricao_valida(descricao) : lógico
 Não pode ser vazia nem conter ";" (separador do ficheiro CSV)
---------------------------------------------------------------------
 INÍCIO
     DEVOLVER REMOVER_ESPACOS(descricao) <> "" E ";" NÃO PERTENCE A descricao
 FIM

---------------------------------------------------------------------
 FUNÇÃO validar_campos(data, tipo, categoria, descricao, valor) : lista
 Devolve a lista de mensagens de erro (vazia se tudo estiver correto)
---------------------------------------------------------------------
 INÍCIO
     erros <- []
     SE NÃO data_valida(data) ENTÃO
         ACRESCENTAR "Data inválida (use AAAA-MM-DD)." A erros
     FIM SE
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

### 4. Operações (CRUD, filtros, ordenação, resumos)

```
=====================================================================
 MÓDULO operacoes
 CRUD, pesquisa/filtragem, ordenação e resumos
 Todas as funções recebem a LISTA de movimentos como 1.º parâmetro.
=====================================================================

 USA modelo, validacao

=====================================================================
 1. CRUD
=====================================================================

---------------------------------------------------------------------
 FUNÇÃO adicionar_movimento(movimentos, data, tipo, categoria, descricao, valor) : tuplo
---------------------------------------------------------------------
 INÍCIO
     erros <- validar_campos(data, tipo, categoria, descricao, valor)
     SE erros não está vazia ENTÃO
         ASSINALAR ERRO(erros)
     FIM SE
     movimento <- criar_movimento(proximo_id(movimentos), data, tipo,
                                  categoria, descricao, valor)
     ACRESCENTAR movimento A movimentos
     DEVOLVER movimento
 FIM

---------------------------------------------------------------------
 FUNÇÃO procurar_indice(movimentos, id) : inteiro
 Devolve a posição do movimento na lista, ou -1 se não existir
---------------------------------------------------------------------
 INÍCIO
     PARA i DE 0 ATÉ COMPRIMENTO(movimentos) - 1 FAZER
         SE movimentos[i][ID] = id ENTÃO
             DEVOLVER i
         FIM SE
     FIM PARA
     DEVOLVER -1
 FIM

---------------------------------------------------------------------
 FUNÇÃO obter_movimento(movimentos, id) : tuplo ou NULO
---------------------------------------------------------------------
 INÍCIO
     i <- procurar_indice(movimentos, id)
     SE i = -1 ENTÃO
         DEVOLVER NULO
     FIM SE
     DEVOLVER movimentos[i]
 FIM

---------------------------------------------------------------------
 FUNÇÃO atualizar_movimento(movimentos, id, data, tipo, categoria, descricao, valor) : tuplo
 Os parâmetros com valor NULO mantêm o valor atual.
 Como o tuplo é imutável, cria-se um NOVO tuplo que substitui o antigo.
---------------------------------------------------------------------
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

     erros <- validar_campos(data, tipo, categoria, descricao, valor)
     SE erros não está vazia ENTÃO
         ASSINALAR ERRO(erros)
     FIM SE

     novo <- criar_movimento(id, data, tipo, categoria, descricao, valor)
     movimentos[i] <- novo
     DEVOLVER novo
 FIM

---------------------------------------------------------------------
 FUNÇÃO remover_movimento(movimentos, id) : lógico
---------------------------------------------------------------------
 INÍCIO
     i <- procurar_indice(movimentos, id)
     SE i = -1 ENTÃO
         DEVOLVER FALSO
     FIM SE
     REMOVER movimentos[i]
     DEVOLVER VERDADEIRO
 FIM

=====================================================================
 2. PESQUISA E FILTRAGEM  (devolvem sempre uma NOVA lista)
=====================================================================

---------------------------------------------------------------------
 FUNÇÃO filtrar_por_tipo(movimentos, tipo) : lista
---------------------------------------------------------------------
 INÍCIO
     resultado <- []
     PARA CADA m EM movimentos FAZER
         SE m[TIPO] = tipo ENTÃO
             ACRESCENTAR m A resultado
         FIM SE
     FIM PARA
     DEVOLVER resultado
 FIM

---------------------------------------------------------------------
 FUNÇÃO filtrar_por_categoria(movimentos, categoria) : lista
---------------------------------------------------------------------
 INÍCIO
     resultado <- []
     PARA CADA m EM movimentos FAZER
         SE m[CATEGORIA] = categoria ENTÃO
             ACRESCENTAR m A resultado
         FIM SE
     FIM PARA
     DEVOLVER resultado
 FIM

---------------------------------------------------------------------
 FUNÇÃO filtrar_por_periodo(movimentos, data_inicio, data_fim) : lista
 Datas AAAA-MM-DD podem ser comparadas diretamente como texto.
---------------------------------------------------------------------
 INÍCIO
     resultado <- []
     PARA CADA m EM movimentos FAZER
         SE data_inicio <= m[DATA] E m[DATA] <= data_fim ENTÃO
             ACRESCENTAR m A resultado
         FIM SE
     FIM PARA
     DEVOLVER resultado
 FIM

---------------------------------------------------------------------
 FUNÇÃO filtrar_por_mes(movimentos, ano, mes) : lista
---------------------------------------------------------------------
 INÍCIO
     prefixo <- ano (4 dígitos) + "-" + mes (2 dígitos)      // ex.: "2026-10"
     resultado <- []
     PARA CADA m EM movimentos FAZER
         SE m[DATA] COMEÇA POR prefixo ENTÃO
             ACRESCENTAR m A resultado
         FIM SE
     FIM PARA
     DEVOLVER resultado
 FIM

---------------------------------------------------------------------
 FUNÇÃO pesquisar_descricao(movimentos, texto) : lista
 Pesquisa sem distinguir maiúsculas/minúsculas
---------------------------------------------------------------------
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

=====================================================================
 3. ORDENAÇÃO  (ordenação por inserção; a lista original não é alterada)
=====================================================================

---------------------------------------------------------------------
 FUNÇÃO ordenar_por_campo(movimentos, campo, decrescente) : lista
---------------------------------------------------------------------
 INÍCIO
     ordenada <- CÓPIA(movimentos)
     PARA i DE 1 ATÉ COMPRIMENTO(ordenada) - 1 FAZER
         atual <- ordenada[i]
         j <- i - 1
         ENQUANTO j >= 0 E vem_depois(ordenada[j][campo], atual[campo], decrescente) FAZER
             ordenada[j + 1] <- ordenada[j]
             j <- j - 1
         FIM ENQUANTO
         ordenada[j + 1] <- atual
     FIM PARA
     DEVOLVER ordenada
 FIM

---------------------------------------------------------------------
 FUNÇÃO vem_depois(a, b, decrescente) : lógico
---------------------------------------------------------------------
 INÍCIO
     SE decrescente ENTÃO
         DEVOLVER a < b
     SENÃO
         DEVOLVER a > b
     FIM SE
 FIM

 FUNÇÃO ordenar_por_data(movimentos, decrescente)
     DEVOLVER ordenar_por_campo(movimentos, DATA, decrescente)

 FUNÇÃO ordenar_por_valor(movimentos, decrescente)
     DEVOLVER ordenar_por_campo(movimentos, VALOR, decrescente)

=====================================================================
 4. RESUMOS E ORÇAMENTO
=====================================================================

---------------------------------------------------------------------
 FUNÇÃO calcular_totais(movimentos) : tuplo (receitas, despesas, saldo)
---------------------------------------------------------------------
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

---------------------------------------------------------------------
 FUNÇÃO totais_por_categoria(movimentos, tipo) : lista de tuplos (categoria, total)
 Só categorias com total > 0, do maior para o menor total
---------------------------------------------------------------------
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

     // ordenação por inserção pelo total (posição 1 do tuplo), decrescente
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

---------------------------------------------------------------------
 FUNÇÃO total_do_dia(movimentos, data) : real
 Total de despesas de um dia (orçamento diário)
---------------------------------------------------------------------
 INÍCIO
     total <- 0
     PARA CADA m EM movimentos FAZER
         SE m[DATA] = data E m[TIPO] = DESPESA ENTÃO
             total <- total + m[VALOR]
         FIM SE
     FIM PARA
     DEVOLVER ARREDONDAR(total, 2)
 FIM

---------------------------------------------------------------------
 FUNÇÃO verificar_orcamento(movimentos, ano, mes, limite)
        : tuplo (gasto, restante, percentagem, excedido)
---------------------------------------------------------------------
 INÍCIO
     do_mes <- filtrar_por_mes(movimentos, ano, mes)
     (_, gasto, _) <- calcular_totais(do_mes)
     restante <- limite - gasto
     SE limite > 0 ENTÃO
         percentagem <- gasto / limite * 100
     SENÃO
         percentagem <- 0
     FIM SE
     excedido <- gasto > limite
     DEVOLVER (gasto, restante, percentagem, excedido)
 FIM
```

### 5. Persistência (CSV)

```
=====================================================================
 MÓDULO persistencia
 Leitura e escrita dos movimentos no ficheiro dados/movimentos.csv
 (uma linha por movimento, campos separados por ";")
=====================================================================

 USA modelo (CAMPOS, criar_movimento)

 CONSTANTE FICHEIRO_PADRAO <- "dados/movimentos.csv"

---------------------------------------------------------------------
 PROCEDIMENTO guardar_movimentos(movimentos, caminho)
---------------------------------------------------------------------
 INÍCIO
     ABRIR caminho PARA ESCRITA COMO ficheiro
     ESCREVER LINHA JUNTAR(CAMPOS, ";") EM ficheiro        // cabeçalho
     PARA CADA m EM movimentos FAZER
         ESCREVER LINHA JUNTAR(m, ";") EM ficheiro
     FIM PARA
     FECHAR ficheiro
 FIM

---------------------------------------------------------------------
 FUNÇÃO carregar_movimentos(caminho) : lista
 Se o ficheiro não existir devolve lista vazia; linhas inválidas são ignoradas
---------------------------------------------------------------------
 INÍCIO
     movimentos <- []
     SE caminho NÃO EXISTE ENTÃO
         DEVOLVER movimentos
     FIM SE

     ABRIR caminho PARA LEITURA COMO ficheiro
     LER LINHA DE ficheiro                                  // salta o cabeçalho
     ENQUANTO NÃO FIM_DE_FICHEIRO(ficheiro) FAZER
         campos <- DIVIDIR(LER LINHA DE ficheiro, ";")
         SE COMPRIMENTO(campos) = 6
            E campos[0] é inteiro E campos[5] é número ENTÃO
             m <- criar_movimento(INTEIRO(campos[0]), campos[1], campos[2],
                                  campos[3], campos[4], REAL(campos[5]))
             ACRESCENTAR m A movimentos
         FIM SE
     FIM ENQUANTO
     FECHAR ficheiro
     DEVOLVER movimentos
 FIM
```

### 6. Interface (menu textual)

```
=====================================================================
 MÓDULO interface
 Menu textual na consola
=====================================================================

 USA modelo, validacao, operacoes, persistencia

=====================================================================
 1. LEITURA DE DADOS (repete o pedido enquanto a resposta for inválida)
=====================================================================

---------------------------------------------------------------------
 FUNÇÃO ler_data(mensagem, permitir_vazio) : texto ou NULO
---------------------------------------------------------------------
 INÍCIO
     REPETIR
         ESCREVER mensagem
         LER texto
         SE texto = "" ENTÃO
             SE permitir_vazio ENTÃO DEVOLVER NULO FIM SE
             DEVOLVER DATA_DE_HOJE()
         FIM SE
         SE data_valida(texto) ENTÃO
             DEVOLVER texto
         FIM SE
         ESCREVER "Data inválida. Use AAAA-MM-DD."
     ATÉ FALSO          // só sai pelos DEVOLVER
 FIM

---------------------------------------------------------------------
 FUNÇÃO ler_opcao(mensagem, opcoes, permitir_vazio) : texto ou NULO
 Mostra as opções numeradas; aceita o número ou o nome
---------------------------------------------------------------------
 INÍCIO
     PARA n DE 1 ATÉ COMPRIMENTO(opcoes) FAZER
         ESCREVER n + ". " + opcoes[n - 1]
     FIM PARA
     REPETIR
         ESCREVER mensagem
         LER texto
         SE texto = "" E permitir_vazio ENTÃO DEVOLVER NULO FIM SE
         SE texto é número E 1 <= texto <= COMPRIMENTO(opcoes) ENTÃO
             DEVOLVER opcoes[texto - 1]
         FIM SE
         SE texto PERTENCE A opcoes ENTÃO
             DEVOLVER texto
         FIM SE
         ESCREVER "Opção inválida."
     ATÉ FALSO
 FIM

---------------------------------------------------------------------
 FUNÇÃO ler_valor(mensagem, permitir_vazio) : real ou NULO
---------------------------------------------------------------------
 INÍCIO
     REPETIR
         ESCREVER mensagem
         LER texto
         SE texto = "" E permitir_vazio ENTÃO DEVOLVER NULO FIM SE
         valor <- converter_valor(texto)
         SE valor <> NULO ENTÃO
             DEVOLVER valor
         FIM SE
         ESCREVER "Valor inválido. Introduza um número positivo (ex.: 12,50)."
     ATÉ FALSO
 FIM

 // ler_texto, ler_inteiro e ler_ano_mes seguem o mesmo padrão:
 // pedir -> validar -> devolver se válido, senão avisar e repetir.

=====================================================================
 2. APRESENTAÇÃO
=====================================================================

---------------------------------------------------------------------
 PROCEDIMENTO mostrar_movimentos(movimentos)
---------------------------------------------------------------------
 INÍCIO
     SE movimentos está vazia ENTÃO
         ESCREVER "(sem movimentos)"
     SENÃO
         ESCREVER cabeçalho da tabela
         PARA CADA m EM movimentos FAZER
             ESCREVER formatar_movimento(m)
         FIM PARA
         (receitas, despesas, saldo) <- calcular_totais(movimentos)
         ESCREVER "Receitas: ", receitas, "  Despesas: ", despesas, "  Saldo: ", saldo
     FIM SE
 FIM

=====================================================================
 3. AÇÕES DO MENU
=====================================================================

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
     // se o tipo mudou, a categoria é obrigatória
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
     SENÃO
         ESCREVER formatar_movimento(m)
         ESCREVER "Tem a certeza? (s/n)"
         LER resposta
         SE resposta = "s" ENTÃO
             remover_movimento(movimentos, id)
             ESCREVER "Movimento removido."
         SENÃO
             ESCREVER "Operação cancelada."
         FIM SE
     FIM SE
 FIM

 PROCEDIMENTO acao_filtrar(movimentos)
 INÍCIO
     ESCREVER "1-Tipo  2-Categoria  3-Mês  4-Intervalo de datas  5-Texto"
     LER escolha
     ESCOLHER escolha
         CASO "1": tipo <- ler_opcao(...)
                   resultado <- filtrar_por_tipo(movimentos, tipo)
         CASO "2": tipo <- ler_opcao(...);  categoria <- ler_opcao(...)
                   resultado <- filtrar_por_tipo(filtrar_por_categoria(movimentos, categoria), tipo)
         CASO "3": (ano, mes) <- ler_ano_mes()
                   resultado <- filtrar_por_mes(movimentos, ano, mes)
         CASO "4": inicio <- ler_data(...);  fim <- ler_data(...)
                   resultado <- filtrar_por_periodo(movimentos, inicio, fim)
         CASO "5": texto <- ler_texto(...)
                   resultado <- pesquisar_descricao(movimentos, texto)
         OUTRO:    ESCREVER "Opção inválida."
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
         ESCREVER "Atenção: já usou mais de 80%. Restam ", restante
     SENÃO
         ESCREVER "Restam ", restante
     FIM SE
 FIM

=====================================================================
 4. CICLO PRINCIPAL
=====================================================================

---------------------------------------------------------------------
 PROCEDIMENTO executar()
---------------------------------------------------------------------
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
             CASO "0": guardar_movimentos(movimentos, FICHEIRO_PADRAO)
                       ESCREVER "Dados guardados. Até à próxima!"
                       TERMINAR CICLO
             OUTRO:    ESCREVER "Opção inválida."
         FIM ESCOLHER
     FIM ENQUANTO
 FIM
```

### 7. Casos de teste

```
=====================================================================
 CASOS DE TESTE (a automatizar quando o código for escrito em Python)
=====================================================================

 Lista de exemplo usada nos testes:
     1  2026-10-01  receita  bolsa        Bolsa         350.00
     2  2026-10-02  despesa  alimentacao  Supermercado   42.35
     3  2026-10-02  despesa  transporte   Passe          25.00
     4  2026-09-20  despesa  alimentacao  Cantina        10.00

 ------------------------------------------------------------------------------
 Função                                  Entrada                    Esperado
 ------------------------------------------------------------------------------
 data_valida                             "2026-10-19"               VERDADEIRO
 data_valida                             "2026-02-30"               FALSO
 data_valida                             "19-10-2026"               FALSO
 converter_valor                         "12,50"                    12.5
 converter_valor                         "-5" / "0" / "abc"         NULO
 adicionar_movimento (4 vezes)           lista vazia                ids 1, 2, 3, 4
 adicionar_movimento                     data "2026-13-01"          ERRO, lista inalterada
 adicionar_movimento                     despesa com cat. "salario" ERRO
 atualizar_movimento                     id 2, valor 50             movimento 2 com valor 50
 atualizar_movimento                     id 99                      ERRO (não existe)
 remover_movimento                       id 3 (2 vezes)             VERDADEIRO, depois FALSO
 adicionar após remover o id 3           —                          novo id = 5
 filtrar_por_tipo                        "despesa"                  3 movimentos
 filtrar_por_categoria                   "alimentacao"              2 movimentos
 filtrar_por_mes                         2026, 10                   3 movimentos
 filtrar_por_periodo                     2026-10-02 a 2026-10-31    2 movimentos
 pesquisar_descricao                     "SUPER"                    1 movimento
 ordenar_por_data                        —                          1.º = id 4
 ordenar_por_valor (decrescente)         —                          350, 42.35, 25, 10
 calcular_totais                         lista exemplo              (350.00, 77.35, 272.65)
 calcular_totais                         lista vazia                (0, 0, 0)
 totais_por_categoria                    "despesa"                  [(alimentacao, 52.35), (transporte, 25.00)]
 total_do_dia                            "2026-10-02"               67.35
 verificar_orcamento                     2026, 10, limite 100       (67.35, 32.65, 67.3%, FALSO)
 verificar_orcamento                     2026, 10, limite 50        excedido = VERDADEIRO
 guardar + carregar                      lista exemplo              lista igual à original
 carregar_movimentos                     ficheiro inexistente       lista vazia
 ------------------------------------------------------------------------------
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
