print('*********************************')
print('****WELCOME TO HANGMAN GAME!*****')
print('*********************************')

secret = 'banana'
list_letter = ['_', '_', '_', '_', '_', '_']
print("Let's play...This is the word:")
print(list_letter)
you_right = False
you_hang = False

while(not you_right and not you_hang):
    guess = input("Letter? \n")
    if guess in secret:
        position = 0
        for letter in secret:
            if guess.upper() == letter.upper():
                list_letter[position] = letter
                print("You found the letter {} in position {}.".format(letter, position))
                print(list_letter)
            position += 1
    else:
        you_hang += 1

