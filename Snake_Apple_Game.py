import pygame
from pygame.locals import *
import time
import random

# this is a project of Apple eating snake this is my first project with OOP SO SORRY FOR ANY MISTAKES

SIZE = 40
DEFAULT_IMAGE_SIZE = (72, 72)
APPLE_SIZE = (71, 72) 
BACKGROUND_COLOUR=(26, 186, 71)
# this is the class for the snake

class Apple:
  def __init__(self, parent_screen,):
    self.snake_food = pygame.image.load("Resources/snake_food.png").convert_alpha()
    self.snake_food = pygame.transform.scale(self.snake_food, APPLE_SIZE)

    self.parent_screen = parent_screen
    self.x = SIZE*3
    self.y = SIZE*3
    
    
  def draw(self):
        # now I will draw the snake food on the screen
    self.parent_screen.blit(self.snake_food, (self.x, self.y))
    pygame.display.flip()
    
            
  def move(self):
        self.x = random.randint(0,25)*SIZE
        self.y = random.randint(0,20)*SIZE






class Snake:

    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        # now I will load the image of a snake head
        self.snake_head = pygame.image.load("Resources/snake_head.png").convert_alpha()
        self.snake_head = pygame.transform.scale(self.snake_head, DEFAULT_IMAGE_SIZE)
        # now I will load the image of a snake body
        self.snake_body = pygame.image.load("Resources/snake_body.png").convert_alpha()
        self.snake_body = pygame.transform.scale(self.snake_body, DEFAULT_IMAGE_SIZE)
        # now I will load the background
        self.background = pygame.image.load("Resources/BG-1.png").convert()
        # now I will load the food of the snake
        # now I set the location of the snake head
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "DOWN"

    def increase_length(self):
      self.length += 1                                                                                                                                                                                                                                                                                                          
      self.x.append(-1)
      self.y.append(-1)
      
    
      
      
      
      
      
      
      
      
      
      # now I will make another function called draw that will draw the snake on the screen
    def draw(self):
       
        # now I will draw the snake head on the screen
        for i in range(self.length - 1, 0, -1):
            self.parent_screen.blit(self.snake_body, (self.x[i], self.y[i]))
        for h in range(self.length):
            self.parent_screen.blit(self.snake_head, (self.x[i], self.y[ i]))
            
            
        pygame.display.flip()

    def up(self):
        self.direction = "UP"

    def down(self):
        self.direction = "DOWN"

    def left(self):
        self.direction = "LEFT"

    def right(self):
        self.direction = "RIGHT"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == "UP":
            self.y[0] -= SIZE
        if self.direction == "DOWN":
            self.y[0] += SIZE
        if self.direction == "LEFT":
            self.x[0] -= SIZE
        if self.direction == "RIGHT":
            self.x[0] += SIZE
        self.draw()


# let's make a class of a game

class Game:
    def __init__(self):
        # let's initiate pygame
        pygame.init()
        # let's set the screen size
        self.snake_game = pygame.display.set_mode((1200, 1000))
       
        pygame.mixer.init()
       
        # let's give a background colour
        self.snake_game.fill((26, 186, 71))
        # now I will create a snake in my snake class
        self.snake = Snake(self.snake_game,2)
        self.snake.draw()
        self.apple = Apple(self.snake_game,)
        
    
    
        
    def display_score(self):
      font = pygame.font.SysFont('bold', 40)
      score = font.render(f"Score : {self.snake.length - 1}", True , (255,255,255) )   
      self.snake_game.blit(score,(858,10))
      pygame.display.flip()
      
    
    def render_background(self):
        bg = pygame.image.load("Resources\BG_2.jpg")
        self.snake_game.blit(bg,(0,0))
        
        
        
        
    def play(self):
      self.render_background()
      self.snake.walk()
      self.apple.draw()
      
      self.display_score()
      
      pygame.display.flip()
      
  
      if self.is_collision(self.snake.x[0],self.snake.y[0], self.apple.x,self.apple.y):
       
        sound = pygame.mixer.Sound("Resources\munch.mp3")
        pygame.mixer.Sound.play(sound)
        self.snake.increase_length()
        self.apple.move()
    
    
      for i in range(3,self.snake.length):
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
            sound = pygame.mixer.Sound("Resources\pacman-die.mp3")
            pygame.mixer.Sound.play(sound)
           
           
            raise Exception ("Game Over")
    
    
    
    def is_collision(self, x1, y1, x2, y2):
      if x1 >= x2 and x1 <= x2 + SIZE:
        if y1 >= y2 and y1 <= y2 + SIZE:
          return True
      return False  



    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('bold', 60)
        line1= font.render(f"Score : {self.snake.length - 1}", True , (255,255,255) ) 
        self.snake_game.blit(line1, (500,400))
        line2= font.render("GAME OVER !! Press Enter To Play Again Or ESC To Exit",True,(255,255,255))
        self.snake_game.blit(line2, (45,450))
        pygame.display.flip()
        
    def reset(self):
        self.snake = Snake(self.snake_game,2)
        self.apple = Apple(self.snake_game,)
    


    # let's make a run function

    def run(self):
        running = True
        pause=False
        while running:
            # here I will make this running false by any event like pressing escape key this will turn the running variable to false hence the loop will stop and the app will be closed
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.up()
                    
                    if event.key ==K_RETURN:
                        pause=False
                    
                    if event.key == K_DOWN:
                        self.snake.down()
                    if event.key == K_LEFT:
                        self.snake.left()
                    if event.key == K_RIGHT:
                        self.snake.right()
                
            try: 
                 if not pause:
                      self.play()
            except Exception as e:
                 pause= True
                 self.show_game_over()
                 self.reset()
                 time.sleep(0.1)


if __name__ == "__main__":
    game = Game()
    game.run()