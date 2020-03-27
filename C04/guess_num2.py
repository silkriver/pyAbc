from random import randint
target = randint(1, 100)
print("我想了一个1到100之间的整数，请你猜猜看吧：")
guess = 0
answer = ""
while guess != target:  # 只要还没猜对就执行循环
    guess = int(input())
    if guess == target:
        answer = "你猜对了！游戏结束。"
    elif guess > target:
        answer = "你猜大了，再猜一次："
    else:
        answer = "你猜小了，再猜一次："
    print(answer)
