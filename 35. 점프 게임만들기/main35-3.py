import pygame
import sys
from PyQt5 import QtWidgets


FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()
clock = pygame.time.Clock()
# FPS(Frame Per Second)
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
# 화면 크기 설정

# background = pygame.image.load("./background.png")

pygame.display.set_caption("Jump Game")
# 화면 타이틀 설정



class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10

    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.5 * neg # y값 높이 조절
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

class Enemy():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self):
        return pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 40))
    
    def move(self,speed):
        self.x = self.x - speed
        if self.x <= 0:
            self.x = MAX_WIDTH

player = Player(50, MAX_HEIGHT - 40)
enemy = Enemy(MAX_WIDTH, MAX_HEIGHT - 40)


def main():

    speed = 7
    game_font = pygame.font.Font(None, 40)

    total_time = 10

    start_ticks = pygame.time.get_ticks()

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    
    screen.blit(timer, (10,10))
    
    while True:
        # if total_time - elapsed_time <= 0:
        #     print("타임아웃")
        #     running = False
        #     screen.fill((255, 255, 255))
        #     screen.blit(timer, (10,10))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.isJump = True

            clock.tick(FPS) 
            screen.fill((255, 255, 255))
            print("fps : " + str(clock.get_fps()))
            # font1 = pygame.font.SysFont(None,30)
            # img1 = font1.render('HELLO WOLRD! 안녕하세요!',True)
            # screen.blit(img1, (50,50))
            
            player_rect = player.draw()
            player.jump()
            
            enemy_rect = enemy.draw()
            enemy.move(speed)
            speed = speed + 0.01
            
            if player_rect.colliderect(enemy_rect):
                print("충돌")
                pygame.quit()
                sys.exit()
                
            pygame.display.update()

if __name__ == '__main__':
    main()
