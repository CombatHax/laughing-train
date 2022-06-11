import pygame


class Player:
    def __init__(self, surf: pygame.Surface):
        self.surf = surf
        self.pos = [0, 500, 100, 100]
        self.upvel = 0
        self.jumping = False
        self.jumpvel = 0

    def move(self, dt):
        keys = pygame.key.get_pressed()
        movement = 0
        if keys[pygame.K_a]:
            movement -= 1
        if keys[pygame.K_d]:
            movement += 1
        if keys[pygame.K_SPACE]:
            if not self.jumping:
                self.jumping = True
                self.jumpvel = -2
        if self.jumping:
            if self.jumpvel >= 0:
                self.jumping = False
            else:
                self.jumpvel += 0.1
        else:
            if self.pos[1] >= 500:
                self.pos[1] = 500
                self.upvel = 0
            else:
                self.upvel += 0.1
        if 0 < movement * dt + self.pos[0] < 700:
            self.pos[0] += movement * dt
            self.pos[1] += (self.upvel + self.jumpvel) * dt

    def draw(self):
        pygame.draw.rect(self.surf, (0, 0, 50), self.pos)
