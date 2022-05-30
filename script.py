import pygame
from pygame.locals import *
import time  
import random

#distância utilizada de parametro, levando em consideração que as dimensões do bloco e da maça são 40pixels por 40 pixels.
size = 40

hardcore = 2


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        
        self.x = size*4
        self.y = size*5
        

    def draw(self):
        
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x=random.randint(0,20)*size

        self.y=random.randint(0,20)*size 


class Snake:
    def __init__(self, surface, length):
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [size]*length
        self.y = [size]*length
        self.direction = 'down'

        self.length = length
        self.x = [40] * length
        self.y = [40] * length


    def move_left(self):
        self.direction = 'left'
        
    def move_right(self):
        self.direction ='right'
        
    def move_down(self):
        self.direction ='down'
        
    def move_up(self):
        self.direction = 'up'

        
    def walk(self):
        
        #função que transforma utilizando arrays o comportamentos dos blocos anteriores da cobra em um sistema aonde o bloco anterior sempre segue o próximo

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # movimentação do bloco 1, a cabeça da cobra.

        if self.direction == 'up':
            self.y[0] -= size
            
        if self.direction == 'down':
            self.y[0] += size
            
        if self.direction == 'left':
            self.x[0] -= size
            
        if self.direction == 'right':
            self.x[0] += size
        
        self.draw()

    
    # função que desenha na tela cada atualização na movimentação da cobra.    
    def draw(self):
        self.parent_screen.fill((16, 82, 1))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()


    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)


    


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 3)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False
        

    def run(self):

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    
                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            self.apple.draw()

            if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move()
                
                
                
                

            time.sleep(.3 / hardcore)
            

if __name__ == '__main__':
    game = Game()
    game.run()

            



    

    

            