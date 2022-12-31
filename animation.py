import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super.__init__()
        self.screen = screen
        self.sprites = []
        for i in range(11):
            self.sprites.append(pygame.image.load(f"0b58c16f14484f15c0eaba09e4c55cd4vkuL7P0nqA9NmTQL-{i}.jpg"))
        self.curr_sprite = 0
        self.curr_img = self.sprites[self.curr_sprite]

        self.rect = self.curr_img.get_rect()
        self.rect.topleft = (x,y)

    def update(self):
        self.curr_sprite += 1 if self.curr_sprite < 28 else 0
        self.curr_img = self.sprites[self.curr_sprite]