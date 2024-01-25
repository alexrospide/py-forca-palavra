# Jogo da Forca utilizando Programação Orientada a Objetos
import random
import banco_de_palavras as cria_arquivo_palavras

# Palco da Forca
palco = ['', 'O', 'O-', 'O-|', 'O-|-', 'O-|-<']


# Classe
class Forca:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.palavra_oculta = ''
        self.tentativas_incorretas = 0
        self.letras_corretas = []
        self.letras_erradas = []
        self.descobre_palavra = []

    # Método para adivinhar a letra
    def advinha(self, letra):
        acertou = letra in self.palavra
        if acertou:
            self.letras_corretas.append(letra)
            index = 0
            for i in self.palavra:
                if i == letra:
                    n = list(self.palavra_oculta)
                    n[index] = letra
                    self.palavra_oculta = ''.join(n)
                index += 1
        else:
            self.letras_erradas.append(letra)
            self.tentativas_incorretas += 1
        print(self.palavra_oculta)

    # Método para verificar se o jogo terminou
    def forca_acabou(self):
        print(f'Tentativas incorretas: {self.tentativas_incorretas}')
        if self.forca_venceu() or self.tentativas_incorretas == 4:
            return True
        return False

    # Método para verificar se o jogador venceu
    def forca_venceu(self):
        if self.palavra_oculta == self.palavra:
            return True
        return False

    def palavra_escondida(self):
        for i in range(len(self.palavra)):
            self.palavra_oculta += '-'

    # Método para checar o status do jogo e imprimir o palco na tela
    def mostra_status_jogo(self):
        print('=== Boneco da Forca ===')
        boneco = palco[len(self.letras_erradas)]
        print(boneco)

        print('=== Palavra Oculta ===')
        print(self.palavra_oculta)
        print(f'A palavra tem {len(self.palavra_oculta)} letras')

        print('=== Letras Corretas ===')
        print(self.letras_corretas)
        for letra in self.letras_corretas:
            print(letra)

        print('=== Letras Erradas ===')
        print(f'{self.letras_erradas}')


# Função para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():
    with open("palavras.txt", "rt") as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco)-1)].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    cria_arquivo_palavras.cria_arquivo()
    jogo = Forca(palavra_aleatoria())
    jogo.palavra_escondida()

    # Enquanto o jogo não tiver terminado, mostrar do status,
    # solicita uma letra e faz a leitura do caracter
    # Verifica o status do jogo

    while not jogo.forca_acabou():
        print('~~~~~ >  Jogo da Forca!')

        jogo.mostra_status_jogo()

        letra = str(input('\nDigite uma letra: '))

        jogo.advinha(letra)

        # De acordo com o status, imprime mensagem na tela para o usuário
        if jogo.forca_venceu():
            print('\nParabéns! Você ganhou!!')
            break
        elif jogo.forca_acabou():
            print('\nFinal do Jogo! Você perdeu.')
            print('A palavra era ' + jogo.palavra)

            print('\nFoi bom jogar com você! \n')
            break


# Executa o programa
if __name__ == "__main__":
    main()
