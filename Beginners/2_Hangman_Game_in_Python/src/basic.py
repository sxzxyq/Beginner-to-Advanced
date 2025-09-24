import random
import sys

WELCOME_PROMPT = "Guess the word! HINT: word is a name of a fruit\n"
SIGNAL_PROMPT = "_ _ _ _ _\n"
START_PROMPT = "\nEnter a letter to guess:"
ERROR_ISALPHA_PROMPT = "Please enter a letter!"
ERROR_LEN_PROMPT = "Please enter only one letter!"
ERROR_KEY_PROMPT = "\nInterruput!"
ERROR_GUESSES = "\nWrong,please try again!\n"
SUCCESS_PROMPT = "\nCongratulations!"
CHANCE_OUT = "This is no more chance!"

words = ["apple","banana","lemon","peach","bearbug"]
#words = ["lemon"]

def generate_word():
    word = random.choice(words)
    return word

def user_input():
    while True:
        try:
            guesses_word = input(START_PROMPT).lower()
            if guesses_word.isalpha() and len(guesses_word) == 1:
                return guesses_word
            elif not guesses_word.isalpha():
                print(ERROR_ISALPHA_PROMPT)
                continue
            else:
                print(ERROR_LEN_PROMPT)
                continue 
        except KeyboardInterrupt:
            print(ERROR_KEY_PROMPT)
            sys.exit()

def word_print(extra_word:list,tool_word:str) -> None:
    #print(extra_word,tool_word)
    for num_3 in range(len(extra_word)):
        #print(num_3)
        if extra_word[num_3] == 1:
            print(tool_word[num_3], end="")
        else:
            print("_", end="")
            
def judge_print(tool_word:str,chances:int) -> None:
    extra_word = [0] * len(tool_word)
    for chance in range(chances):
        user_word = user_input()
        if user_word in tool_word:
            for num_2 in range(len(tool_word)):
                if user_word == tool_word[num_2] and extra_word[num_2] != 1:
                    extra_word[num_2] = 1
                    break
            word_print(extra_word,tool_word)
            if not 0 in extra_word:
                print(SUCCESS_PROMPT)
                break
                # if user_word == tool_word[num_2] and extra_word[num_2] != 1:
                #     print(user_word)
                #     extra_word[num_2] = 1 
                # elif extra_word[num_2] == 1:
                #     print(tool_word[num_2])
                # else: 
                #     print("_")
        else:
            print(ERROR_GUESSES)
    else:
        print(CHANCE_OUT)
            
def calculate_chance(word:str) -> int:
    chances = len(word) + 2
    return chances
      
def main_loop():
    tool_word = generate_word()
    chances = calculate_chance(tool_word)
    judge_print(tool_word,chances)
    

def main():
    print(WELCOME_PROMPT)
    print(SIGNAL_PROMPT)
    main_loop()    
    
if __name__ == "__main__":
    main()