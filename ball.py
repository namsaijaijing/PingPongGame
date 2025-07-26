import pygame
from player import*

class Ball():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.velocity = 200
        self.dy = 1
        self.dx = 1

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def move(self,dt,player1,player2):
        self.rect.x +=self.dx*dt*self.velocity
        self.rect.y +=self.dy*dt*self.velocity
        self.collide(player1,player2)

    def collide(self,player1,player2):
        if self.rect.y > 455-30:
            self.dy = -1
        if self.rect.x > 802-30:
           self.dx = -1
           player2.score += 1
           self.rect.x = (802/2)-15
           self.rect.y = (455/2)-15
        if self.rect.y <47:
            self.dy = 1
        if self.rect.x < 0:
           self.dx = 1
           player1.score += 1
           self.rect.x = (802/2)-15
           self.rect.y = (455/2)-15