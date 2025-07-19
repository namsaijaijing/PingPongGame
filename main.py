import pygame
from player import *
from ball import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((802,455))
        pygame.display.set_caption("PingPong Game")
        self.clock = pygame.time.Clock()
        self.BG = pygame.image.load("asset/Board.png")
        player1_img = pygame.image.load("asset/Player1.png")
        player2_img = pygame.image.load("asset/Player2.png")
        ball_img = pygame.image.load("asset/Ball.png")
        self.player1 = Player(780,455/2.7,player1_img)
        self.player2 = Player(4,455/2.7,player2_img)
        self.ball =  Ball((802/2)-15,(455/2)-15,ball_img)

    def run(self):
        running = True
        while running:
            
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.BG,(0,0))

            self.player1.draw(self.screen)
            self.player1.move1(dt)
            
            self.player2.draw(self.screen)
            self.player2.move2(dt)

            self.ball.draw(self.screen)
            self.ball.move(dt)

            pygame.display.update()
        pygame.quit()


ping_pong = Game()
ping_pong.run()