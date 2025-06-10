import random
from hangman_arts import stages, logo

# reading the word file
with open ("words.txt", "r") as f:
    words = f.read().split()

secret_word = random.choice(words)
print(secret_word)

#to replace word with under scores
words_to_guess = []
for i in secret_word:
    words_to_guess.append("_")

lives = len(stages)
end_of_game = False


print(logo)

# game loop
while not end_of_game:
    guess = input("Provide a letter ! 0: (~:}").lower()
    word_lenght = len(secret_word)

    
    # print(" \nWord:", " ".join(secret_word))
    # print("Guessed letters: "," ".join(guessed_letters))
    # print("Attempts left: ", lives)
        


    for position in range(word_lenght):
        alpha = secret_word[position]

        if guess == alpha:
            words_to_guess[position] = alpha
            print(words_to_guess)
    if guess not in secret_word:
        print("You have guessed wrong, please try again \n 😁", words_to_guess)
        lives= lives -1
        print(stages[lives])


    if lives == 0:
        print("Game Over, You have Ran Out Of Lives! \n  ); Better Luck Next Time (;)")
        end_of_game= True
        print(logo)

    if "_" not in words_to_guess:
        print("You win, Congratulations    👍👍👍👍👍🙌🙌🙌🥳🥳🥳🥳🥳🥳🍾🍾🍾🍾🍾🎇🎇🎇🎇🎇🎆🎆🎆🎆🎆🥂🥂🥂🥂🥂")
        end_of_game= True
        print(logo)