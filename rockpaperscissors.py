import random
while True:
 player_action = input('Qual a sua jogada? (pedra, papel, tesoura):')
 possible_action = ['pedra', 'papel', 'tesoura']
 computer_action = random.choice(possible_action)

 print(f'Você escolheu {player_action} o computador escolheu {computer_action}')

 if player_action == computer_action:
  print('Empate! ')
 elif player_action == 'pedra':
  if computer_action == 'tesoura':
   print('Você ganhou! Pedra esmaga tesoura. ')
  else:
   print('Você perdeu! Papel engole a pedra. ')
 elif player_action == 'tesoura':
  if computer_action == 'pedra':
   print('Você perdeu! Pedra esmaga tesoura. ')
  else:
   print('Você ganhou! Tesoura corta papel. ')
 elif player_action == 'papel':
   if computer_action == 'pedra':
    print('Você ganhou! Papel engole pedra. ')
   else:
    print('Você perdeu! Tesoura corta papel.. ')
 play_again = input("Jogar novamente (s/n): ")
 if play_again.lower() != "s":
  break



























