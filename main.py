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
        self.scoreboard1 = pygame.image.load("asset/ScoreBar.png")
        self.scoreboard1 = pygame.transform.flip(self.scoreboard1,True,False)
        self.scoreboard2 = pygame.image.load("asset/ScoreBar.png")

        player1_img = pygame.image.load("asset/Player1.png")
        player2_img = pygame.image.load("asset/Player2.png")
        ball_img = pygame.image.load("asset/Ball.png")
        self.player1 = Player(780,455/2.7,player1_img)
        self.player2 = Player(4,455/2.7,player2_img)
        self.ball =  Ball((802/2)-15,(455/2)-15,ball_img)

        self.font = pygame.font.SysFont("Arial",24)

        self.start_time = pygame.time.get_ticks()
        self.timer = 120

        self.finish = False

    def collide(self):
        if self.ball.rect.colliderect(self.player1.rect):
            self.ball.dx = -(self.ball.dx)
        if self.ball.rect.colliderect(self.player2.rect):
            self.ball.dx = -(self.ball.dx)

    def display_score(self):
        text1 = self.font.render("Player1 score:"+str(self.player1.score),True,(255,255,255)) 
        text2 = self.font.render("Player2 score:"+str(self.player2.score),True,(255,255,255))       
        self.screen.blit(text1,(802-250,5))
        self.screen.blit(text2,(75,5))

    def display_time(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) / 1000
        text_time = self.font.render("Time",True,(255,255,255))
        self.screen.blit(text_time,((802/2)-24,0))
        if not self.finish:
            text_timer = self.font.render(str(int(self.timer - elapsed_time)),True,(255,255,255))
        else:
            text_timer = self.font.render("0",True,(255,255,255))

        self.screen.blit(text_timer,((802/2)-20,30))

    def time_check(self):
        text_win1 = self.font.render("Player 1 Win!",True,(255,255,255))
        text_win2 = self.font.render("Player 2 Win!",True,(255,255,255))
        text_draw = self.font.render("DRAW!",True,(255,255,255))
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) / 1000
        if (elapsed_time > self.timer):
            self.finish = True
            if self.player1.score > self.player2.score:
                self.screen.blit(text_win1,((802/2)-50,(455/2)-24))
                self.ball.rect.x = (802/2)-15
                self.ball.rect.y = (455/2)-15
            if self.player2.score > self.player1.score:
                self.screen.blit(text_win2,((802/2)-50,(455/2)-24))
                self.ball.rect.x = (802/2)-15
                self.ball.rect.y = (455/2)-15
            if self.player2.score == self.player1.score:
                self.screen.blit(text_draw,((802/2)-50,(455/2)-24))
                self.ball.rect.x = (802/2)-15
                self.ball.rect.y = (455/2)-15


    def run(self):
        running = True
        while running:
            
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.BG,(0,0))

            self.screen.blit(self.scoreboard1,(802-341,0))
            self.screen.blit(self.scoreboard2,(0,0))

            self.player1.draw(self.screen)
            self.player1.move1(dt)
            
            self.player2.draw(self.screen)
            self.player2.move2(dt)

            self.ball.draw(self.screen)
            self.ball.move(dt,self.player1,self.player2)

            self.collide()
            self.display_score()
            self.display_time()
            self.time_check()

            pygame.display.update()
        pygame.quit()


ping_pong = Game()
ping_pong.run()