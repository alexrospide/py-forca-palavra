# Script para criar o arquivo contendo as palavras do jogo

palavras = ['banana',
            'laranja',
            'canela',
            'caranguejo',
            'kiwi',
            'ameixa',
            'manga',
            'maça',
            'melancia',
            'pera',
            'goiaba',
            'mirtilo',
            'uva',
            'cereja',
            'paralelepipedo',
            'torpedo',
            'navio']


nome_arquivo = 'palavras.txt'


def cria_arquivo():
    print('Criando arquivo')

    with open(nome_arquivo, 'w+') as arquivo:
        for palavra in palavras:
            arquivo.write(palavra)
            arquivo.write('\n')


#cria_arquivo()
