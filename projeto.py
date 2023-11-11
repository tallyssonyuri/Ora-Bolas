from math import* # Importa todas as funções da biblioteca math, como hypot, sin, cos, etc.

# [X] Criar um arquivo trajetoBola.txt
# [ ] Importar arquivo para o codigo
# [ ] Acessar arquivo e entender o que são cada variavel

Velocidade = 0.02 # Define uma variável chamada Velocidade que guarda o valor 0.02, que representa a velocidade do robô em unidades por segundo.

BolaX = 12 # Define a posição inicial da bola no eixo X.
BolaY = 10 # Define a posição inicial da bola no eixo Y.
RaioBola = 3 # Define o raio da bola.

SmallSizeX = 1 # Define a posição inicial do robô no eixo X.
SmallSizeY = 2 # Define a posição inicial do robô no eixo Y.
RaioSmallSize = 5 # Define o raio do robô.

while hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize) >= 0: # Enquanto a distância entre o robô e a bola for maior que a soma dos seus raios, o loop continuará.

    print("Posicao Robo: X = %.2f / Y = %.2f" % (SmallSizeX, SmallSizeY)) # Imprime a posição atual do robô.
    print("Posicao Bola: X = %.2f / Y = %.2f" % (BolaX, BolaY)) # Imprime a posição atual da bola.
    print("Diferenca: %.4f " % hypot(BolaX - SmallSizeX, BolaY - SmallSizeY)) # Imprime a distância entre o robô e a bola.
    print("Distancia: %.4f" % (hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize))) # Imprime a diferença entre a distância entre o robô e a bola e a soma dos seus raios.
    print()

    if BolaX - SmallSizeX < 0: # Se a posição da bola no eixo X for menor que a posição do robô no eixo X, o robô se move para a esquerda.
        SmallSizeX -= Velocidade
    else: # Se a posição da bola no eixo X for maior que a posição do robô no eixo X, o robô se move para a direita.
        SmallSizeX += Velocidade

    if BolaY - SmallSizeY < 0: # Se a posição da bola no eixo Y for menor que a posição do robô no eixo Y, o robô se move para baixo.
        SmallSizeY -= Velocidade
    else: # Se a posição da bola no eixo Y for maior que a posição do robô no eixo Y, o robô se move para cima.
        SmallSizeY += Velocidade

    if hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize) <= 0: # Se a distância entre o robô e a bola for menor ou igual à soma dos seus raios, a bola foi interceptada.
        print("Bola Interceptada!!!!!") # Imprime uma mensagem indicando que a bola foi interceptada.
        print("Posicao Robo: X = %.2f / Y = %.2f" % (SmallSizeX, SmallSizeY)) # Imprime a posição final do robô.
        print("Posicao Bola: X = %.2f / Y = %.2f" % (BolaX, BolaY)) # Imprime a posição final da bola.
        print("Diferenca: %.4f " % hypot(BolaX - SmallSizeX, BolaY - SmallSizeY)) # Imprime a distância final entre o robô e a bola.
        print("Distancia: %.4f" % (hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize))) # Imprime a diferença final entre a distância entre o robô e a bola e a soma dos seus raios.
        print()
