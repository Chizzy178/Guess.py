word = "Chijioke"
guess_word = ""
guess_count = 3
guesses = 0
out_of_guesses = True

while guess_word != word and out_of_guesses:
    if guesses != guess_count:
        guess_word = input("Guess the correct word: ")
        guesses += 1
    else:
        out_of_guesses = False

if out_of_guesses == False:
    print("Sorry, your chances are used up")
else:
    print("Congrats, you did it!")
    
