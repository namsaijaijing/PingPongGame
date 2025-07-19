import pygame

class Ball():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.velocity = 150
        self.dy = 1
        self.dx = 1

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def move(self,dt):
        self.rect.x +=self.dx*dt*self.velocity
        self.rect.y +=self.dy*dt*self.velocity
        self.collide()

    def collide(self):
        if self.rect.y > 455-30:
            self.dy = -1
        if self.rect.x > 802-30:
            self.dx = -1
        if self.rect.y < 0:
            self.dy = 1
        if self.rect.x < 0:
            self.dx = 1