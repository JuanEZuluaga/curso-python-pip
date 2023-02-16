import random

def choose_options():
  options = ('papel', 'tijera', 'piedra')
  user_option = input('Elige Piedra, papel o tijera: ').lower()
  computer_option = random.choice(options)
  if not user_option in options:
    return None
  return user_option, computer_option


def check_rules(user_option,computer_option,user_wins,computer_wins):
  if user_option == computer_option:
        print('Empate causita')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('Ganaste causa')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Perdiste causa')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('Ganaste causa')
      user_wins += 1
    else:
      print('Tijera gana a papel')
      print('Perdiste Causita')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('Ganaste causita')
      user_wins += 1
    else:
      print('Piedra gana a tijera')
      print('Perdiste causa')
      computer_wins += 1
  return user_wins,computer_wins


def check_winner(user_wins,computer_wins):
  if user_wins == 2:
    return 'User Win'
  else:
    return 'Computer Win'


def main():
  user_wins = 0
  computer_wins = 0
  rounds = 1

  while user_wins < 2 and computer_wins < 2:

    print('*'*10)
    print('ROUND',rounds)
    print('*'*10)

    user_option, computer_option = choose_options()
    
    if user_option == None:
      continue
    
    rounds += 1
    
    user_wins , computer_wins = check_rules(user_option,computer_option,user_wins,computer_wins)

  print(check_winner(user_wins,computer_wins))
  

if __name__ == '__main__':
  main()