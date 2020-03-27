from random import randint
target = randint(1, 100)  # 生成1到100之间的一个随机整数
answer = ""
guess = int(input("我想了一个1到100之间的整数，请你猜猜看吧："))
if guess == target:
    answer = "你猜对了！"
elif guess > target:
    answer = "你猜大了。"
else:
    answer = "你猜小了。"
print(answer)
