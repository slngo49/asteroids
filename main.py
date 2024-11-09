# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    game_clock = pygame.time.Clock()
    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0,0,0))
        
        # Draw the player
        for player in drawable:
            player.draw(screen)  

        # FPS text
        font = pygame.font.Font(None, 36)  # None uses default font, 36 is size
        fps_text = font.render(f"FPS: {game_clock.get_fps():.1f}", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))  # Position at top-left corner

        pygame.display.flip()
        dt = game_clock.tick(60)/1000

        for player in updatable:
            player.update(dt) 

if __name__ == "__main__":
    main()