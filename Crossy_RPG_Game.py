import pygame

pygame.init()

#Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Crossy RPG'
# Colors according to RGB codes
WHITE_COLOR = (255, 255, 255)   
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()
# set next iteration of clock (typical FPS is 60)
TICK_RATE = 60
is_game_over = False

# Create the window of specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set the game window color to white
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

player_image = pygame.image.load('images/player.png')
player_image = pygame.transform.scale(player_image, (50, 50))

# Main game loop, used to update all gameplay such as movement, checks and graphics
while not is_game_over:

    # Loop to get thru all events occuring at any given time
    # Events are most often mouse movement, mouse and button clicks or exit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
            
        print(event)

    game_screen.blit(player_image, (275, 275))

    # Draw rectangle on top of the game screen canvas (x, y, width, height)
    # pygame.draw.rect(game_screen, BLACK_COLOR, [250, 250, 100, 100])
    # Draw circle on top of game screen (x, y, radius)
    # pygame.draw.circle(game_screen, BLACK_COLOR, (300, 200), 50)
       
    pygame.display.update()
    clock.tick(TICK_RATE)
    
pygame.quit()
quit()
