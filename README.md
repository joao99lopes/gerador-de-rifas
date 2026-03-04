# 🎟️ Gerador de Rifas em PDF

Script em Python (`gerador.py`) para gerar automaticamente rifas
numeradas em PDF, a partir de um template de imagem.

O PDF é gerado em formato **A4 horizontal**, com múltiplas rifas por
página e numeração automática de 4 dígitos (ex: `#0001` até ao número
definido).

------------------------------------------------------------------------

## 📦 Funcionalidades

-   Geração automática de centenas ou milhares de rifas
-   Numeração sequencial com 4 algarismos
-   Número em duas posições:
    -   Vertical (90º)
    -   Horizontal (0º)
-   Layout configurável (linhas e colunas)
-   Criação automática da pasta `build/`
-   Exportação direta para PDF pronto a imprimir

------------------------------------------------------------------------

## 🖼️ Estrutura Esperada

Coloca o ficheiro `template.png` na mesma pasta do script.

    projeto/
    │
    ├── template.png
    ├── gerador.py
    └── build/

O PDF final será criado automaticamente dentro da pasta:

    build/rifas_1_a_<TOTAL_RIFAS>.pdf

------------------------------------------------------------------------

## ⚙️ Configuração

No início do script podes alterar:

``` python
TOTAL_RIFAS = 1100
RIFAS_POR_LINHAS = 2
RIFAS_POR_COLUNA = 4
IMAGEM_RIFA = "template.png"
```

### 🔧 Parâmetros

-   `TOTAL_RIFAS` → número total de rifas a gerar\
-   `RIFAS_POR_LINHAS` → número de rifas por linha\
-   `RIFAS_POR_COLUNA` → número de rifas por coluna\
-   `IMAGEM_RIFA` → ficheiro base da rifa

------------------------------------------------------------------------

## 🖨️ Layout

-   Página: A4 horizontal
-   2 colunas × 4 linhas (8 rifas por página)
-   Cada rifa é redimensionada automaticamente
-   Numeração no formato:


```
    #0001
    #0002
    ...
```
------------------------------------------------------------------------

## 📚 Dependências

Instalar com:

``` bash
pip install pillow reportlab
```

Bibliotecas usadas:

-   Pillow (PIL) → manipulação da imagem
-   ReportLab → geração do PDF

------------------------------------------------------------------------

## ▶️ Como executar

``` bash
python gerador.py
```

Após execução:

    PDF gerado com sucesso!

O ficheiro estará disponível na pasta `build/`.

------------------------------------------------------------------------

## 📌 Notas Importantes

-   Ajusta as coordenadas do número se precisares de alinhar melhor ao
    teu template:

    ``` python
    c.translate(x + 40, y + 110)  # posição número vertical
    c.drawString(x + 370, y + 130, ...)  # posição número horizontal
    ```

-   O script assume que o `template.png` tem proporções compatíveis com
    o layout escolhido.

-   Para impressão profissional, recomenda-se exportar o template em
    alta resolução (300dpi).

------------------------------------------------------------------------

## 🚀 Possíveis melhorias futuras

-   Margens de corte automáticas
-   Exportação por lotes
-   Interface gráfica simples
-   Personalização de fonte
-   Suporte a códigos QR ou código de barras
