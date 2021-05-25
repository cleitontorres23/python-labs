import random

print('*********************************')
print('****WELCOME TO HANGMAN GAME!*****')
print('*********************************')

file = open("words.txt", 'r')
line = file.readline()

print("Let's play...This is the word:")

you_right = False
you_hang = False
words = []

for lines in file:
    lines = lines.strip()
    words.append(lines)

number = random.randrange(0, len(words))
secret_word = words[number].upper()
right_letters = ['_' for letter in secret_word]
#print(right_letters)
print(secret_word)

while(not you_right and not you_hang):
    guess = input("Guess Letter? \n")
    guess = guess.strip().upper()
    if guess in secret_word:
        position = 0
        for letter in secret_word:
            if (guess.upper() == letter.upper()):
                right_letters[position] = letter
                print("You found the letter {} in position {}.".format(letter, position))
                print(right_letters)
            position += 1
    else:
        you_hang += 1
        print("Sorry, you have hanged!")

file.close