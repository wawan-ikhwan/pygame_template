import pygame
import pygame.draw # https://www.pygame.org/docs/ref/draw.html
import pygame.display # https://www.pygame.org/docs/ref/display.html
import pygame.event # https://www.pygame.org/docs/ref/event.html
import pygame.mouse # https://www.pygame.org/docs/ref/mouse.html
import pygame.key # https://www.pygame.org/docs/ref/key.html
import pygame.time # https://www.pygame.org/docs/ref/time.html
import pygame.font # https://www.pygame.org/docs/ref/font.html

pygame.init()

# CONSTANT
WIDTH, HEIGHT = (480,320)

# START OF GAME SETUP
pygame.display.set_caption('PYGAME BEST TEMPLATE')
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # surface
FONT_COMIC = pygame.font.SysFont('Comic Sans MS', 20)
# END OF GAME SETUP

# START OF INITIALIZING
t = pygame.time.get_ticks()
xCircle = 0
yCircle = 0
# END OF INITIALIZING

isGameRunning = True
while isGameRunning:

  # REFRESH
  SCREEN.fill((255, 255, 255))
  current_ticks = pygame.time.get_ticks()

  # START OF EVENT
  for EVENT in pygame.event.get():
    if EVENT.type == pygame.QUIT:
      isGameRunning = False
  # END OF EVENT

  # START OF USER INPUT
  mouse_pos = pygame.mouse.get_pos()
  mouse_pressed = pygame.mouse.get_pressed()
  key_pressed = pygame.key.get_pressed()
  # END OF USER INPUT
  
  # START OF UPDATING
  if current_ticks - t > 100:
    t = current_ticks
    if xCircle < WIDTH:
      xCircle += 1
  # END OF UPDATING
  
  # START OF DRAWING
  pygame.draw.circle(SCREEN,(0,255,0), (xCircle, HEIGHT//2),10)
  SCREEN.blit(FONT_COMIC.render(str(mouse_pos), False, (0, 0, 255)),(10,10))
  SCREEN.blit(FONT_COMIC.render(str(key_pressed), False, (0, 0, 255)),(10,30))
  SCREEN.blit(FONT_COMIC.render(str(mouse_pressed), False, (0, 0, 255)),(10,50))
  # END OF DRAWING

  # UPDATE SCREEN
  pygame.display.update()

pygame.quit()