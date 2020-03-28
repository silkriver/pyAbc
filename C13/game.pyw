"""贪吃蛇小游戏"""
import pygame as pg
from random import randrange
red, black, bgcolor = (255, 0, 0), (0, 0, 0), (200, 200, 200)
screen_width, screen_height = 500, 500


class Snake:
    def __init__(self):     # 初始化类实例
        pg.init()           # 初始化pygame
        self.score = 0      # 游戏得分
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode((screen_width, screen_height))
        body, head = [[250, 250], [240, 250], [230, 250]], [250, 250]
        food = [randrange(1, 50) * 10, randrange(1, 50) * 10]
        self.display.fill(bgcolor)
        self.play_game(head, body, food, 1)
        while True:
            self.screen_final_score()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

    def met_food(self, food):       # 碰到食物
        food = [randrange(1, 50) * 10, randrange(1, 50) * 10]
        self.score += 1
        return food

    def met_border(self, head):     # 碰到窗口边界
        return any([head[0] >= 500, head[0] < 0, head[1] >= 500, head[1] < 0])

    def met_self(self, body):       # 碰到自己
        head = body[0]
        return True if head in body[1:] else False

    def no_way(self, body):         # 是否无路可走
        head = body[0]
        return True if self.met_border(head) or self.met_self(body) else False

    def move(self, head, body, food, heading):  # 移动
        if heading == 1:
            head[0] += 10
        elif heading == 0:
            head[0] -= 10
        elif heading == 2:
            head[1] += 10
        elif heading == 3:
            head[1] -= 10
        if head == food:
            food = self.met_food(food)
            body.insert(0, list(head))
        else:
            body.insert(0, list(head))
            body.pop()
        return body, food

    def draw_snake(self, body):     # 绘制蛇
        for pos in body:
            pg.draw.rect(self.display, black, pg.Rect(pos[0], pos[1], 10, 10))

    def draw_food(self, food):      # 绘制食物
        pg.draw.rect(self.display, red, pg.Rect(food[0], food[1], 10, 10))

    def play_game(self, head, body, food, heading):     # 开始游戏
        crashed = False
        prev_heading, heading = 1, 1
        while crashed is not True:
            for event in pg.event.get():
                crashed = True if event.type == pg.QUIT else False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT and prev_heading != 1:
                        heading = 0
                    elif event.key == pg.K_RIGHT and prev_heading != 0:
                        heading = 1
                    elif event.key == pg.K_UP and prev_heading != 2:
                        heading = 3
                    elif event.key == pg.K_DOWN and prev_heading != 3:
                        heading = 2
            self.display.fill(bgcolor)
            self.draw_food(food)
            self.draw_snake(body)
            body, food = self.move(head, body, food, heading)
            pg.display.set_caption("贪吃蛇小游戏  当前得分: %s" % self.score)
            pg.display.update()
            prev_heading = heading
            crashed = True if self.no_way(body) else False
            self.clock.tick(3)

    def screen_final_score(self):   # 在屏幕上显示最终得分
        font = pg.font.Font('freesansbold.ttf', 35)
        text = font.render("Final Score: %s" % self.score, True, red, bgcolor)
        textRect = text.get_rect()
        textRect.center = ((screen_width / 2), (screen_height / 2))
        self.display.blit(text, textRect)
        pg.display.update()


if __name__ == "__main__":
    Snake()
