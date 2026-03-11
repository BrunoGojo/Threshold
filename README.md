import pypandoc

text = """
# Threshold com OpenCV

## Descrição
Este projeto demonstra como aplicar Threshold (Limiar) em imagens usando Python e OpenCV.
A aplicação captura a imagem da webcam em tempo real, converte para escala de cinza e aplica um limite (threshold) que transforma a imagem em preto e branco.

Também é exibido um histograma da imagem, mostrando a distribuição das intensidades dos pixels.

## Tecnologias
- Python
- OpenCV
- NumPy

## Como executar

1. Instale as dependências:

pip install opencv-python numpy

2. Execute o programa:

python main.py

## Funcionalidades

O programa exibe as seguintes janelas:

- Original → imagem da webcam
- Cinza → imagem convertida para escala de cinza
- Threshold → imagem binarizada
- Histograma → distribuição das intensidades dos pixels
- Controle de Limite → slider para ajustar o threshold em tempo real

## Conceito de Threshold

pixel > limite → branco  
pixel ≤ limite → preto

Isso transforma a imagem em duas cores: preto e branco.

## Controles

q → fechar o programa
"""

output_path = "/mnt/data/README.md"

pypandoc.convert_text(text, "md", format="md", outputfile=output_path, extra_args=['--standalone'])

output_path
