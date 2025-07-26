import pygame

class Player():
    def __init__(self ,x ,y ,image):
        self.image = image
        self.rect = image.get_rect(x=x ,y=y)
        self.velocity = 200
        self.score = 0

    def draw(self,screen):
        screen.blit(self.image ,(self.rect.x,self.rect.y))

    def move1(self,dt):
        pressed = pygame.key.get_pressed()
        dy = 0
        if pressed[pygame.K_UP]:
            dy = -1
        if pressed[pygame.K_DOWN]:
            dy = 1

        self.rect.y += dy * self.velocity * dt

        self.check()

    def move2(self,dt):
        pressed = pygame.key.get_pressed()
        dy = 0
        if pressed[pygame.K_w]:
            dy = -1
        if pressed[pygame.K_s]:
            dy = 1

        self.rect.y += dy * self.velocity * dt

        self.check()

    def check(self):
        if self.rect.y < 47:
            self.rect.y = 47
        if self.rect.y > 455-120:
            self.rect.y = 455-120
        