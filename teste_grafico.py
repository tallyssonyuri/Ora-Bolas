from math import *
import matplotlib.pyplot as plt

# Inicialização
Velocidade = 0.02

BolaX = 10
BolaY = 0
RaioBola = 1

SmallSizeX = 1
SmallSizeY = 2
RaioSmallSize = 5

# Listas para armazenar dados para gráficos
posicao_robo_x = []
posicao_robo_y = []
posicao_bola_x = []
posicao_bola_y = []
tempo = []
distancia = []

t = 0
while True:
    # Imprimir posições e distância
    print("Posicao Robo: X = %.2f / Y = %.2f" % (SmallSizeX, SmallSizeY))
    print("Posicao Bola: X = %.2f / Y = %.2f" % (BolaX, BolaY))
    print("Diferenca: %.4f " % hypot(BolaX - SmallSizeX, BolaY - SmallSizeY))
    print("Distancia: %.4f" % (hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize)))
    print()

    # Armazenar dados para gráficos
    posicao_robo_x.append(SmallSizeX)
    posicao_robo_y.append(SmallSizeY)
    posicao_bola_x.append(BolaX)
    posicao_bola_y.append(BolaY)
    tempo.append(t)
    distancia.append(hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize))

    if BolaX - SmallSizeX < 0:
        SmallSizeX -= Velocidade
    else:
        SmallSizeX += Velocidade

    if BolaY - SmallSizeY < 0:
        SmallSizeY -= Velocidade
    else:
        SmallSizeY += Velocidade

    if hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize) <= 0:
        print("Bola Interceptada!!!!!")
        print("Posicao Robo: X = %.2f / Y = %.2f" % (SmallSizeX, SmallSizeY))
        print("Posicao Bola: X = %.2f / Y = %.2f" % (BolaX, BolaY))
        print("Diferenca: %.4f " % hypot(BolaX - SmallSizeX, BolaY - SmallSizeY))
        print("Distancia: %.4f" % (hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize)))
        print()
        break

    t += 1

# Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦
plt.figure(figsize=(10, 5))
plt.plot(posicao_robo_x, posicao_robo_y, label='Robô')
plt.plot(posicao_bola_x, posicao_bola_y, label='Bola')
plt.title('Trajetórias da bola e do robô')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡
plt.figure(figsize=(10, 5))
plt.plot(tempo, posicao_robo_x, label='Robô X')
plt.plot(tempo, posicao_robo_y, label='Robô Y')
plt.plot(tempo, posicao_bola_x, label='Bola X')
plt.plot(tempo, posicao_bola_y, label='Bola Y')
plt.title('Coordenadas da bola e do robô em função do tempo')
plt.xlabel('Tempo')
plt.ylabel('Posição')
plt.legend()
plt.show()

# Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo 𝑡
plt.figure(figsize=(10, 5))
plt.plot(tempo, distancia)
plt.title('Distância entre a bola e o robô em função do tempo')
plt.xlabel('Tempo')
plt.ylabel('Distância')
plt.show()