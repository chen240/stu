
import pygame
from snak_class import *
import random  
# 食物类  
# 方法： 放置/移除  
# 点以25为单位  
class Food:  
    def __init__(self):  
        self.rect = pygame.Rect(-25,0,25,25)  
  
    def remove(self):  
        self.rect.x=-25  
  
    def set(self):  
        if self.rect.x == -25:  
            allpos = []  
            # 不靠墙太近 25 ~ SCREEN_X-25 之间  
            for pos in range(25,SCREEN_X-25,25):  
                allpos.append(pos)  
            self.rect.left = random.choice(allpos)  
            self.rect.top  = random.choice(allpos)  
            print(self.rect)  