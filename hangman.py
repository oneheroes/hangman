# Write your code here
import random



possible_answers = ['python', 'java', 'kotlin', 'javascript']
correct_number = random.randint(0, 3)
correct_answer = possible_answers[correct_number]
length_of_answer = len(correct_answer)
hidden_password = "-" * length_of_answer
hidden_password_list = list(hidden_password)
lives_left = 8
guessed_letters = []
english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play = "play"

print("H A N G M A N")
while play != 'exit':

    print('Type "play" to play the game, "exit" to quit:')
    play = input()
    if play == "exit":
        break
    elif play != 'exit' and play != 'play':
        continue
    elif play == 'play':
        lives_left = 8
        while lives_left > 0:

            print("")
            print(hidden_password)
            guess_letter = input("Input a letter: ")
            if len(guess_letter) > 1:
                print("You should input a single letter")
                continue
            if guess_letter not in english_alphabet:
                print("Please enter a lowercase English letter")
                continue
            if guess_letter in guessed_letters:
                print("You've already guessed this letter")
                continue
            elif guess_letter not in guessed_letters:
                guessed_letters.append(guess_letter)

            if guess_letter in correct_answer:
                for y in range(0,len(correct_answer)):
                    if guess_letter == correct_answer[y]:
                        hidden_password_list[y] = guess_letter
                        hidden_password = "".join(hidden_password_list)
                        if hidden_password == correct_answer:
                            lives_left = 0
                            print("")
                            print(hidden_password)
                            print("You guessed the word!")
                            print("You survived!")
                            print("")
            elif guess_letter not in correct_answer:
                    print("That letter doesn't appear in the word")
                    lives_left -= 1

                    if lives_left == 0:
                        print("You lost!")
                        print("")
                        # while play != 'play':
                        #     print('Type "play" to play the game, "exit" to quit:')
                        #     play = input()
                        #     if play == "exit":
                        #         break
                        #     elif play != 'exit' and play != 'play':
                        #         continue
                        #     elif play == 'play':
                        #         lives_left = 8



