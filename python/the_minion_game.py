def minion_game(string):
    vogais = ['A', 'E', 'I', 'O', 'U']
    jogadores = {'Kevin': 0, 'Stuart': 0}
    for i in range(len(string)):
        if string[i] in vogais:
            jogadores['Kevin'] += len(string) - i
        else:
            jogadores['Stuart'] += len(string) - i
    if jogadores['Kevin'] > jogadores['Stuart']:
        print(f"Kevin {jogadores['Kevin']}")
    elif jogadores['Stuart'] > jogadores['Kevin']:
        print(f"Stuart {jogadores['Stuart']}")
    elif jogadores['Kevin'] == jogadores['Stuart']:
        print("Draw")


minion_game("BANANA")  # Esperado: "Stuart 12"

