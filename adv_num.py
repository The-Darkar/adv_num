import random

def num(x):
  aleat = random.randint(1, x)
  num = 0
  while num != aleat:
    num = int(input('Digite um número entre 1 e 10: '))
    if num < aleat:
      print('\n \n Você Errou! \n tente mais alto. \n \n')
    elif num > aleat:
      print('\n \n Você Errou! \n tente mais baixo.\n \n')
  print(f'\n \n Parabéns você acertou! \n O número correto é {aleat} \n \n')

num(10)