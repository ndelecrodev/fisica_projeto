# Uso

Como executar a aplicação e utilizar a calculadora de MRU e MRUV.

## Executando a aplicação

Com o ambiente virtual ativado e as dependências instaladas (veja [instalacao.md](instalacao.md)), rode a partir da raiz do repositório:

```bash
python home.py
```

> **Importante:** execute o comando a partir da raiz do projeto. Os ícones das janelas são carregados com caminhos relativos (ex.: `assets/icon-ico/pagina-inicial.ico`), então rodar o script de outro diretório fará com que os ícones não sejam encontrados.

A janela principal abre maximizada, em tema escuro, mostrando a **Home Page**.

## Navegação

A Home Page apresenta botões de conteúdo. Atualmente apenas o botão **"MRU e MRUV"** está funcional e leva à calculadora. Os demais botões ("Outro conteúdo") existem na interface, mas ainda não têm nenhuma ação associada — são placeholders para conteúdos futuros.

Dentro da página de cálculo há duas abas: **MRU** e **MRUV**. Cada aba tem um botão **Voltar**, que retorna para a Home Page.

## Aba MRU (Movimento Retilíneo Uniforme)

1. Marque **apenas uma** das três caixas de seleção, de acordo com o que deseja calcular:
   - **Calcular Posição Final (s)** — pede posição inicial (s0), velocidade (v) e tempo (t).
   - **Calcular Velocidade (v)** — pergunta se você tem o espaço percorrido (Δs). Se sim, pede Δs e tempo; se não, pede posição inicial, posição final e tempo.
   - **Calcular Tempo (t)** — mesma lógica de Δs: com Δs pede velocidade; sem Δs pede posição inicial, posição final e velocidade.
2. Preencha os campos exibidos (aceitam números decimais, use `.` como separador).
3. Pressione **Enter** em qualquer campo ou clique em **Calcular**.
4. O resultado aparece em uma janela pop-up, com um botão **Ver Gráficos** para abrir os gráficos de posição/velocidade/aceleração x tempo.

Se algum campo estiver vazio ou com um valor não numérico, uma janela de erro aparece: *"Insira valores válidos em todas as caixas de texto"*.

## Aba MRUV (Movimento Retilíneo Uniformemente Variado)

1. Informe se você possui o **Espaço Percorrido (Δs)** marcando **Sim** ou **Não** (apenas uma das duas).
2. Preencha os campos que fizerem sentido para o seu problema. **Deixe em branco os campos que você não sabe** — a calculadora tenta descobrir automaticamente quais grandezas conseguem ser calculadas com os dados fornecidos.
3. Unidades esperadas: distância em **metros**, tempo em **segundos**, aceleração em **m/s²**.
4. Clique em **Calcular** (ou pressione Enter, quando aplicável).

A calculadora tenta todas as fórmulas de MRUV compatíveis com os valores informados e mostra **todos os resultados possíveis** — não apenas um. Quando um resultado intermediário (por exemplo, o tempo) é necessário para calcular outra grandeza (por exemplo, a posição final) e não foi informado diretamente, a calculadora reaproveita o valor recém-calculado e sinaliza isso na janela de resposta, na seção **"Reajuste automático aplicado"**.

Se nenhuma combinação de fórmulas puder ser resolvida com os dados informados, aparece a mensagem: *"Houve um ERRO ao calcular o MRUV"*.

Assim como na aba MRU, o resultado é exibido em uma janela pop-up com um botão **Ver Gráficos**.

## Gráficos

O botão **Ver Gráficos** abre uma nova janela com abas contendo (quando os dados necessários estiverem disponíveis):

- **s x t** — posição em função do tempo
- **v x t** — velocidade em função do tempo
- **a x t** — aceleração em função do tempo (linha tracejada)

No modo MRU, a aceleração é sempre fixada em `0`. As janelas de resultado (MRU, MRUV, erro) fecham automaticamente após um tempo: **60 segundos** para janelas de resultado e **10 segundos** para janelas de erro.

## Exemplo prático (MRU)

Calculando a posição final com `s0 = 0`, `v = 10` (m/s) e `t = 5` (s):

1. Vá até a aba **MRU**.
2. Marque **Calcular Posição Final (s)**.
3. Preencha: Posição Inicial = `0`, Velocidade = `10`, Tempo = `5`.
4. Clique em **Calcular** → resultado esperado: `Posição Final: 50.00`.

<!-- TODO: confirm se há um comportamento conhecido em que este cálculo específico pode falhar silenciosamente — ver docs/pt/troubleshooting.md -->
