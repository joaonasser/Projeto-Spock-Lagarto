# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:50:37 2015

@author: Joao
"""
print("Vamos la, o jogo e' simples, e' um jo kem poh evoluido, fuciona assim: papel cobre pedra, pedra esmaga lagarto, lagarto envenene spock, spoc quebra tesoura, tesoura corta papel, papel refuta spock, spock vaporiza pedra, pedra destroi tesoura, tesoura decapita lagarto e finalmente, lagarto come papel. Se nao entendeu de primeira relaxa, jogando voce aprende. e' voce contra o CPU, quem ganhar 3 vezes primeiro FATURA")
derrotas =0
vitorias = 0
from random import randint
while vitorias < 3 and derrotas < 3:
    num = randint(1,5)
    if num == 1:
            comp ="p"
    elif num == 2:
            comp ="pp"
    elif num == 3:
            comp ="t"
    elif num == 4:
            comp = "l"
    else:
            comp = "s"
        
    jog = input(" escolha (p)pedra, (pp)papel, (t)tesoura, (l)lagarto ou (s)spock:")
    
    if jog == "p":
        if comp == "t":
            print('o computador escolheu TESOURA, voce venceu')
            vitorias += 1
        if comp == "pp":
            print('o computador escolheu PAPEL, voce perdeu')
            derrotas =+1
        if comp == 'l':
            print('o cumputador escolheu LAGARTO, voce venceu')
            vitorias += 1
        if comp == 's':
            print('o computador escolheu SPOCK, voce perdeu')
            derrotas =+1
    if jog == 'pp':
        if comp == 'p':
            print('o computador escolheu PEDRA, voce venceu')
            vitorias += 1
        if comp == 't':
            print('o computador escolheu TESOURA, voce perdeu')
            derrotas =+1
        if comp == 's':
            print(' o computador escolheu SPOCK, voce venceu')
            vitorias += 1
        if comp == 'l':
            print('o computador escolheu LAGARTO, voce perdeu')
            derrotas =+1
    if jog == 't':
        if comp == 'pp':
            print(' o computador escolheu PAPEL, voce venceu')
            vitorias += 1
        if comp == 'p':
            print(' o computador escolheu PEDRA, voce perdeu')
            derrotas =+1
        if comp == 's':
            print( 'o computador escolheu SPOCK, voce perdeu')
            derrotas =+1
        if comp == 'l':
            print(' o computador escolheu LAGARTO, voce venceu')
            vitorias += 1
    if jog == 's':
        if comp == 'pp':
            print(' o computador escolheu PAPEL, voce perdeu')
            derrotas =+1
        if comp == 't':
            print(' o computador escolheu TESOURA, voce venceu')
            vitorias += 1
        if comp == 'p':
            print(' o compuador escolheu PEDRA, voce venceu')
            vitorias += 1
        if comp == 'l':
            print(' o computador escolheu LAGARTO, voce perdeu')
            derrotas =+1
    if jog == 'l':
        if comp == 'p':
            print(' o computador escolheu PEDRA, voce perdeu')
            derrotas =+1
        if comp == 'pp':
            print(' o computador escolheu PAPEL, voce venceu')
            vitorias += 1
        if comp == 't':
            print(' o computador escolheu TESOURA, voce perdeu')
            derrotas =+1
        if comp == 's':
            print (' o computador escolheu SPOCK, voce venceu')
            vitorias += 1
        
    if jog == comp:
        print("empate")
