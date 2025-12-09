import random
import os
import hangman_art 
import hangman_word_list 

chosen_word = hangman_word_list.word_list[random.randint(0, len(hangman_word_list.word_list) - 1)]

wrong_letter = 0
correct_letters = []
letters = []
new_word = "_" * len(chosen_word)
gameover = False
guess = ""

while gameover != True:


      print(f"\n**********{6-wrong_letter} LIVES LEFT**********")
      print(new_word)

      print(hangman_art.stages[wrong_letter])
      new_word = ""

      guess = input("\nChoose a letter: ").lower()

      for letter in chosen_word:

            if letter == guess:
                  new_word += letter
                  correct_letters.append(guess)

            elif letter in correct_letters:
                  new_word += letter

            else:
                  new_word += "_"
                  
      os.system("cls")

      if (guess not in correct_letters) and (guess not in letters):
            print("The letter is not in the word!")
            wrong_letter += 1

      if guess in letters:
            print("\nYou've already tried this letter!")
      

      letters.append(guess)

      
      if "_" not in new_word:
            gameover = True
            os.system("cls")
            print(f"The word was: {chosen_word}\n\n**********You won!**********")

      elif wrong_letter == 6:
            gameover = True
            os.system("cls")
            print(f"\nThe word was: {chosen_word}\n\n**********You lose!**********")