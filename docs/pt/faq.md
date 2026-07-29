# Perguntas Frequentes (FAQ)

## Que tipo de aplicação é essa?

É uma aplicação **desktop** com interface gráfica (não é um site, API ou app mobile), construída com CustomTkinter. Ela calcula grandezas de Movimento Retilíneo Uniforme (MRU) e Movimento Retilíneo Uniformemente Variado (MRUV) e plota os gráficos correspondentes.

## Quais unidades devo usar?

Distância em **metros (m)**, tempo em **segundos (s)** e aceleração em **metros por segundo ao quadrado (m/s²)**, conforme indicado na própria interface da aba MRUV.

## Preciso preencher todos os campos da aba MRUV?

Não. Deixe em branco os campos que você não conhece. A calculadora tenta todas as combinações de fórmulas possíveis com os dados fornecidos e mostra todos os resultados que conseguir calcular.

## Por que às vezes aparece "Reajuste automático aplicado"?

Isso acontece quando uma grandeza (por exemplo, o tempo) não foi informada diretamente, mas pôde ser calculada a partir de outros dados — e esse valor calculado foi então reutilizado para obter outra grandeza que dependia dele (por exemplo, a posição final). A interface deixa isso explícito para que você saiba que aquele resultado depende de um valor derivado, não de um valor que você digitou.

## Posso usar números negativos ou decimais?

Sim, os campos aceitam qualquer valor que o Python interprete como `float` (ex.: `-5`, `3.14`). Use ponto (`.`) como separador decimal, não vírgula.

## Por que os botões "Outro conteúdo" na tela inicial não fazem nada?

Eles são placeholders para conteúdos futuros do projeto. Atualmente apenas o botão "MRU e MRUV" está implementado.

## Existe uma API ou modo linha de comando?

Não. A aplicação só é usada através da interface gráfica, executando `python home.py`. As classes `Mru` e `Mruv` (em `mru.py` e `mruv.py`) poderiam, em tese, ser importadas e usadas isoladamente em outro script Python, mas isso não é um modo de uso documentado ou suportado oficialmente pelo projeto.

## O projeto funciona em Linux ou macOS?

O código usa `self.state("zoomed")` para maximizar a janela e arquivos `.ico` para os ícones — ambos os recursos são mais confiáveis no Windows. Não há confirmação de testes em Linux/macOS. <!-- TODO: confirm suporte oficial a Linux/macOS -->

## Onde ficam os cálculos/fórmulas usados?

Em `mru.py` (fórmulas de MRU) e `mruv.py` (fórmulas de MRUV). Veja a referência completa em [arquitetura.md](arquitetura.md).
