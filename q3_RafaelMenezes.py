import cv2

imagem = cv2.imread('Denji-in-Chainsaw-Man.webp')

ajuste_brilho = int(input("Digite o valor de ajuste de brilho (-100 a 100): "))
ajuste_brilho = max(-100, min(ajuste_brilho, 100))

imagem_brilho_ajustado = cv2.convertScaleAbs(
    imagem, alpha=1, beta=ajuste_brilho)

cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem com Brilho Ajustado', imagem_brilho_ajustado)
cv2.waitKey(0)
cv2.destroyAllWindows()
