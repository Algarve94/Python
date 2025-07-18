import pygame
pygame.init()
pygame.mixer_music.load('Pizzaria.mp3')
pygame.mixer_music.play()
pygame.event.wait()
import emoji
(input(emoji.emojize('Olá, bem vindo ao Mundo da Pizza!:pizza:', language= 'alias')))
(input((emoji.emojize('Veja em nosso cardápio e encontre nossas famosas pizzas :sunglasses:', language= 'alias'))))
r = int(input('''Lista de pizzas: 
Pepperoni [ 1 ]
Mussarela [ 2 ]
Calabresa [ 3 ]
Margueritta [ 4 ]
Qual sua preferência?: '''))
valor = '79.90'
from time import sleep
if r == 1:
    sleep(1)
    print('Você escolheu Pepperoni')
elif r == 2:
    sleep(1)
    print('Você escolheu Mussarela')
elif r == 3:
    sleep(1)
    print('Você escolheu Calabresa')
else:
    sleep(1)
    print('Ótima escolha!! Você escolheu Margueritta')
sleep(1)
p = int(input('''Qual sua forma de pagamento?
1 - Dinheiro
2 - Débito
3 - Crédito \n'''))
if p == 1:
    sleep(1)
    print('O valor ficou em {}R${}{}'.format('\033[1;30;42m' ,valor, '\033[m'))
elif p == 2:
    sleep(1)
    print('O valor ficou em {}R${}{}'.format('\033[1;30;42m' ,valor, '\033[m'))
    sleep(1)
elif p == 3:
    sleep(1)
    print('O valor ficou em {}R${}{}'.format('\033[1;30;42m' ,valor, '\033[m'))
    parcela = int(input('Em quantas vezes deseja parcelar? \n2x\n3x\n'))
    parcela2 = 79.90 / 2
    parcela3 = 79.90 / 3
    if parcela == 2:
        sleep(1)
        print('O valor ficou em {}R${:.2f}{}'.format('\033[1;30;42m', parcela2, '\033[m'))
    else:
        sleep(1)
        print('O valor ficou em {}R${:.2f}{}'.format('\033[1;30;42m', parcela3, '\033[m'))
sleep(1)
print('Obrigado pela preferência! Até breve...')





