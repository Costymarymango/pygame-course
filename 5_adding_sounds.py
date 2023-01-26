import pygame

# Intialize pygame
pygame.init()

# Create a displaysurface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds")

#Load sound effects
explosion = pygame.mixer.Sound('explosion.wav')
chirp = pygame.mixer.Sound('chirp.wav')

# Play the sound effects
explosion.play()
pygame.time.delay(2000)
chirp.play() 
pygame.time.delay(2000)

# Change the volume of a sound effect
chirp.set_volume(.1)
chirp.play()

# Load background music
pygame.mixer.music.load('music_1.wav')

# Play and stop the music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
chirp.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()
# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
# End the game
pygame.quit()