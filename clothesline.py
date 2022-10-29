import random



frame0 = \
    r"""
    
=====!=====!=======!=====!=======!=====!=======!=====!=====
    /'''V'''\     /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |       |     |
     |     |       |     |       |     |       |     |
     ```````       ```````       ```````       ```````


"""
frame1 = \
    r"""
=====!=====!=======!=====!=======!=====!=======!===========
    /'''V'''\     /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |       |     |      |   |
     |     |       |     |       |     |      |   |
     ```````       ```````       ```````      `-._|


"""
frame2 =\
    r"""
=====!=====!=======!=====!=======!=====!===================
    /'''V'''\     /'''V'''\     /'''V'''\
   /         \   /         \   /         \
  '-"|     |"-' '-"|     |"-' '-"|     |"-'
     |     |       |     |       |     |
     |     |       |     |       |     |
     ```````       ```````       ```````
                                            _.~.,_.._
                                             ```````

"""
frame3 =\
    r"""
=====!=====!=======!=====!=======!=========================
    /'''V'''\     /'''V'''\     /'\
   /         \   /         \   /   .\
  '-"|     |"-' '-"|     |"-'  '|  ='
     |     |       |     |      |   |
     |     |       |     |      |   |
     ```````       ```````      `-._|
                                            _.~.,_.._
                                             ```````
"""
frame4 =\
    r"""
=====!=====!=======!=====!=================================
    /'''V'''\     /'''V'''\
   /         \   /         \
  '-"|     |"-' '-"|     |"-'
     |     |       |     |
     |     |       |     |
     ```````       ```````
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""
frame5 =\
    r"""
=====!=====!=======!=======================================
    /'''V'''\     /'\
   /         \   /   .\
  '-"|     |"-'  '|  ='
     |     |      |   |
     |     |      |   |
     ```````      `-._|
                              _.~.,_.._     _.~.,_.._
                               ```````       ```````
"""
frame6 =\
    r"""
=====!=====!===============================================
    /'''V'''\
   /         \
  '-"|     |"-'
     |     |
     |     |
     ```````
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""
frame7 =\
    r"""
=====!=====================================================
    /'\
   /   .\
   '|  ='
    |   |
    |   |
    `-._|
                _.~.,_.._     _.~.,_.._     _.~.,_.._
                 ```````       ```````       ```````
"""
frame8 =\
    r"""
===========================================================






  _.~.,_.._     _.~.,_.._     _.~.,_.._     _.~.,_.._
   ```````       ```````       ```````       ```````
"""




def clear_screen():
    print("\033[H\033[J", end="")


def is_letter_in_word(letter, word):
    if letter in word:
        return "True"
    if letter not in word:
        return "False"

def print_clothesline(wrong_gueses):
    #print("You have " + str(8-wrong_gueses) + " chances left.")
    if wrong_gueses == 0:
        print(frame0)
    if wrong_gueses == 1:
        print(frame1)
    if wrong_gueses == 2:
        print(frame2)
    if wrong_gueses == 3:
        print(frame3)
    if wrong_gueses == 4:
        print(frame4)
    if wrong_gueses == 5:
        print(frame5)
    if wrong_gueses == 6:
        print(frame6)
    if wrong_gueses == 7:
        print(frame7)
    if wrong_gueses == 8:
        print(frame8)

def update_guess(old_guess, letter,  word):
    new_guess = ""
    for index in range(len(old_guess)):
        if word[index] == letter:
            new_guess = new_guess + letter
        else:
            new_guess = new_guess + old_guess[index]
    return new_guess

def pick_secret_word():
    
    secret_word_options = ["apple", "banana", "grape", "door", "cat", "dog", "home",]
    random_secret_word = random.choice(secret_word_options)
    return random_secret_word




def main():
    clear_screen()
    letters_guessed = []
    secret_word = pick_secret_word()
    message = ("The secret word is: ")
    secret_word_length = len(secret_word)
    #print(secret_word + " " + str(secret_word_length))

    #guess = ("-"*secret_word_length)
    #print(guess)

    print("Welcome to Clothesline!\n\n")

    guess = ("-"*secret_word_length)


    incorrect_count = (0)
    while incorrect_count < 8:
        #print("Word:   " + guess + "\n")
        print_clothesline(incorrect_count)
        print("Word:   " + guess + "\n")
        print("Guessed:" )
        print(letters_guessed)
        
        letter = input("Guess a latter...If you dare! ")
        letters_guessed.append(letter)
       
        result = is_letter_in_word(letter, secret_word)
        if result == "True":
            print("Correct!")
            guess = update_guess(guess, letter, secret_word)
            if secret_word == guess:
                print("Final Word: " + secret_word)
                print("YOU WON!!!!")
                return
        else:
            print("Incorrect!")
            incorrect_count = incorrect_count + 1
            if incorrect_count == 8:
                
                clear_screen()
                print("Word:   " + guess + "\n")
                print_clothesline(incorrect_count)
                print("Guessed:" )
                print(letters_guessed)

                print("NO MORE CHANCES,YOU LOSE :(")
                return
        
        clear_screen()
    









main()    








