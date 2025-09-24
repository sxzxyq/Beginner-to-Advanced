# 重构后的最终代码版本

import random
import sys  # 导入 sys 模块以使用 sys.exit()

# --- 常量定义 (Constants) ---
# PEP 8 规范建议常量使用全大写字母。
# 将提示信息分组管理，更清晰。
# 将单词列表设为元组 (tuple)，表示其为不可变数据。
WELCOME_PROMPT = "Guess the word! HINT: The word is a name of a fruit.\n"
START_PROMPT = "\nEnter a letter to guess: "
ERROR_ISALPHA_PROMPT = "Invalid input. Please enter a single letter!"
ERROR_ALREADY_GUESSED = "You've already guessed that letter. Try another one."
ERROR_WRONG_GUESS = "\nWrong, please try again!"
SUCCESS_PROMPT = "\nCongratulations! You've guessed the word!"
FAILURE_PROMPT = "\nGame over! The word was: "
INTERRUPT_PROMPT = "\nGame interrupted. Goodbye!"
CHANCES_LEFT_PROMPT = "You have {} chances left."

WORDS = ("apple", "banana", "lemon", "peach", "orange", "grape", "mango") # 修改：使用元组并修正数据

def get_secret_word(word_list: tuple) -> str:
    """
    从给定的单词列表中随机选择一个单词。
    
    Args:
        word_list: 包含待选单词的元组。

    Returns:
        一个随机选择的单词。
    """
    return random.choice(word_list)

def get_player_guess(guessed_letters: set) -> str | None:
    """
    获取并验证玩家的输入。

    处理无效输入、重复输入和程序中断 (Ctrl+C) 的情况。

    Args:
        guessed_letters: 一个包含玩家已猜过字母的集合。

    Returns:
        一个合法的小写字母字符串，如果用户中断则返回 None。
    """
    while True:
        try:
            guess = input(START_PROMPT).lower()  # 修改：直接转换为小写，解决大小写问题

            if not guess.isalpha() or len(guess) != 1:
                print(ERROR_ISALPHA_PROMPT)
            elif guess in guessed_letters:
                print(ERROR_ALREADY_GUESSED)
            else:
                return guess  # 输入合法，返回
        except KeyboardInterrupt:
            # 修改：健壮性改进，处理 Ctrl+C 中断
            print(INTERRUPT_PROMPT)
            sys.exit() # 干净地退出程序

def display_game_state(secret_word: str, guessed_letters: set):
    """
    根据已猜中的字母，打印当前单词的显示状态。

    Args:
        secret_word: 需要猜测的秘密单词。
        guessed_letters: 包含玩家已猜过字母的集合。
    """
    # Pythonic 改进：使用列表推导式和 str.join()
    # 如果字母在已猜集合中，就显示它，否则显示下划线
    display = [letter if letter in guessed_letters else '_' for letter in secret_word]
    print(f"\nCurrent word: {' '.join(display)}")

def play_game():
    """游戏的主循环逻辑。"""
    secret_word = get_secret_word(WORDS)
    # Pythonic 改进：使用集合 (set) 来存储已猜字母，效率更高且能自动去重
    guessed_letters = set()
    # 使用一个集合来跟踪还剩下哪些字母需要猜，当它为空时，玩家获胜
    letters_to_guess = set(secret_word)
    chances = len(secret_word) + 2  # 游戏规则：比单词长度多两次机会

    # 动态生成初始的下划线提示
    print('_ ' * len(secret_word))

    # Pythonic 改进：使用 while 循环，条件更清晰
    while chances > 0:
        print(CHANCES_LEFT_PROMPT.format(chances))
        
        guess = get_player_guess(guessed_letters)
        
        guessed_letters.add(guess) # 将新猜的字母加入集合

        if guess in letters_to_guess:
            # 如果猜对了
            letters_to_guess.remove(guess)
            print(f"Good guess! The letter '{guess}' is in the word.")
            
            # 检查是否所有独特的字母都已猜完
            if not letters_to_guess:
                print(SUCCESS_PROMPT)
                print(f"The word was: {secret_word}")
                return # 游戏胜利，直接退出函数
        else:
            # 如果猜错了
            chances -= 1
            print(ERROR_WRONG_GUESS)
        
        # 每次猜测后都显示当前进度
        display_game_state(secret_word, guessed_letters)

    # 循环正常结束（chances 耗尽），说明玩家失败
    print(FAILURE_PROMPT + secret_word)


def main():
    """程序入口。"""
    print(WELCOME_PROMPT)
    play_game()

# 确保脚本作为主程序运行时才执行 main()
if __name__ == "__main__":
    main()