import math
import os

from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

# CONFIGURAÇÕES
TOTAL_RIFAS = 1000
RIFAS_POR_LINHAS = 2
RIFAS_POR_COLUNA = 4
IMAGEM_RIFA = "template.png"  # <-- mete aqui o nome do teu ficheiro

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_DIR = os.path.join(BASE_DIR, "build")
os.makedirs(BUILD_DIR, exist_ok=True)

OUTPUT = os.path.join(BUILD_DIR, f"rifas_1_a_{TOTAL_RIFAS}.pdf")
img_reader = ImageReader(IMAGEM_RIFA)
img = Image.open(IMAGEM_RIFA)
img_width, img_height = img.size

page_width, page_height = landscape(A4)

rifa_width = page_width / RIFAS_POR_LINHAS
rifa_height = page_height / RIFAS_POR_COLUNA

c = canvas.Canvas(OUTPUT, pagesize=landscape(A4))

rifas_por_pagina = RIFAS_POR_LINHAS * RIFAS_POR_COLUNA
total_paginas = math.ceil(TOTAL_RIFAS / rifas_por_pagina)

for pagina in range(total_paginas):
    posicao = 0

    for linha in range(RIFAS_POR_COLUNA):
        for coluna in range(RIFAS_POR_LINHAS):
            numero_atual = pagina + (posicao * total_paginas) + 1
            if numero_atual > TOTAL_RIFAS:
                continue
            x = coluna * rifa_width
            y = page_height - ((linha + 1) * rifa_height)

            # Desenhar imagem
            c.drawImage(img_reader, x, y, width=rifa_width, height=rifa_height)
            c.setFont("Helvetica", 10)

            # Número a 90º
            c.saveState()
            c.translate(x + 40, y + 110)
            c.rotate(90)
            c.drawString(0, 0, f"#{numero_atual:04d}")
            c.restoreState()

            # Número normal
            c.drawString(x + 370, y + 130, f"#{numero_atual:04d}")

            posicao += 1

    c.showPage()

c.save()

print("PDF gerado com sucesso!")
