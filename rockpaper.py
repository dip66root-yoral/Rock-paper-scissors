import random
import pyttsx3

while True:
    voice = pyttsx3.init()
    emoji ={'r': '💎' ,'p': '📄', 's': '✂️'}
    choices = ('r', 'p', 's')

    user_choice= input("Rock , paper, or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please choose 'r', 'p', or 's'.")

    computer_choice = random.choice(choices)

    print(f'you chose {emoji[user_choice]}')
    print(f'computer chose {emoji[computer_choice]}')
    if user_choice== computer_choice:
        result_text = "It's a Tie"
    elif  (
     (user_choice == 'r' and computer_choice == 's') or
     (user_choice == 'p' and computer_choice == 'r') or
     (user_choice == 's' and computer_choice == 'p')):
        result_text = "You Won"
    else:
        result_text = "You Lost"

    print(result_text)
    voice.say(result_text)
    voice.runAndWait()

    voice.stop()
    del voice
        
    should_continue =input("Continue? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing!")
        break





# import random
# import pyttsx3

# emoji ={'r': '💎' ,'p': '📄', 's': '✂️'}
# choices = ('r', 'p', 's')
# text_to_speech = pyttsx3.init()
# user_choice = input("Rock , paper, or scissors? (r/p/s): ").lower()
# if user_choice not in choices:
#     print("Invalid choice! Please choose 'r', 'p', or 's'.")
# while True:

#     computer_choice = random.choice(choices)
#     print(f'Computer chose {emoji[computer_choice]}')
#     print(f'User chose {emoji[user_choice]}')
#     if user_choice== computer_choice:
#         print("Tie!")
#         text_to_speech.say("IT'S A TIE")
#         text_to_speech.runAndWait()
#     elif  (
#      (user_choice == 'r' and computer_choice == 's') or
#      (user_choice == 'p' and computer_choice == 'r') or
#      (user_choice == 's' and computer_choice == 'p')):
        
#         text_to_speech.say("you won")
#         text_to_speech.runAndWait()
#         print("you won")
#     else:
#         text_to_speech.say("you lost")
#         text_to_speech.runAndWait()
#         print("You lost")
#     should_continue =input("Continue? (y/n): ").lower()
#     if should_continue == 'n':
#         print("Thanks for playing!")
#         break


# text_to_speech.stop()
