import random

with open('words.txt') as f:
    words = f.read().split()

word = random.choice(words).upper()    

running = True # Feel free to change
tries = 6
guess_letters = []
w_completion = '-' * len(word)

print("----WELCOME TO HANG_MAN GAME----\n")
print()
while running and tries != 0:
    print(f"You Have {tries} {'Try' if tries == 1 else 'Tries'} Left.") # Fixing some grammar stuffs
    print(w_completion)
    guess = input('Guess a word or a letter: ').upper()
    if guess.isalpha() and (len(guess) == 1 or len(guess) == len(word)):
        if guess == word:
            print()
            print('----HORRAY. YOU GOT IT!---')
            running = False
        elif guess in word:
            guess_letters.append(guess)
            tries -= 1
        else:
            print(f"{guess} Is Not Included!\n")
            tries -= 1
    else:
        print('INVALID INPUT!\n')

    word_as_list = list(w_completion)
    for i, letter in enumerate(word):
        if letter == guess:
            word_as_list[i] = guess
    w_completion = ''.join(word_as_list)
    
    if '-' not in w_completion:
        print()
        print(w_completion)
        print('**** YOU WON ****\n')
        running = False

if tries == 0:
    print('XXXX YOU RAN OUT OF TRIES AND DIED!!! XXXX\n')
