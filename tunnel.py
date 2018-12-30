##################################################################
# Tunnel Class - matrix "tunnel" simulation
#
# Much of this code is building a graphic implemenatation
# Create a list of data (colors) then reflect and draw pattern logic.
# Reflect:
# 	Reverse data as it is drawn ---> dataIndex = dataLength - (count - lastIndex)
#	Because dataIndex will reverse once dataLength has been iterated to,
#	pattern logic should only be necessary for one quadrant
# Pattern Logic:
#	if the column number is greater or less than the row number,
#	 	then draw the dataIndexY
#	if not, 
#		then draw dataIndexX
###################################################################

import pygame
import random

pygame.init()

FRAME_WIDTH = 768
FRAME_HEIGHT = 768
BOARD_WIDTH = 32 * 2
BOARD_HEIGHT = 32 * 2
GAP_SIZE = 0
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
        self.length = len(self.colors)
        self.rect = LED_RECT
        self.m = 0                          # m, movement
    def draw_tunnel(self, status):
        if status == True:
            self.m += 1
        for i in range(BOARD_HEIGHT):
            ####################################################################
            # x and y hold data (color) positions, i and j hold matrix position
            # reflect: if halfway through list,
            #          then y = L - (i - (L - 1)
            ####################################################################
            self.rect[0] = GAP_SIZE     # move rect to the first column
            self.rect[1] = ((CARD_HEIGHT + GAP_SIZE) * i) + (GAP_SIZE / 2) # move rect to row
            if i < self.length:
                y = i      # y is used to reference to colors list
            else:
                y = self.length - (i - (self.length - 1))   		# reflect #
            for j in range(BOARD_WIDTH):
                self.rect[0] = ((CARD_WIDTH + GAP_SIZE) * j) + (GAP_SIZE / 2)
                if j < self.length:
                    x = j   # x is used to reference to colors list
                else:
                    x = self.length - (j - (self.length - 1))   	# reflect #
                # pattern logic
                if (y <= j <= ((self.length * 2 - 1) - y)):     # pattern logic (y,x + t) % L
                    pygame.draw.rect(FRAME, self.colors[(y + self.m) % self.length], self.rect)                  
                else:
                    pygame.draw.rect(FRAME, self.colors[(x + self.m) % self.length], self.rect)
                    

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
             if event.key == pygame.K_b:
                 moving = False            
       
       CLOCK.tick(FPS)
       pygame.display.update()

main()
