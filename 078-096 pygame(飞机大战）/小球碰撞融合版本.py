import pygame
import sys
from pygame.locals import *
from random import *
import math

# spritecollide(sprite,group,dokill,collided=None)
# 第三个参数是碰撞毁灭；第四个参数设置特殊检测方法，忽略的话默认检测rect
# 第四个参数pygame.sprite.collide_circle就是支持圆碰撞检测,但需要半径参数

class Ball(pygame.sprite.Sprite):
    # pygame.sprite.Sprite是pygame里精灵的基类，继承就行

    def __init__(self,image,position,speed,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(image).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top=position
        self.speed=speed
        self.width,self.height=bg_size[0],bg_size[1]
        self.radius=self.rect.width/2
        # 传入半径参数(圆碰撞检测所需)

    def move(self):
        self.rect=self.rect.move(self.speed)
        #这里用rect的move方法就可以了

        # 设置小球碰左墙后从相连右边出来(穿越效果)
        if self.rect.right<=0:
            self.rect.left=self.width
        elif self.rect.left>=self.width:
            self.rect.right=0
        elif self.rect.bottom<=0:
            self.top=self.height
        elif self.rect.top>=self.height:
            self.rect.bottom=0

def main():
    pygame.init()
    # pygame.mixer.init()

    ball_image = 'gray_ball.png'
    bg_image = 'background.png'

    running = True

    # 增加魔性BGM
    pygame.mixer.music.load('Music/bg_music.ogg')
    pygame.mixer.music.play()

    # 添加音效
    loser_sound=pygame.mixer.Sound(r'Music/loser.wav')
    laugh_sound=pygame.mixer.Sound(r'Music/laugh.wav')
    winner_sound=pygame.mixer.Sound('Music/winner.wav')
    hole_sound=pygame.mixer.Sound(r'Music/hole.wav')

    # 音乐结束时游戏结束
    GAMEOVER=USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)

    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("玩球")
    background = pygame.image.load(bg_image).convert_alpha()
    # 创建五个随机小球放入balls列表
    balls=[]
    group=pygame.sprite.Group()

    BALL_NUM=5
    for i in range(BALL_NUM):
        position=randint(0,width-100),randint(0,height-100)
        # 球的直径为100
        speed=[randint(-10,10),randint(-10,10)]
        ball=Ball(ball_image,position,speed,bg_size)
        # Ball类实例化
        while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):
            ball.rect.left,ball.rect.top=randint(0,width-100),randint(0,height-100)
        balls.append(ball)
        group.add(ball)

    clock=pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==GAMEOVER:
                loser_sound.play()
                pygame.time.delay(2000)
                # 等2000ms（2s）
                laugh_sound.play()
                pygame.time.delay(3000)
                running=False

        screen.blit(background,(0,0))

        # 小球们移动并刷新画面
        for each_ball in balls:
            each_ball.move()
            screen.blit(each_ball.image, each_ball.rect)
            # class Ball里传入的rect就是矩形位置

        # 判断碰撞
        for each in group:
            group.remove(each)
            if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.speed[0]=-each.speed[0]
                each.speed[1]=-each.speed[1]
            group.add(each)


        pygame.display.flip()
        clock.tick(30)



if __name__=='__main__':
    main()