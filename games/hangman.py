import random


def play():
    welcome()
    secret_word = secret() 
    print(secret_word)
    
    rights = right_letters(secret_word)
    
    you_right = False
    you_hang = False
    errors = 0 
    
    while(not you_right and not you_hang):
        guess = guess_input()
        print(secret_word)
        if ( guess in secret_word ):
            guess_right(guess,rights,secret_word)
            print(rights)
        elif(errors == 2):
            #you_hang += 1
            print("You have one more change!")
            errors += 1
        else:
            lose_message(secret_word)
        #you_right = '_' not in rights
    
    if (you_right):
        win_message()
    elif(errors == 2):
        lose_message()


def welcome():
    print('*********************************')
    print('****WELCOME TO HANGMAN GAME!*****')
    print('*********************************')

def secret():
    with open("words.txt", 'r') as file:
        line = file.readline()
        words = []

        for lines in file:
            lines = lines.strip()
            words.append(lines)

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def right_letters(words):
    return ['_' for letter in words]

    
def guess_input():
    guess = input("Guess Letter: \n")
    guess = guess.strip().upper()
    return guess

def guess_right(guess,rights,secret_word):
    position = 0
    for letter in secret_word:
        if (guess == letter):
            rights[position] = letter
            print("You found the letter {} in position {}.".format(letter, position))
        position += 1


def win_message():
    print('CONGRATS, YOU WIN ! ! !   ')
    print("      ___________         ")
    print("     '._==_==_=_.'        ")
    print("    .-\\:     /-.         ")
    print("   | (|:.    |) |         ")
    print("    '-|:.    |-'          ")
    print("     \\::.    /           ")
    print("     '::.   .'            ")
    print("         ) (              ")
    print("       _.' '._            ")
    print("      '-------'           ")

def lose_message(secret_word):
    print('OH NO !, YOU HAVE HANGED! ')
    print('THE SECRET WORD IS: {}'.format(secret_word)  )
    print("         _______________              ")
    print("        /               \             ")
    print("       /                 \            ")
    print("    /\/                   \/\         ")
    print("    \ |   XXXX     XXXX   | /         ")
    print("     \|   XXXX     XXXX   |/          ")
    print("      |    XX       XX    |           ")
    print("      |                   |           ")
    print("       \__     XXX      __/           ")
    print("         |\    XXX    /|              ")
    print("         | |         | |              ")
    print("         | I I I I I I |              ")
    print("         | I I I I I I |              ")
    print("         \_          _/               ")
    print("           \_      _/                 ")
    print("             \____/                   ")

play()