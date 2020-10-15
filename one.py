import pyautogui 
import time
import os 


print("""
\n [1.] Spam A Given Wordlist \n [2.] Spam User Wordlist \n [3.] Spam Random User Word \n [4.] Exit
""")

user_input = int(input())

def main() :

    if user_input == 1 : 

        f = open('word.txt', 'r') 
        for word in f :
            pyautogui.typewrite(word)
            pyautogui.press('enter')

    elif user_input == 2 : 

        try:
            
            path = input('Enter Wordlist Path: ')
            user_f = open(path, 'r')
            for word in user_f : 
                pyautogui.typewrite(user_f)
                pyautogui.press('enter')

        except FileNotFoundError :
            print('File Not Found. Enter a Valid Path')

    elif user_input == 3 : 
        user_word = input('Enter sentence/word to spam : ')
        loop = int(input('Enter No of messages to send: '))

        for i in range(loop+1):
            pyautogui.typewrite(user_word)
            pyautogui.press('enter')

    elif user_input == 4 : 
        print('Thanks For Using My Script 😃')

    else : 
        print('Invalid Input')


main()import pyautogui 
import time
import os 


print("""
\n [1.] Spam A Given Wordlist \n [2.] Spam User Wordlist \n [3.] Spam Random User Word \n [4.] Exit
""")

user_input = int(input())

def main() :

    if user_input == 1 : 

        f = open('word.txt', 'r') 
        for word in f :
            pyautogui.typewrite(word)
            pyautogui.press('enter')

    elif user_input == 2 : 

        try:
            
            path = input('Enter Wordlist Path: ')
            user_f = open(path, 'r')
            for word in user_f : 
                pyautogui.typewrite(user_f)
                pyautogui.press('enter')

        except FileNotFoundError :
            print('File Not Found. Enter a Valid Path')

    elif user_input == 3 : 
        user_word = input('Enter sentence/word to spam : ')
        loop = int(input('Enter No of messages to send: '))

        for i in range(loop+1):
            pyautogui.typewrite(user_word)
            pyautogui.press('enter')

    elif user_input == 4 : 
        print('Thanks For Using My Script 😃')

    else : 
        print('Invalid Input')


main()
