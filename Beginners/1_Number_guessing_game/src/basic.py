import random
from typing import List,Optional,Dict

def generate_random(low_number:int,high_number:int) -> int:
    number = random.randint(low_number,high_number)
    return number

def bisection_method(low:int , high:int ,number:int):
    left = low
    right = high
    chance = 0
    mid = (left + right)/2
    
    while left <= right:
        if mid <= number:
            left = mid + 1
        else: 
            right = mid -1
        mid = (left + right)/2
        chance += 1
    print(chance)
    return chance + 1

def check(number:int,guess:int) -> bool:
    if guess > number:
        print("再试一次！你猜得太高了")
        return False
    elif guess < number:
        print("再试一次！你猜得太小了")
        return False
    else :
        print("Congratulations！")
        return True
        
def main():
    low = int(input("请输入较小数："))
    high = int(input("请输入较大数："))
    number = generate_random(low,high)
    chance = bisection_method(low,high,number)
    count = 0
    while count <= chance:
        guess = int(input("猜猜看："))
        judge = check(number,guess)
        if judge:
            break
        count += 1
    if not judge:
        print("下次好运！")

main()