while True:
    print('Veuillez saisir une phrase affirmative commencant pas L et se termine par un point')
    phrase = input()

    if phrase.startswith('L') and phrase.endswith('.'):
        break
    else:
        print('respecter les regles svp')
