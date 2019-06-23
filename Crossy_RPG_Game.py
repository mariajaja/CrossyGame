# Gain access to pygame library
import pygame

# Screen info for running pygame
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE_COLOR = (255, 255, 255)   
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

class Game:
    
    TICK_RATE = 60

    # Initializer for the game class to set up title, width and height
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('images/player.png', 275, 500, 50, 50)
        enemy_0 = EnemyCharacter('images/enemy0.png', 20, 300, 50, 50)
        treasure = GameObject('images/treasure.png', 275, 50, 50, 50)
        
        while not is_game_over:

            for event in pygame.event.get():
                # Allows exit of game when that type is detected
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    is_game_over = True
                # Detects when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # Move up if up key pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down if down key pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # Detect when key is released and stop movement
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)
                
            self.game_screen.fill(WHITE_COLOR)

            # Draw treasure
            treasure.draw(self.game_screen)
            
            # Update player position
            player_character.move(direction, self.height)
            # Draw player at new position
            player_character.draw(self.game_screen)

            # Update enemy position
            enemy_0.move(self.width)
            # Draw enemy at new position
            enemy_0.draw(self.game_screen)

            # End game if collision between enemy or treasure
            if player_character.detect_collision(enemy_0):
                is_game_over = True
            elif player_character.detect_collision(treasure):
                is_game_over = True
            
            pygame.display.update()
            clock.tick(self.TICK_RATE)
            
class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        
        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height
        
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerCharacter(GameObject):

    SPEED = 10
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function to move character up or down     
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        # Make sure the character never goes past the bottom of the screen    
        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50

    def detect_collision(self, other_body):
        # Checks if not overlapping in y-axis
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        # Checks if not overlapping in x-axis
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        # Collided.
        return True
            

# Class to represent enemies moving left to right and right to left
class EnemyCharacter(GameObject):

    SPEED = 10
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character right once it hits too far on left
    # and left once it hits too far right on screen
    def move(self, max_width):
        if self.x_pos <= 10:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 30:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
        
pygame.init()

# create a new instance of a Game
new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()


# Quit game  
pygame.quit()
quit()
