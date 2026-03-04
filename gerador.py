import os

from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

# CONFIGURAÇÕES
TOTAL_RIFAS = 1100
RIFAS_POR_LINHAS = 2
RIFAS_POR_COLUNA = 4
IMAGEM_RIFA = "template.png"  # <-- mete aqui o nome do teu ficheiro

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_DIR = os.path.join(BASE_DIR, "build")
os.makedirs(BUILD_DIR, exist_ok=True)

OUTPUT = os.path.join(BUILD_DIR, f"rifas_1_a_{TOTAL_RIFAS}.pdf")

# Abrir imagem base
img = Image.open(IMAGEM_RIFA)
img_width, img_height = img.size

# Página A4 horizontal
page_width, page_height = landscape(A4)

# Calcular tamanho de cada rifa (4 colunas x 2 linhas)
rifa_width = page_width / RIFAS_POR_LINHAS
rifa_height = page_height / RIFAS_POR_COLUNA

c = canvas.Canvas(OUTPUT, pagesize=landscape(A4))

numero_atual = 1

while numero_atual <= TOTAL_RIFAS:
    for linha in range(4):
        for coluna in range(2):
            if numero_atual > TOTAL_RIFAS:
                break

            x = coluna * rifa_width
            y = page_height - ((linha + 1) * rifa_height)

            # Desenhar imagem
            c.drawImage(IMAGEM_RIFA, x, y, width=rifa_width, height=rifa_height)

            # Adicionar número (ajusta posição se necessário)
            c.setFont("Helvetica", 10)

            # Número a 90º
            c.saveState()
            c.translate(x + 40, y + 110)
            c.rotate(90)
            c.drawString(0, 0, f"#{numero_atual:04d}")
            c.restoreState()

            # Número normal (0º)
            c.drawString(x + 370, y + 130, f"#{numero_atual:04d}")
            numero_atual += 1

    c.showPage()

c.save()

print("PDF gerado com sucesso!")
