from math import hypot

# Velocidade de Atualizacao
Velocidade = 0.02

# Posicao inicial Robo
SmallSizeX = 1
SmallSizeY = 1
RaioSmallSize = 3

# Raio da bola.
RaioBola = 1 

# Le os valores do arquivo 
with open("trajetoBola.txt", 'r') as arquivo_trajeto:
    linhas_trajeto = arquivo_trajeto.readlines()[1:]  # Ignora o cabeçalho

# Abre o arquivo trajetoRobo.txt
with open("trajetoRobo.txt", 'w') as arquivo_saida:
    # Itera sobre as linhas e extrai os valores iniciais de BolaX e BolaY
    for linha in linhas_trajeto:
        colunas = linha.split('\t')
        BolaX = float(colunas[1].replace(',', '.'))
        BolaY = float(colunas[2].replace(',', '.'))
        
        # Loop principal
        while hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize) >= 0:
            # Joga as informacoes do trajeto no arquivo 
            arquivo_saida.write(f"Posicao Robo: X = {SmallSizeX:.2f} / Y = {SmallSizeY:.2f}\n")
            arquivo_saida.write(f"Posicao Bola: X = {BolaX:.2f} / Y = {BolaY:.2f}\n")
            arquivo_saida.write(f"Diferenca: {hypot(BolaX - SmallSizeX, BolaY - SmallSizeY):.4f}\n")
            arquivo_saida.write(f"Distancia: {hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize):.4f}\n\n")

            if BolaX - SmallSizeX < 0:
                SmallSizeX -= Velocidade
            else:
                SmallSizeX += Velocidade

            if BolaY - SmallSizeY < 0:
                SmallSizeY -= Velocidade
            else:
                SmallSizeY += Velocidade

            # Atualiza os valores de BolaX e BolaY para o próximo instante de tempo
            BolaX = float(colunas[1].replace(',', '.'))
            BolaY = float(colunas[2].replace(',', '.'))

            if hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize) <= 0:
                arquivo_saida.write("Bola Interceptada!!!!!\n")
                arquivo_saida.write(f"Posicao Robo: X = {SmallSizeX:.2f} / Y = {SmallSizeY:.2f}\n")
                arquivo_saida.write(f"Posicao Bola: X = {BolaX:.2f} / Y = {BolaY:.2f}\n")
                arquivo_saida.write(f"Diferenca: {hypot(BolaX - SmallSizeX, BolaY - SmallSizeY):.4f}\n")
                arquivo_saida.write(f"Distancia: {hypot(BolaX - SmallSizeX, BolaY - SmallSizeY) - (RaioBola + RaioSmallSize):.4f}\n\n")
                break  # Sai do loop quando a bola é interceptada
