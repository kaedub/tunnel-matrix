import pygame
import random

pygame.init()

FRAME_WIDTH = 1000
FRAME_HEIGHT = 1000
BOARD_WIDTH = 128
BOARD_HEIGHT = 128
GAP_SIZE = 1
CARD_WIDTH = (FRAME_WIDTH / BOARD_WIDTH) - GAP_SIZE
CARD_HEIGHT = (FRAME_HEIGHT / BOARD_HEIGHT) - GAP_SIZE
LED_RECT = [0, 0, CARD_WIDTH, CARD_HEIGHT]


FRAME = pygame.display.set_mode( [FRAME_WIDTH, FRAME_HEIGHT] )
CLOCK = pygame.time.Clock()
FPS = 8

BLACK = (0,0,0)
RED = (200,0,0)
LRED = (255, 20, 20)
GREEN = (0,140,0)
BLUE = (0,0,200)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
PURPLE = (135,0,135)
VIOLET = (200,130,200)
AQUA = (0,80, 200)
LIME = (50,245,20)
GOLD = (255,215,0)
SALMON = (255,150,120)
CRIMSON = (220,20,60)
SEAGREEN = (32,17,170)
NAVY = (0,0,138)
WHITE = (255,255,255)
GREY = (155,155,155)


COLORS = [SALMON, LRED, RED, CRIMSON, ORANGE, YELLOW, GOLD, LIME, GREEN, SEAGREEN,
          AQUA, BLUE, NAVY, PURPLE, VIOLET, GREY]

while BOARD_WIDTH / 2 > len(COLORS):
   COLORS += COLORS

class Tunnel():
    def __init__(self):
        self.colors = COLORS[0:BOARD_WIDTH/2]
        self.length = len(self.colors)    # = BOARD_WIDTH and BOARD_HEIGHT
        self.rect = LED_RECT
        self.m = 0                          # m, movement
        self.direction = 1
        self.drawcross = False
    def draw_tunnel(self, status):
        if status == True:
            if self.direction == 1:
               self.m += 1
            elif self.direction == -1:
               self.m -= 1
        for i in range(BOARD_HEIGHT):
            #############################################
            # This part is all pygame draw formatting
            #############################################
            self.rect[0] = GAP_SIZE     # move rect to the first column
            self.rect[1] = ((CARD_HEIGHT + GAP_SIZE) * i) + (GAP_SIZE / 2) # move rect to row
            if i < self.length:
                y = i      # y is used to reference to colors list
            else:
                y = self.length - (i - (self.length - 1))   # reflect #
            for j in range(BOARD_WIDTH):
                self.rect[0] = ((CARD_WIDTH + GAP_SIZE) * j) + (GAP_SIZE / 2)
                if j < self.length:
                    x = j   # x is used to reference to colors list
                else:
                    x = 2 * self.length - j - 1   # reflect - simplified equation #
                ###########################################################
                # This is all pattern logic
                ###########################################################
                if (i == j) or (j + i == self.length * 2 - 1):     # pattern logic (y,x + t) % L
                    if self.drawcross:
                        pygame.draw.rect(FRAME, self.colors[((self.length - (i - (self.length - 1))) + self.m)% self.length], self.rect)
                    else:
                        pygame.draw.rect(FRAME, self.colors[(y + (self.m) + 1) % self.length], self.rect)
                elif (i + j > self.length * 2 - 1):
                    if (y - x) > 0:
                        pygame.draw.rect(FRAME, self.colors[(y + 1 + self.m) % self.length], self.rect)
                    elif (y - x) < 0:
                        pygame.draw.rect(FRAME, self.colors[(x + 1 + self.m) % self.length], self.rect)
                elif (i + j < self.length * 2 - 1):
                    if (y - x) > 0:
                        pygame.draw.rect(FRAME, self.colors[(y + 1 + self.m) % self.length], self.rect)
                    elif (y - x) < 0:
                        pygame.draw.rect(FRAME, self.colors[(x + 1 + self.m) % self.length], self.rect)
                    

def main():
    game_loop = True

    pattern = Tunnel()

    moving = False
    
    while game_loop:
       FRAME.fill(WHITE)
       
       pattern.draw_tunnel(moving)
       
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             pygame.quit()
             quit()
          if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 moving = True
             if event.key == pygame.K_v:
                 pattern.direction *= -1
             if event.key == pygame.K_x:
                 if pattern.drawcross == True:
                    pattern.drawcross = False
                 else:
                    pattern.drawcross = True
             if event.key == pygame.K_b:
                 moving = False            
       
       CLOCK.tick(FPS)
       pygame.display.update()

main()
