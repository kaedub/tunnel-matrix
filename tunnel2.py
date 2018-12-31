
##################################################################
# Tunnel Class - matrix "tunnel" simulation
#
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
###################################################################
# CONTROLS:
#   SPACE - start/stop moving pattern
#   v - change direction
#   c - change pattern
###################################################################

import pygame
import random

pygame.init()

FRAME_WIDTH = 512 * 2
FRAME_HEIGHT = 512 * 2
BOARD_WIDTH = 64 * 2
BOARD_HEIGHT = 64 * 2
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

# Some magic is going on here that needs to be explained
def reflect_index(length, index):
    return 2 * length - index - 1

class Square():
    """Square class to separate concern of drawing pygame shapes"""
    pass

class Tunnel():
    """Draws a tunnel matrix that can be moved each frame.
    Must be run inside of a pygame game loop."""
    def __init__(self):    
        self.colors = COLORS[0: len(COLORS)]
        self.length = BOARD_WIDTH / 2    # = BOARD_WIDTH and BOARD_HEIGHT
        self.rect = LED_RECT                
        self.m = 0                          # m, movement index
        self.direction = 1
        self.drawcross = False
    
    def _set_rect_row(self, pos):
        self.rect[0] = GAP_SIZE
        self.rect[1] = ((CARD_HEIGHT + GAP_SIZE) * pos) + (GAP_SIZE / 2) 
    
    def _set_rect_col(self, pos):
        self.rect[0] = ((CARD_WIDTH + GAP_SIZE) * pos) + (GAP_SIZE / 2)         
        
    def render(self, status):
        """Render the tunnel matrix inside frame """
        if status == True:
            self.m += self.direction

        for row in range(BOARD_HEIGHT):
            self._set_rect_row(row)
            
            # color_y is the color index for the y-axis or top and bottom quadrants.
            # if row has passed halfway then index reverses
            color_y = row if row < self.length else reflect_index(self.length, row)

            for col in range(BOARD_WIDTH):
                self._set_rect_col(col)

                # color_x is the color index for x-axis or left and right quadrants.
                color_x = col if col < self.length else reflect_index(self.length, col)
                    
                # draw cell with y quadrant color index
                if (color_y <= col <= reflect_index(self.length, color_y)):     # pattern logic (y, x + t) % L
                    color_i = (color_y + self.m) % self.length
                # draw cell with x quadrant color index          
                else:
                    color_i = (color_x + self.m) % self.length

                pygame.draw.rect(FRAME, self.colors[color_i], self.rect)  
                
        
    def render_xfold(self, status):
        if status == True:
            if self.direction == 1:
               self.m += 1
            elif self.direction == -1:
               self.m -= 1
        for row in range(BOARD_HEIGHT):
            self.rect[0] = GAP_SIZE     # move rect to the first column
            self.rect[1] = ((CARD_HEIGHT + GAP_SIZE) * row) + (GAP_SIZE / 2) # move rect to row

            # 
            if row < self.length:
                y = row      # y is used to reference to colors list
            else:
                y = self.length - (row - (self.length - 1))   # reflect #
            for col in range(BOARD_WIDTH):
                self.rect[0] = ((CARD_WIDTH + GAP_SIZE) * col) + (GAP_SIZE / 2)
                if col < self.length:
                    x = col   # x is used to reference to colors list
                else:
                    # re
                    x = 2 * self.length - col - 1   # reflect - simplified equation #
                ###########################################################
                # This is all pattern logic
                ###########################################################
                # if part of diagonal cross
                if (row == col) or (col + row == self.length * 2 - 1):     # pattern logic (y,x + t) % L
                    if self.drawcross:
                        # ((L - (y - (L - 1))) + t)% L
                        pygame.draw.rect(FRAME, self.colors[((self.length - (row - (self.length - 1))) + self.m)% self.length], self.rect)
                    else:
                        pygame.draw.rect(FRAME, self.colors[(y + 1 + self.m) % self.length], self.rect)
                # if par
                elif (row + col > self.length * 2 - 1):
                    if (y - x) > 0:
                        pygame.draw.rect(FRAME, self.colors[(y + 1 + self.m) % self.length], self.rect)
                    elif (y - x) < 0:
                        pygame.draw.rect(FRAME, self.colors[(x + 1 + self.m) % self.length], self.rect)
                elif (row + col < self.length * 2 - 1):
                    if (y - x) > 0:
                        pygame.draw.rect(FRAME, self.colors[(y + 1 + self.m) % self.length], self.rect)
                    elif (y - x) < 0:
                        pygame.draw.rect(FRAME, self.colors[(x + 1 + self.m) % self.length], self.rect)
                    

def main():
    game_loop = True

    pattern = Tunnel()
    
    # 1 - tunnel pattern, 2 - xfold tunnel pattern
    patternType = 1

    isMoving = False
    
    while game_loop:
       FRAME.fill(WHITE)
       if patternType == 1:
           pattern.render(isMoving)
       elif patternType == 2:
           pattern.render_xfold(isMoving)
       
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             pygame.quit()
             quit()
          if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 if isMoving == False:
                     isMoving = True
                 elif isMoving == True:
                     isMoving = False
             if event.key == pygame.K_v:
                 pattern.direction *= -1
             if event.key == pygame.K_x:
                 if pattern.drawcross == True:
                    pattern.drawcross = False
                 else:
                    pattern.drawcross = True
             if event.key == pygame.K_c:
                 if patternType == 1:
                     patternType = 2
                 elif patternType == 2:
                     patternType = 1
             
       
       CLOCK.tick(FPS)
       pygame.display.update()

main()
