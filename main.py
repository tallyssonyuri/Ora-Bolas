import math
import matplotlib.pyplot as plt

# Definindo as propriedades do robô
robo = {'raio': 0.09, 'velocidade': 0.056, 'posicao': [2, 2]}

# Solicitar ao usuário para definir as posições iniciais do robô
robo['posicao'][0] = float(input("Digite a posição inicial x do robô: "))
robo['posicao'][1] = float(input("Digite a posição inicial y do robô: "))
print("")

# tamanho = min( len(), len())
# for x in range tamanho:
  #lista2.append(lista1[x])

trajetoria_robo = []
trajetoria_bola =[]
velocidades_robo = []
velocidades_bola = []
aceleracao_robo = []
aceleracao_bola = []
# Definindo as propriedades do robô


def calcula_aceleracao(velocidades_robo, velocidades_bola):
    for i in range(1, len(velocidades_robo)):
        ax = (velocidades_robo[i][0] - velocidades_robo[i-1][0])/0.02
        ay = (velocidades_robo[i][1] - velocidades_robo[i-1][1])/0.02

        aceleracao_robo.append([ax, ay])

    for i in range(1, len(velocidades_bola)):
        ax = (velocidades_bola[i][0] - velocidades_bola[i-1][0])/0.02
        ay = (velocidades_bola[i][1] - velocidades_bola[i-1][1])/0.02

        aceleracao_bola.append([ax, ay])

def calcula_velocidade(trajetoria_robo, trajetoria_bola):
    for i in range(1, len(trajetoria_robo)):
        p1 = float(trajetoria_robo[i][0])
        p2 = float(trajetoria_robo[i-1][0])
        vx = (trajetoria_robo[i][0] - trajetoria_robo[i-1][0])/0.02
        vy = (trajetoria_robo[i][1] - trajetoria_robo[i-1][1])/0.02

        velocidades_robo.append([vx, vy])

    for i in range(1, len(trajetoria_bola)):
        vx = (trajetoria_bola[i][0] - trajetoria_bola[i-1][0])/0.02
        vy = (trajetoria_bola[i][1] - trajetoria_bola[i-1][1])/0.02

        velocidades_bola.append([vx, vy])

    calcula_aceleracao(velocidades_robo, velocidades_bola)

# Função para calcular a distância entre o robô e a bola
def calcular_distancia(pos1, pos2):
  return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Função para mover o robô em direção à bola
def mover_robo(robo, bola):
    # Calcular a direção do movimento
    direcao = [bola['posicao'][0] - robo['posicao'][0], bola['posicao'][1] - robo['posicao'][1]]
    # Normalizar a direção
    norma = math.sqrt(direcao[0]**2 + direcao[1]**2)
    direcao = [direcao[0]/norma, direcao[1]/norma]
    # Atualizar a posição do robô
    trajetoria_robo.append([robo['posicao'][0], robo['posicao'][1]])

    robo['posicao'][0] += direcao[0] * robo['velocidade']
    robo['posicao'][1] += direcao[1] * robo['velocidade']

# Função para mover a bola com base nas posições lidas de um arquivo
def mover_bola(bola, linha):
    # Dividir a linha em colunas
    colunas = linha.split()
    # Atualizar a posição da bola com os valores lidos do arquivo
    bola['posicao'] = [float(colunas[1].replace(',', '.')), float(colunas[2].replace(',', '.'))]

# Função principal para executar a simulação
def simular_jogo(robo, linhas, raio_bola):
  # Inicializar a bola
  bola = {'raio': raio_bola, 'velocidade': 2.55, 'posicao': [0, 0]}

  # Definir o raio inicial da bola
  raio_bola = 0.0215

  # Inicializar listas para armazenar dados para plotagem
  tempo = []
  posicoes_robo = []
  posicoes_bola = []
  distancias = []

  # Mover a bola para a primeira posição lida do arquivo
  for i, linha in enumerate(linhas):
      mover_bola(bola, linha)
      mover_robo(robo, bola)
      print(f"Tempo: {i*0.02:.2f}s, Posição do robô: [{robo['posicao'][0]:.3f}, {robo['posicao'][1]:.3f}], Posição da bola: [{bola['posicao'][0]:.3f}, {bola['posicao'][1]:.3f}]")
      print()

      # Armazenar dados para plotagem
      tempo.append(i*0.02)
      posicoes_robo.append(robo['posicao'][:])
      posicoes_bola.append(bola['posicao'][:])
      distancias.append(calcular_distancia(robo['posicao'], bola['posicao']))

      if calcular_distancia(robo['posicao'], bola['posicao']) <= robo['raio'] + bola['raio']:
          print(f"O robô alcançou a bola no tempo {i*0.02:.2f}s, na posição [{robo['posicao'][0]:.3f}, {robo['posicao'][1]:.3f}]")
          break

  calcula_velocidade(trajetoria_robo, trajetoria_bola)

  while True:
  # Menu para o usuário escolher quais gráficos exibir
    print("")
    print("")
    print("Escolha quais gráficos você gostaria de exibir:")
    print("")
    print("1. Trajetórias da bola e do robô")
    print("2. Posições da bola e do robô")
    print("3. Distância entre a bola e o robô")
    print("4. Componentes da velocidade da bola e do robô")
    print("5. Componentes da aceleração da bola e do robô")
    print("6. Aprofundamento")
    print("7. Sair")
    print("")
    escolha = input("Digite o número correspondente à sua escolha: ")
  
    # Plotar gráficos de acordo com a escolha do usuário
    if escolha == '7':
      print("Fim!")
      break
    elif escolha == '1':
        # Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦
        plt.figure(figsize=(10, 12))
        plt.subplot(3, 2, 1)
        plt.plot([pos[0] for pos in posicoes_robo], [pos[1] for pos in posicoes_robo], label='Robô')
        plt.plot([pos[0] for pos in posicoes_bola], [pos[1] for pos in posicoes_bola], label='Bola')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Trajetórias da bola e do robô')
        plt.legend()
        plt.show()
    elif escolha == '2':
      # Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡
      plt.figure(figsize=(10, 12))

      # Gráfico da posição x do robô e da bola em função do tempo
      plt.subplot(2, 1, 1)
      plt.plot(tempo, [pos[0] for pos in posicoes_robo], label='Robô x')
      plt.plot(tempo, [pos[0] for pos in posicoes_bola], label='Bola x')
      plt.xlabel('Tempo (s)')
      plt.ylabel('Posição x')
      plt.title('Posições x da bola e do robô')
      plt.legend()

      # Gráfico da posição y do robô e da bola em função do tempo
      plt.subplot(2, 1, 2)
      plt.plot(tempo, [pos[1] for pos in posicoes_robo], label='Robô y')
      plt.plot(tempo, [pos[1] for pos in posicoes_bola], label='Bola y')
      plt.xlabel('Tempo (s)')
      plt.ylabel('Posição y')
      plt.title('Posições y da bola e do robô')
      plt.legend()

      plt.tight_layout()
      plt.show()

    elif escolha == '3':
        # Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo 𝑡
        plt.figure(figsize=(10, 12))
        plt.subplot(3, 2, 3)
        plt.plot(tempo, distancias, label='Distância')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Distância')
        plt.title('Distância entre a bola e o robô')
        plt.legend()
        plt.show()
    elif escolha == '4':
        # Gráfico dos componentes vx e vy da velocidade da bola e do robô
        plt.figure(figsize=(10, 12))
        plt.subplot(3, 2, 4)
        tamanho = min(len(velocidades_bola), len(velocidades_robo))
        lista1 = []
        lista2 = []
  
        for x in range (tamanho):
          lista1.append([velocidades_bola[0], velocidades_bola[1]])
          lista2.append([velocidades_robo[0], velocidades_robo[1]])
  
        plt.plot(tempo[:-1], [vel[0] for vel in lista2], label='Robô vx')
        plt.plot(tempo[:-1], [vel[1] for vel in lista2], label='Robô vy')
        plt.plot(tempo[:-1], [vel[0] for vel in lista1], label='Bola vx')
        plt.plot(tempo[:-1], [vel[1] for vel in lista1], label='Bola vy')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Velocidade')
        plt.title('Componentes da velocidade da bola e do robô')
        plt.legend()
        plt.show()
    elif escolha == '5':
        # Gráfico dos componentes ax e ay da aceleração da bola e do robô
        plt.figure(figsize=(10, 12))
        plt.subplot(3, 2, 5)
  
        tamanho2 = min(len(aceleracao_bola), len(aceleracao_robo))
        lista3 = []
        lista4 = []
  
        for x in range(tamanho2):
           lista3.append([aceleracao_robo[0], aceleracao_robo[1]])
           lista4.append([aceleracao_bola[0], aceleracao_bola[1]])
  
        plt.plot(tempo[:-2], [acc[0] for acc in lista3], label='Robô ax')
        plt.plot(tempo[:-2], [acc[1] for acc in lista3], label='Robô ay')
        plt.plot(tempo[:-2], [acc[0] for acc in lista4], label='Bola ax')
        plt.plot(tempo[:-2], [acc[1] for acc in lista4], label='Bola ay')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Aceleração')
        plt.title('Componentes da aceleração da bola e do robô')
        plt.legend()
        plt.show()
    elif escolha == '6':
      print("")
      print("Em nosso aprofundamento, decidimos seguir para testar o quanto o raio de interceptação pode influenciar no algoritmo")
      print("")
      print("E após diversos testes notamos que quanto maior for a soma dos raios, menor será o tempo para interceptação, e quanto menor for a soma do raios, maior será o tempo de interceptação!")
      print("")
      print("Você pode alterar o raio da bola para o valor que quiser e ver como fica na pratica!")
      print("")
      print("OBS. Lembrando que o raio original da bola na categoria Robo SmallSize possui cerca de 0.0215m, ou seja, um pouco mais de 2cm, o valor para teste será considerado em metros.")
      print("")
      raio_bola = float(input("Digite o novo raio da bola: "))
      print("")
      print("Segue abaixo as novas posições do robo e da bola com o novo raio informado:")
      print("")
      # Reiniciar as listas de dados
      tempo = []
      posicoes_robo = []
      posicoes_bola = []
      distancias = []
      # Executar a simulação com o novo raio da bola
      simular_jogo(robo, listaLinhasTrajBola, raio_bola)

# Abrir o arquivo de texto com as posições da bola
with open('trajetoBola.txt', 'r') as arquivo: # Abre o arquivo txt fornecido no moodle
  listaLinhasTrajBola = arquivo.readlines() # Lê as linhas contidas no txt

matriz_de_posicao = [] # montamos a matriz que terá as posições da bola

for linha in range( len( listaLinhasTrajBola ) ): # Percorremos as linhas contidas no txt

  dadosLinha = listaLinhasTrajBola[linha].strip('\n' ) # Tira a quebra de linha
  dadosLinha = dadosLinha.replace( ",","." ) # Troca a virgula por ponto
  dadosLinha = dadosLinha.split( "\t" ) # Separa os dados de acordo com o espaço do arquivo

  matriz_de_posicao.append(dadosLinha) # Inserimos as informações de acordo com cada linha e coluna da matriz

  trajetoria_bola.append([float(matriz_de_posicao[linha][1]), float(matriz_de_posicao[linha][2])])

# Executar a simulação
simular_jogo(robo, listaLinhasTrajBola, 0.0215)