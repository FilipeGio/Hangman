def match_word(gs, wd):
    for pos, l in enumerate(wd):
        if gs == l.lower():
            word_split[pos] = gs


from random import choice

# Choosing the world
life = 1
words = ['Python', 'Average', 'Badoo']
word = choice(words)
emp_word = '_' * len(word)
word_split = []
print(word)

for c in range(len(word)):
    word_split.append('_')

print(emp_word)

while True:
    # User Input
    guess = str(input('Please choose a letter: ')).lower()

    # Check for matches
    match_word(guess, word)
    emp_word = ''
    for c in word_split:
        emp_word += c

    print(emp_word.capitalize())

    if '_' not in emp_word:
        print('Congratulations')
        break
    if guess not in word.lower():

        if life == 1:
            print('''
            _______
            |     |
            |     O
            |
            |
            ''')
        elif life == 2:
            print('''
            _______
            |     |
            |     O
            |     |
            |
            ''')

        elif life == 3:
            print('''
            _______
            |     |
            |     O
            |   / | 
            |
            ''')

        elif life == 4:
            print('''
            _______
            |     |
            |     O
            |   / | )
            |
            ''')

        elif life == 5:
            print('''
            _______
            |     |
            |     O
            |   / | )
            |    /
            ''')
        if life == 6:
            print('''
            _______
            |     |
            |     O
            |   / | )
            |    / )
            ''')
            print('Game Over')
            break

        life += 1
