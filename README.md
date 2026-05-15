# Sprint-Data-Structures-and-Algorithms
# Simulador de Sessão de Recarga — EV Challenge 2026

Simulador de sessão de recarga de veículos elétricos desenvolvido em Python para o Sprint 1 do EV Challenge 2026 (FIAP + GoodWe).

## Lógica Detalhada

### 1. Entrada de dados — `nome_e_tipo_usuario()`

Coleta o nome do usuário via `input()` e exibe um menu com 3 tipos de conta.

A validação usa o padrão `while True` + `try/except` + `break`:
- `while True` mantém o programa pedindo até receber uma resposta válida
- `try` tenta converter o que o usuário digitou em `int()`
- Se a conversão falhar (ex: digitou "abc"), o `except` captura o erro e pede novamente
- Se a conversão der certo mas o número estiver fora de 1–3, o `else` avisa e repete
- Só sai do laço quando o número for 1, 2 ou 3 — aí o `break` encerra
- O 'try/except' foi usado para caso o usúario digitasse algo que não fosse números

Retorna uma tupla `(nome, tipo)`.

---

### 2. Escolha do carregador — `carregador_kw()`

Exibe os 3 tipos de carregador disponíveis e a mesma lógica de validação acima.

Após a escolha válida, converte o número para a potência real:
1 → 7.4 kW   (carregador lento)
2 → 11.0 kW  (carregador normal)
3 → 22.0 kW  (carregador rápido)

Retorna um `float` com a potência em kW.

---

### 3. Duração da sessão — `duracao_sessao()`

Tem dois laços de validação em sequência:

**Laço 1 — valor numérico:**
- Usa `float()` para aceitar decimais (ex: 1.5 horas)
- Rejeita zero e números negativos
- Repete até receber um número positivo válido

**Laço 2 — unidade:**
- Pergunta se a duração é em `(h)oras` ou `(m)inutos`
- `.lower()` aceita H ou M maiúsculos também
- Repete até receber exatamente `h` ou `m`

**Conversão:**
se unidade == "m":  duracao_horas = duracao / 60
se unidade == "h":  duracao_horas = duracao

Sempre retorna a duração em horas, independente do que foi digitado.

---

### 4. Cálculo — `calcular(potencia, duracao_horas, tipo)`

Aplica as duas fórmulas do sistema:
Energia (kWh) = Potência (kW) × Tempo (h)
Custo (R)=Energia(kWh)×Tarifa(R)    = Energia (kWh) × Tarifa (R
)=Energia(kWh)×Tarifa(R/kWh)

A tarifa é definida por condicional conforme o tipo de usuário:

| Tipo | Código | Tarifa |
|------|--------|--------|
| Regular    | 1 | R$ 1,50/kWh |
| Premium    | 2 | R$ 1,20/kWh |
| Condomínio | 3 | R$ 1,35/kWh |

Retorna uma tupla `(energia, custo)`.

**Exemplo:** usuário Premium, carregador Normal (11 kW), 2 horas
Energia = 11 × 2       = 22 kWh
Custo   = 22 × 1.20   = R$ 26,40

---

### 5. Relatório — `exibir_relatorio()`

Recebe todos os dados prontos e apenas os exibe.
Não calcula nada — responsabilidade única de formatação.

Usa f-strings com `:.2f` para formatar os números com 2 casas decimais:
:.2f → 22 vira 22.00 | 1.5 vira 1.50

Saída esperada:
═══════════════════════════════
RELATÓRIO DA SESSÃO
═══════════════════════════════
Usuário:  João Silva
Tipo:     2
Potência: 11.0 kW
Duração:  2.00 horas
Energia:  22.00 kWh
Custo:    R$ 26.40
═══════════════════════════════

---

### 6. Orquestração — `main()`

Conecta todas as funções na ordem certa, passando os dados entre elas:
nome_e_tipo_usuario()  →  nome, tipo
carregador_kw()        →  potencia
duracao_sessao()       →  horas
calcular()             →  energia, custo
exibir_relatorio()     →  saída final

A `main()` nunca faz entrada, cálculo ou exibição diretamente — só orquestra.

O `if __name__ == "__main__"` garante que o programa só executa ao rodar o arquivo diretamente, não quando importado como módulo por outro script.

---

## Estrutura do código

| Função | Responsabilidade |
|---|---|
| `nome_e_tipo_usuario()` | Coleta e valida nome e tipo do usuário |
| `carregador_kw()` | Coleta e valida a potência do carregador |
| `duracao_sessao()` | Coleta duração e converte para horas |
| `calcular()` | Calcula energia e custo com tarifa diferenciada |
| `exibir_relatorio()` | Exibe o relatório final formatado |
| `main()` | Orquestra o fluxo completo do programa |
