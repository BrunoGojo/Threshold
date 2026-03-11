import cv2
import numpy as np

def nothing(x):
    pass

# Inicializa a webcam
cap = cv2.VideoCapture(0)

# Criação das janelas
cv2.namedWindow("Original")
cv2.namedWindow("Cinza")
cv2.namedWindow("Threshold")
cv2.namedWindow("Histograma")
cv2.namedWindow("Controle de Limite")

# Criação do trackbar em janela separada
cv2.createTrackbar("Limite", "Controle de Limite", 127, 255, nothing)

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensiona para ficar mais organizado
    frame = cv2.resize(frame, (400, 300))

    # Converte para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lê o valor atual do trackbar
    threshold_val = cv2.getTrackbarPos("Limite", "Controle de Limite")

    # Aplica o threshold binário
    _, threshold_img = cv2.threshold(gray, threshold_val, 255, cv2.THRESH_BINARY)

    # -------------------------
    # Criação do histograma
    # -------------------------
    hist_width = 400
    hist_height = 300
    hist_img = np.zeros((hist_height, hist_width, 3), dtype=np.uint8)

    # Calcula o histograma da imagem em cinza
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # Normaliza os valores para caberem na altura da janela
    cv2.normalize(hist, hist, 0, hist_height, cv2.NORM_MINMAX)

    # Largura de cada barra/intervalo do histograma
    bin_width = hist_width / 256

    # Desenha o histograma
    for i in range(1, 256):
        x1 = int((i - 1) * bin_width)
        y1 = hist_height - int(hist[i - 1].item())

        x2 = int(i * bin_width)
        y2 = hist_height - int(hist[i].item())

        cv2.line(hist_img, (x1, y1), (x2, y2), (255, 255, 255), 1)

    # Desenha uma linha vermelha mostrando o valor atual do threshold
    x_thresh = int((threshold_val / 255) * hist_width)
    cv2.line(hist_img, (x_thresh, 0), (x_thresh, hist_height), (0, 0, 255), 2)

    # Exibe as janelas
    cv2.imshow("Original", frame)
    cv2.imshow("Cinza", gray)
    cv2.imshow("Threshold", threshold_img)
    cv2.imshow("Histograma", hist_img)

    # Encerra ao apertar q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera recursos
cap.release()

cv2.destroyAllWindows()
