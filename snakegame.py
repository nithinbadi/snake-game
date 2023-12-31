import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400,400
GRID_SIZE = 20
GRID_WIDTH=WIDTH//GRID_SIZE
GRID_HEIGHT=HEIGHT//GRID_SIZE
FPS=10

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
snake_direction = (1,0)
snake_growth = False

food = (random.randint(0,GRID_HEIGHT-1),random.randint(0, GRID_HEIGHT-1))

game_over=False
score=0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction !=(0,1):
                snake_direction=(0,-1)
            elif event.key == pygame.K_DOWN and snake_direction!=(0,-1):
                snake_direction = (0,1)
            elif event.key == pygame.K_LEFT and snake_direction!=(1,0):
                snake_direction =(-1,0)
            elif event.key == pygame.K_RIGHT and snake_direction!=(-1,0):
                snake_direction = (1,0)
    
    new_head = (snake[0][0] + snake_direction[0],snake[0][1]+snake_direction[1])
    snake.insert(0,new_head)


    if snake[0]==food:
        snake_growth=True
        score+=1
        food = (random.randint(0,GRID_WIDTH-1), random.randint(0,GRID_HEIGHT-1))
    else:
        snake_growth=False
    if(
        snake[0][0]<0
        or snake[0][0]>=GRID_WIDTH
        or snake[0][1]<0
        or snake[0][1]>=GRID_HEIGHT
        or snake[0] in snake[1:]
    ):
        game_over=True
    
    if not snake_growth:
        snake.pop()
    
    screen.fill(BLACK)

    pygame.draw.rect(screen,GREEN,(food[0]*GRID_SIZE,food[1]*GRID_SIZE,GRID_SIZE,GRID_SIZE))

    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0]*GRID_SIZE,segment[1]*GRID_SIZE,GRID_SIZE,GRID_SIZE))
    
    pygame.display.flip()
    clock.tick(FPS)

print(score)
pygame.quit()
sys.exit()
