import pygame
import math
import sys


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Algorithm Visualizer")


def draw_line_with_slope(screen, color, point1, point2):
    # Calculate the angle of the line
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    angle = math.atan2(dy, dx)
    
    # Calculate the length of the line
    length = math.sqrt(dx**2 + dy**2)

    # Draw the line
    pygame.draw.line(screen, color, point1, point2, 2)


running = True
player = pygame.Rect((300,250,50,50))
while running:
  pygame.draw.circle(screen, (255,0,0), (100, 100), 3)
  pygame.draw.circle(screen, (255,0,0), (200, 100), 3)
  pygame.draw.circle(screen, (255,0,0), (300, 100), 3)
  pygame.draw.circle(screen, (255,0,0), (400, 100), 3)
  pygame.draw.circle(screen, (255,0,0), (500, 100), 3)
  draw_line_with_slope(screen,(255,0,0), (500,500), (100,100))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()