import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame
import Player

pygame.init()


def main():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    player = Player.Player(screen)
    font = pygame.font.SysFont("Arial", 32)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
        dt = clock.tick(60)
        fps = clock.get_fps()
        screen.fill((0, 0, 0))
        fps_text = font.render(f"FPS: {int(fps)}", False, (255, 255, 255))
        screen.blit(fps_text, (0, 0))
        player.move(dt)
        player.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
