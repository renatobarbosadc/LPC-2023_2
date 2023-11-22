#importações
import random
import string

#constantes
CONST_FRASE = "METHINKS IT IS LIKE A WEASEL"
CONST_COPIES_SIZE = 100
CONST_PROB = 5

#funções
def gera_char():
    return random.choice(string.ascii_uppercase + " ")

def gera_string_inicial():
    frase_auxiliar = ''
    for cont in range(0, 28):
        frase_auxiliar = frase_auxiliar + gera_char()
    return  frase_auxiliar

def retorna_frase(frase_auxiliar):
    frase = frase_auxiliar
    for x in range(0,28):
        prob = random.randint(1, 100)
        if prob <= 5:
            frase = frase[:x] + gera_char() + frase[x+1:]
    return frase

def adiciona_cem_frases(frase_auxiliar):
    lista_auxiliar = []
    for i in range(0, CONST_COPIES_SIZE):
        frase = retorna_frase(frase_auxiliar)
        lista_auxiliar.append(frase)
    return lista_auxiliar

def retorna_melhor_frase(lista_auxiliar):
    lista_pontos = []
    for i in lista_auxiliar:
        pontuacao = 0
        for j in range(0, 28):
            if i[j] == CONST_FRASE[j]:
                pontuacao = pontuacao + 1
        lista_pontos.append(pontuacao)
    posicao_melhor = lista_pontos.index(max(lista_pontos))
    melhor_frase = lista_auxiliar[posicao_melhor]
    return melhor_frase

def main():
    frase_base = gera_string_inicial()
    lista_frases = []
    contador_geracoes = 0
    string_encontrada = False
    while not string_encontrada:
        lista_frases.clear()
        lista_frases = adiciona_cem_frases(frase_base)
        frase_base = retorna_melhor_frase(lista_frases)
        if(frase_base == CONST_FRASE):
            string_encontrada = True
        contador_geracoes = contador_geracoes + 1
        print(frase_base)
        print(contador_geracoes)
main()
