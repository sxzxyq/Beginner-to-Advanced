# code
# Python
import random
import math
# <--- 修改点: 移除了未使用的 List, Optional, Dict，并加入了需要的 math 模块

# --- 常量定义 ---
# <--- 新增点: 将固定的字符串定义为常量，便于维护和修改，也让代码更清晰。
PROMPT_LOW = "请输入范围的下限整数: "
PROMPT_HIGH = "请输入范围的上限整数: "
PROMPT_GUESS = "现在，猜一个数: "
MSG_TOO_HIGH = "再试一次！你猜得太高了。"
MSG_TOO_LOW = "再试一次！你猜得太小了。"
MSG_CONGRATS = "恭喜你，猜对了！"
MSG_FAIL = "很遗憾，次数用完了。正确的数字是 {}。"
MSG_INVALID_INPUT = "无效的输入，请输入一个有效的整数。"
MSG_RANGE_ERROR = "范围设置错误，下限必须小于上限。"

def get_integer_input(prompt: str) -> int:
    """
    <--- 新增函数: 封装了获取用户输入并处理错误的功能，提高了代码的健壮性。
    从用户那里获取一个有效的整数输入。

    Args:
        prompt: 显示给用户的提示信息。

    Returns:
        用户输入的整数。
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(MSG_INVALID_INPUT)

def test1(prompt:str) -> int:
    while True:
        try:
            return int(input("prompt"))
        except ValueError:
            print("False number!")
    
def calculate_max_guesses(low: int, high: int) -> int:
    """
    <--- 修改点: 函数重命名并优化了实现逻辑。
    使用对数计算在给定范围内通过二分查找找到目标所需的最大猜测次数。

    Args:
        low: 范围的下限。
        high: 范围的上限。

    Returns:
        最大猜测次数。
    """
    # <--- 修改点: 采用数学公式直接计算，比循环模拟更高效、更简洁。
    range_size = high - low + 1
    return math.ceil(math.log2(range_size))

def test2(low:int,high:int) -> int:
    return math.ceil(math.log2(high-low+1))

def check_guess(target_number: int, guess: int) -> bool:
    """
    <--- 修改点: 函数和参数名更清晰 (number -> target_number)。
    检查玩家的猜测是否正确，并打印相应的提示。

    Args:
        target_number: 游戏设定的目标数字。
        guess: 玩家猜测的数字。

    Returns:
        如果猜对则返回 True，否则返回 False。
    """
    if guess > target_number:
        print(MSG_TOO_HIGH)
        return False
    elif guess < target_number:
        print(MSG_TOO_LOW)
        return False
    else:
        print(MSG_CONGRATS)
        return True

def game_loop():
    """
    <--- 修改点: 将主逻辑封装在 game_loop 函数中，而不是直接放在 main 中。
    这是良好的编程实践，使得代码可以被其他脚本导入和调用。
    """
    print("--- 欢迎来到猜数游戏 ---")

    # 获取并验证游戏范围
    while True:
        low = get_integer_input(PROMPT_LOW)
        high = get_integer_input(PROMPT_HIGH)
        if low < high:
            break
        print(MSG_RANGE_ERROR) # <--- 新增点: 处理下限大于等于上限的逻辑错误

    secret_number = random.randint(low, high)
    max_attempts = calculate_max_guesses(low, high)

    print(f"我已经想好了一个 {low} 到 {high} 之间的数，你有 {max_attempts} 次机会。")

    # <--- 修改点: 使用 for 循环代替 while 循环，更 Pythonic。
    for attempt in range(max_attempts):
        print(f"--- 第 {attempt + 1} 次尝试 ---")
        player_guess = get_integer_input(PROMPT_GUESS)
        
        if check_guess(secret_number, player_guess):
            break  # 猜对了，中断循环
    else:
        # <--- 修改点: 使用 for...else 结构处理游戏失败的情况。
        # 只有当 for 循环正常结束（未被 break）时，才会执行 else 块。
        print(MSG_FAIL.format(secret_number))

def main():
    """
    程序主入口。
    """
    game_loop()

# <--- 推荐实践: 使用 __name__ == "__main__" 作为程序入口。
# 这可以防止在其他脚本导入此文件时自动运行游戏。
# if __name__ == "__main__":
#     main()
    
if __name__ == "__main__":
    main()