import random

WELCOME_PROMPT = "Guess the word! HINT: word is a name of a fruit\n"
SIGNAL_PROMPT = "_ _ _ _ _\n"
START_PROMPT = "Enter a letter to guess:"
ERROR_ISALPHA_PROMPT = "Please enter a letter!"
ERROR_LEN_PROMPT = "Please enter only one letter!"
ERROR_KEY_PROMPT = "Interruput!"
ERROR_GUESSES = "\nWrong,please try again!\n"

#words = ["apple","banana","lemon","peach","bearbug"]
words = ["lemon"]

def generate_word():
    word = random.choice(words)
    return word

def user_input():
    while True:
        try:
            guesses_word = input(START_PROMPT)
            if guesses_word.isalpha() and len(guesses_word) == 1:
                return guesses_word
            elif not guesses_word.isalpha():
                return print(ERROR_ISALPHA_PROMPT)
            else:
                return print(ERROR_LEN_PROMPT) 
        except KeyboardInterrupt:
            return print(ERROR_KEY_PROMPT)

def word_print(extra_word:list,tool_word:str) -> None:
    print(extra_word,tool_word)
    for num_3 in range(len(extra_word)):
        print(num_3)
        if extra_word[num_3] == 1:
            print(tool_word[num_3])
        else:
            print("_")
            
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
                # if user_word == tool_word[num_2] and extra_word[num_2] != 1:
                #     print(user_word)
                #     extra_word[num_2] = 1 
                # elif extra_word[num_2] == 1:
                #     print(tool_word[num_2])
                # else: 
                #     print("_")
        else:
            print(ERROR_GUESSES)
            
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